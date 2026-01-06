"""Utility functions for the application."""

import yaml
from pathlib import Path
from typing import Optional


def load_config(config_path: str = "config.yaml") -> dict:
    """
    Load configuration from YAML file.

    Args:
        config_path: Path to config file (default: config.yaml)

    Returns:
        dict: Configuration dictionary

    Raises:
        FileNotFoundError: If config file doesn't exist
        yaml.YAMLError: If YAML is invalid

    Example:
        >>> config = load_config()
        >>> ollama_config = config['ollama']
        >>> print(ollama_config['base_url'])
    """
    config_file = Path(config_path)

    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    return config


def probe_models(available_models: list[str], supported_models: list[str]) -> list[str]:
    """
    Get intersection of available and supported models.

    Args:
        available_models: Models available in Ollama
        supported_models: Models supported by this application

    Returns:
        list[str]: Models that are both available and supported

    Example:
        >>> available = ['llama2', 'mistral', 'random-model']
        >>> supported = ['llama2', 'codellama']
        >>> probe_models(available, supported)
        ['llama2']
    """
    return [model for model in supported_models if model in available_models]


def setup_logging(level: str = "INFO"):
    """Configure application logging."""
    import logging

    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
