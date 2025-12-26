# CrewAI Playground

A learning project to explore AI agents, Model Context Protocol (MCP), and multi-agent frameworks while building practical media processing capabilities.

## Overview

This project is designed as a hands-on learning environment following KISS (Keep It Simple, Stupid) principles. The goal is to understand and experiment with:

- **LLM Integration**: Hot-swappable models via Ollama
- **Media Processing**: Video/audio transcription using FFmpeg and Faster-Whisper
- **Agent Frameworks**: Experimenting with CrewAI and LangGraph
- **MCP Integration**: Leveraging Model Context Protocol
- **Modern Stack**: FastAPI backend with Streamlit UI

### Architecture Vision

```
┌─────────────┐
│  Streamlit  │ (Simple UI for model selection & file upload)
│     UI      │
└──────┬──────┘
       │
┌──────▼──────┐
│   FastAPI   │ (REST API Backend)
│   Backend   │
└──────┬──────┘
       │
       ├─► LLM Hub (Ollama wrapper with hot-swappable models)
       │
       ├─► Media Processor (FFmpeg + Faster-Whisper pipeline)
       │
       ├─► Agent Orchestrator (CrewAI/LangGraph experiments)
       │
       └─► MCP Server (exposes capabilities via MCP)
```

## Setup

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (fast Python package manager)
- [Ollama](https://ollama.ai) running locally
- FFmpeg (for media processing - future)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd crewai-playground
```

2. Initialize the project with uv:
```bash
uv init
uv add pyyaml ollama
```

3. Configure your `config.yaml`:
```yaml
ollama:
  base_url: "http://localhost:11434"
  default_model: "llama2"
  timeout: 30
  temperature: 0.7
  supported_models:
    - llama2
    - mistral
    - codellama
```

4. Pull your desired models in Ollama:
```bash
ollama pull llama2
ollama pull mistral
```

5. Verify Ollama is running:
```bash
ollama ps
```

## Current Status

### Completed
- Project structure and configuration
- `OllamaClient` class with core functionality:
  - Model initialization
  - Text generation (with streaming support)
  - Model switching at runtime
  - Health checks
  - Available models listing
- Custom exception hierarchy for error handling
- YAML-based configuration system

### In Progress
- Config file loading (Option D: default to loading, allow override)
- Model probing (intersection of supported + available models)
- Test script for `OllamaClient`

### Not Started
- ⬜ FFmpeg wrapper class
- ⬜ Faster-Whisper integration
- ⬜ CrewAI agent setup
- ⬜ LangGraph workflow experiments
- ⬜ FastAPI backend
- ⬜ Streamlit UI
- ⬜ MCP server implementation

## Project Structure

```
crewai-playground/
├── config.yaml           # Configuration for Ollama and future services
├── ollama_client.py      # Main Ollama client wrapper
├── exceptions.py         # Custom exception classes
├── test_ollama.py        # Test script (coming soon)
├── utils.py             # Utility functions (coming soon)
└── README.md            # This file
```

## Roadmap

### Phase 1: LLM Foundation (Current)
1. Complete `OllamaClient` with config loading
2. Implement `probe_models()` for runtime model discovery
3. Write test script to validate all functionality
4. Add proper logging configuration

### Phase 2: Media Processing
1. Design `FFmpegProcessor` class for audio extraction
2. Integrate Faster-Whisper for transcription
3. Create pipeline: video → audio → transcript
4. Handle common video formats (mp4, mov, avi)

### Phase 3: Agent Framework Experiments
1. **CrewAI**: Build multi-agent workflow for transcript analysis
   - Summarization agent
   - Key points extraction agent
   - Action items agent
2. **LangGraph**: Implement state machine for processing pipeline
   - Conditional routing based on file type
   - Error recovery and retry logic

### Phase 4: API & UI
1. FastAPI backend:
   - File upload endpoints
   - Processing status tracking
   - Model selection API
2. Streamlit UI:
   - Simple file upload
   - Model dropdown (hot-swappable)
   - Processing progress
   - Results display

### Phase 5: MCP Integration
**Goal:** Expose application capabilities via Model Context Protocol for integration with Claude Desktop and other MCP clients.

**What is MCP?**
- Protocol for connecting AI assistants to external tools and data sources
- Allows Claude (or other LLMs) to interact with your transcription/agent system
- Enables workflows like: "Claude, transcribe this video and analyze it with CrewAI agents"

**Implementation Steps:**
1. **MCP Server Setup**
   - Install `mcp` package
   - Create MCP server that exposes tools/resources
   - Define server capabilities (tools, resources, prompts)

2. **Expose Tools via MCP**
   - `transcribe_video` - Process video file and return transcript
   - `run_crew_analysis` - Execute CrewAI workflow on text
   - `run_langgraph_flow` - Execute LangGraph state machine
   - `list_models` - Show available Ollama models
   - `generate_text` - Simple text generation

3. **Expose Resources**
   - Access to transcripts
   - Processing status/history
   - Agent workflow results

4. **Integration Examples**
   - Connect to Claude Desktop app
   - Command-line MCP client examples
   - Document how to add server to Claude config

5. **Learning Outcomes**
   - Understand MCP protocol design
   - Learn tool/resource patterns
   - Practice API design for AI consumption

## Design Principles

- **KISS**: Keep implementations simple and focused
- **Dependency injection**: Design for testability and flexibility
- **Fail fast**: Use custom exceptions for clear error handling
- **Config-driven**: Externalize configuration for easy experimentation

## Learning Resources

- [Ollama Documentation](https://ollama.ai/docs)
- [CrewAI Documentation](https://docs.crewai.com)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [MCP Specification](https://modelcontextprotocol.io)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Streamlit Documentation](https://docs.streamlit.io)
