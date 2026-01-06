"""Pydantic models for request/response validation."""

from pydantic import BaseModel, Field
from typing import Optional, Any


class GenerateRequest(BaseModel):
    """Request model for text generation."""
    prompt: str = Field(..., description="Text prompt for generation")
    stream: bool = Field(False, description="Enable streaming response")
    think: bool = Field(False, description="Enable thinking mode (if supported)")


class GenerateResponse(BaseModel):
    """Response model for text generation."""
    response: str = Field(..., description="Generated text")
    model: str = Field(..., description="Model used for generation")
    created_at: Optional[str] = Field(None, description="Timestamp of generation")
    done: bool = Field(True, description="Whether generation is complete")


class SwitchModelRequest(BaseModel):
    """Request model for switching models."""
    model: str = Field(..., description="Name of model to switch to")


class SwitchModelResponse(BaseModel):
    """Response model for model switching."""
    success: bool = Field(..., description="Whether switch was successful")
    model: str = Field(..., description="Current model name")
    message: Optional[str] = Field(None, description="Additional information")


class ModelsResponse(BaseModel):
    """Response model for listing models."""
    models: list[str] = Field(..., description="List of available model names")
    count: int = Field(..., description="Number of available models")


class HealthResponse(BaseModel):
    """Response model for health check."""
    status: str = Field(..., description="Health status (healthy/unhealthy)")
    ollama_running: bool = Field(..., description="Whether Ollama is running")
    details: Optional[dict] = Field(None, description="Additional health information")
