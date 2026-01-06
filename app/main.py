"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, llm
from app.utils import setup_logging

# Setup logging
setup_logging("INFO")

# Create FastAPI app instance
app = FastAPI(
    title="CrewAI Playground API",
    version="0.1.0",
    description="API for experimenting with LLMs, agents, and media processing"
)

# Add CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(llm.router, prefix="/llm", tags=["llm"])


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "CrewAI Playground API",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
