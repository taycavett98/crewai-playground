"""Health check endpoints."""

from fastapi import APIRouter, HTTPException
from app.models.schemas import HealthResponse
from app.services.ollama_client import OllamaClient

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Check if the API and Ollama are healthy.

    Returns:
        HealthResponse with status information

    Raises:
        HTTPException if Ollama is unreachable
    """
    try:
        client = OllamaClient()
        status = client.health_check()

        return HealthResponse(
            status="healthy",
            ollama_running=True,
            details=status
        )
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Ollama is not reachable: {str(e)}"
        )
