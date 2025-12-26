from typing import Optional
import ollama
SUPPORTED_MODELS = [] # TODO: read from config or hard code?

import logging

logger = logging.getLogger(__name__) # TODO: set this up somewhere

class OllamaClient():

    def __init__(self, model: str):
        self.model = model

    def list_available_models(self)->list[str]:
        """
        Docstring for list_available_models
        
        :param self: Description
        :return: Description
        :rtype: list[str]
        """
        models = ollama.list()
        logger.info(f'models type: {type(models)}')
        logger.info(f'models response from ollama.list(): {models}')
        return models

    def generate(self, user_input: str, think = False, stream=False):
        response = ollama.generate(model=self.model, prompt= user_input, think=think, stream=stream)

        logger.debug(f'RESPONSE: {response}')
        return response 
    
    def _check_model(self, model)->bool:
        models_in_client = ollama.list()
        # extract models
        logger.info(f'models_in_client: {models_in_client}')
        if model in models_in_client:
            return True
        else:
            return False

    def change_model(self, model: str):
        if self._check_model(model):
            self.model = model
            return True
        else:
            return False

    def health_check(self):
        return ollama.ps()