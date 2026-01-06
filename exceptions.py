"""Custom exceptions for the CrewAI Playground project."""


class OllamaError(Exception):
    """Base exception for all Ollama-related errors."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class OllamaConnectionError(OllamaError):
    """Raised when unable to connect to Ollama server."""

    def __init__(self, base_url: str, original_error: Exception = None):
        self.base_url = base_url
        self.original_error = original_error
        message = f"Failed to connect to Ollama server at {base_url}"
        if original_error:
            message += f": {str(original_error)}"
        super().__init__(message)


class ModelNotFoundError(OllamaError):
    """Raised when requested model is not available."""

    def __init__(self, model_name: str, available_models: list[str] = None):
        self.model_name = model_name
        self.available_models = available_models
        message = f"Model '{model_name}' not found"
        if available_models:
            message += f". Available models: {', '.join(available_models)}"
        super().__init__(message)


class GenerationError(OllamaError):
    """Raised when text generation fails."""

    def __init__(self, model_name: str, prompt: str, original_error: Exception = None):
        self.model_name = model_name
        self.prompt = prompt
        self.original_error = original_error
        message = f"Generation failed for model '{model_name}'"
        if original_error:
            message += f": {str(original_error)}"
        super().__init__(message)


# usage
if __name__ == "__main__":
    # basic exception
    try:
        raise OllamaConnectionError("http://localhost:11434")
    except OllamaConnectionError as e:
        print(f"Caught error: {e}")
        print(f"Base URL was: {e.base_url}")

    # exception with context
    try:
        raise ModelNotFoundError("llama3", ["llama2", "mistral"])
    except ModelNotFoundError as e:
        print(f"\nCaught error: {e}")
        print(f"Available: {e.available_models}")

    # nested exception
    try:
        original = ValueError("Network timeout")
        raise OllamaConnectionError("http://localhost:11434", original)
    except OllamaConnectionError as e:
        print(f"\nCaught error: {e}")
        print(f"Original error: {e.original_error}")
