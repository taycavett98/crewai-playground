# Implementation Guide

This guide will help you implement the FastAPI backend step by step.

## Project Structure

```
crewai-playground/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app entry point - START HERE
│   ├── utils.py                   # Utility functions (config loading, etc.)
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py             # Pydantic request/response models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── health.py              # Health check endpoints
│   │   └── llm.py                 # LLM-related endpoints
│   └── services/
│       ├── __init__.py
│       └── ollama_client.py       # Your OllamaClient class
├── config.yaml
├── exceptions.py
├── pyproject.toml
└── README.md
```

## Implementation Order

Follow this order for best learning experience:

### 1. Utilities (app/utils.py)
**Start here** - you need config loading for everything else.

- Implement `load_config()` function
  - Use `Path` from pathlib
  - Use `yaml.safe_load()`
  - Handle FileNotFoundError
- Implement `probe_models()` function
  - Simple list intersection

### 2. Update OllamaClient (app/services/ollama_client.py)
- Add config loading to `__init__` (Option D pattern)
- Update `list_available_models()` to extract model names from response
- Update `_check_model()` to work with extracted names
- Test that it works!

### 3. Pydantic Schemas (app/models/schemas.py)
Define all the request/response models:

**Tips:**
- Use `Field()` for defaults and descriptions
- Example structure:
  ```python
  class GenerateRequest(BaseModel):
      prompt: str = Field(..., description="Text prompt for generation")
      stream: bool = Field(False, description="Enable streaming")
  ```

Implement in order:
1. `HealthResponse` (simplest)
2. `ModelsResponse`
3. `GenerateRequest` and `GenerateResponse`
4. `SwitchModelRequest` and `SwitchModelResponse`

### 4. Health Route (app/routes/health.py)
Simplest endpoint - implement this first to test the setup.

**Steps:**
1. Uncomment the router creation
2. Uncomment the health_check endpoint
3. Implement the logic:
   - Import OllamaClient
   - Call health_check()
   - Return HealthResponse
4. Handle exceptions with try/except

### 5. LLM Routes (app/routes/llm.py)
Implement endpoints in order:

1. **GET /llm/models** (easiest)
   - Call `list_available_models()`
   - Return ModelsResponse

2. **POST /llm/generate** (medium)
   - Extract prompt from request
   - Call `generate()`
   - Return GenerateResponse

3. **POST /llm/models/switch** (medium)
   - Extract model name from request
   - Call `change_model()`
   - Return SwitchModelResponse based on success/failure

### 6. Main App (app/main.py)
**Do this last** - wire everything together.

1. Uncomment FastAPI app creation
2. Uncomment CORS middleware
3. Import route modules
4. Include routers
5. Add root endpoint
6. Uncomment uvicorn.run()

## Testing Your API

### Running the server:
```bash
# From project root
python -m app.main

# Or with uvicorn directly
uvicorn app.main:app --reload
```

### Testing endpoints:

**Option 1: cURL**
```bash
# Health check
curl http://localhost:8000/health

# List models
curl http://localhost:8000/llm/models

# Generate text
curl -X POST http://localhost:8000/llm/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, how are you?"}'
```

**Option 2: FastAPI Docs (Recommended!)**
- Go to http://localhost:8000/docs
- Interactive UI to test all endpoints

**Option 3: Python script**
```python
import requests

response = requests.get("http://localhost:8000/health")
print(response.json())
```

## Common Issues & Tips

### Import Errors
If you get import errors, run from project root:
```bash
python -m app.main
```

### Ollama Connection Issues
- Make sure Ollama is running: `ollama ps`
- Check the port in config.yaml matches Ollama's port
- Default is usually `http://localhost:11434`

### Type Hints
- Use `list[str]` not `List[str]` (Python 3.9+)
- Use `Optional[str]` for nullable fields
- Import from `typing` if needed

### Exception Handling Pattern
```python
try:
    result = client.some_method()
    return SuccessResponse(data=result)
except OllamaConnectionError as e:
    raise HTTPException(status_code=503, detail=str(e))
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
```

## Questions to Think About While Coding

1. **What should happen if config.yaml is missing?**
   - Raise exception? Use defaults? You decide!

2. **Should you create a new OllamaClient for each request?**
   - Or create one instance and reuse it?
   - Think about state management (current model)

3. **How should streaming work?**
   - Return StreamingResponse vs regular response
   - This is advanced - skip for now if needed

4. **Error messages - how detailed should they be?**
   - Production: vague ("Internal server error")
   - Development: detailed (full stack trace)

## Next Steps After Implementation

1. Write a simple test script or use the docs UI
2. Test each endpoint
3. Handle edge cases (model not found, Ollama down, etc.)
4. Then move on to Streamlit UI!

## Need Help?

If you get stuck on any TODO:
1. Try to implement it yourself first
2. Test it
3. If it doesn't work, show me your code and I'll help debug
4. Ask specific questions about concepts you don't understand

Good luck! Start with `app/utils.py` and work your way through. 🚀
