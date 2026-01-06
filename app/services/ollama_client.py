from typing import Optional
import ollama
import logging
import sys
from pathlib import Path

# Add parent directory to path so we can import from app
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from app.utils import load_config

logger = logging.getLogger(__name__)


class OllamaClient():

    def __init__(self, model: Optional[str] = None, config: Optional[dict] = None):
        """
        Initialize OllamaClient.

        Args:
            model: Model name to use. If None, uses default from config.
            config: Configuration dict. If None, loads from config.yaml.
        """
        if config is None:
            full_config = load_config()
            config = full_config.get('ollama', {})

        self.config = config
        self.base_url = config.get('base_url', 'http://localhost:11434')
        self.model = model or config.get('default_model', 'llama2')
        self.supported_models = config.get('supported_models', [])

    def list_available_models(self) -> list[str]:
        """
        List all models available in Ollama.

        Returns:
            list[str]: List of model names
        """
        try:
            response = ollama.list()
            # ollama.list() returns a dict with 'models' key containing list of model objects
            if isinstance(response, dict) and 'models' in response:
                model_names = [model['name'] for model in response['models']]
            else:
                model_names = []

            logger.info(f'Available models: {model_names}')
            return model_names
        except Exception as e:
            logger.error(f'Failed to list models: {e}')
            raise

    def generate(self, user_input: str, think: bool = False, stream: bool = False):
        """
        Generate text using the current model.

        Args:
            user_input: The prompt/input text
            think: Enable thinking mode (if supported by model)
            stream: Enable streaming response

        Returns:
            dict: Response from Ollama with generated text and metadata
        """
        try:
            response = ollama.generate(
                model=self.model,
                prompt=user_input,
                options={'temperature': self.config.get('temperature', 0.7)}
            )
            logger.debug(f'Generated response from {self.model}')
            return response
        except Exception as e:
            logger.error(f'Generation failed: {e}')
            raise 
    
    def _check_model(self, model: str) -> bool:
        """
        Check if a model is available.

        Args:
            model: Model name to check

        Returns:
            bool: True if model is available
        """
        try:
            available_models = self.list_available_models()
            # Check if the model name is in available models (exact match or prefix match)
            for available_model in available_models:
                if model in available_model or available_model.startswith(model):
                    return True
            return False
        except Exception as e:
            logger.error(f'Error checking model {model}: {e}')
            return False

    def change_model(self, model: str) -> bool:
        """
        Switch to a different model.

        Args:
            model: Model name to switch to

        Returns:
            bool: True if successful, False if model not available
        """
        if self._check_model(model):
            self.model = model
            logger.info(f'Switched to model: {model}')
            return True
        else:
            logger.warning(f'Model {model} not available')
            return False

    def health_check(self) -> dict:
        """
        Check if Ollama is running and responsive.

        Returns:
            dict: Status information from Ollama

        Raises:
            Exception: If Ollama is not reachable
        """
        try:
            status = ollama.ps()
            logger.info('Ollama health check passed')
            return status
        except Exception as e:
            logger.error(f'Ollama health check failed: {e}')
            raise