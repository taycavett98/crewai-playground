"""LLM-related endpoints."""

from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    GenerateRequest,
    GenerateResponse,
    SwitchModelRequest,
    SwitchModelResponse,
    ModelsResponse
)
from app.services.ollama_client import OllamaClient

router = APIRouter()


@router.get("/models", response_model=ModelsResponse)
async def list_models():
    """
    List all available Ollama models.

    Returns:
        ModelsResponse with list of available models
    """
    try:
        client = OllamaClient()
        models = client.list_available_models()

        return ModelsResponse(
            models=models,
            count=len(models)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to list models: {str(e)}"
        )


@router.post("/generate", response_model=GenerateResponse)
async def generate_text(request: GenerateRequest):
    """
    Generate text using the current model.

    Args:
        request: GenerateRequest with prompt and options

    Returns:
        GenerateResponse with generated text
    """
    try:
        client = OllamaClient()
        response = client.generate(
            user_input=request.prompt,
            think=request.think,
            stream=request.stream
        )

        # Extract the response text from Ollama's response
        generated_text = response.get('response', '')

        return GenerateResponse(
            response=generated_text,
            model=client.model,
            created_at=response.get('created_at'),
            done=response.get('done', True)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Text generation failed: {str(e)}"
        )


@router.post("/models/switch", response_model=SwitchModelResponse)
async def switch_model(request: SwitchModelRequest):
    """
    Switch to a different model.

    Args:
        request: SwitchModelRequest with model name

    Returns:
        SwitchModelResponse with success status
    """
    try:
        client = OllamaClient()
        success = client.change_model(request.model)

        if success:
            return SwitchModelResponse(
                success=True,
                model=client.model,
                message=f"Successfully switched to {client.model}"
            )
        else:
            return SwitchModelResponse(
                success=False,
                model=client.model,
                message=f"Model {request.model} not available. Still using {client.model}"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to switch model: {str(e)}"
        )
