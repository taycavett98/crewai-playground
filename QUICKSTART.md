# Quick Start Guide

## ✅ What's Done

All the foundational code is implemented! You can now focus on CrewAI and LangGraph.

### Implemented Components

1. **Utils** (`app/utils.py`):
   - ✅ `load_config()` - Loads YAML configuration
   - ✅ `probe_models()` - Finds intersection of supported/available models
   - ✅ `setup_logging()` - Configures application logging

2. **OllamaClient** (`app/services/ollama_client.py`):
   - ✅ Config-driven initialization (Option D pattern)
   - ✅ `list_available_models()` - Gets models from Ollama
   - ✅ `generate()` - Text generation with temperature support
   - ✅ `change_model()` - Hot-swap models at runtime
   - ✅ `health_check()` - Verify Ollama is running

3. **Pydantic Schemas** (`app/models/schemas.py`):
   - ✅ All request/response models defined
   - ✅ Proper validation and documentation

4. **API Routes**:
   - ✅ `GET /health` - Health check endpoint
   - ✅ `GET /llm/models` - List available models
   - ✅ `POST /llm/generate` - Generate text
   - ✅ `POST /llm/models/switch` - Switch models

5. **FastAPI App** (`app/main.py`):
   - ✅ All routes wired up
   - ✅ CORS enabled
   - ✅ Logging configured
   - ✅ Auto-generated docs at `/docs`

## 🚀 Running the API

### Option 1: Using the run script (Recommended)
```bash
source .venv/bin/activate
python run.py
```

### Option 2: Using uvicorn directly
```bash
source .venv/bin/activate
uvicorn app.main:app --reload
```

### Option 3: Using uv
```bash
uv run uvicorn app.main:app --reload
```

## 🧪 Testing the API

### Interactive Docs (Best way!)
Visit: http://localhost:8000/docs

You'll see a beautiful Swagger UI where you can test all endpoints interactively!

### cURL Examples

**Health Check:**
```bash
curl http://localhost:8000/health
```

**List Models:**
```bash
curl http://localhost:8000/llm/models
```

**Generate Text:**
```bash
curl -X POST http://localhost:8000/llm/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain what an AI agent is in one sentence"}'
```

**Switch Model:**
```bash
curl -X POST http://localhost:8000/llm/models/switch \
  -H "Content-Type: application/json" \
  -d '{"model": "mistral"}'
```

## 🤖 Next Steps: Focus on Agents!

Now you can focus on what you want to learn: **CrewAI and LangGraph**

### CrewAI Implementation Ideas

Create `app/agents/crew_example.py`:

```python
from crewai import Agent, Task, Crew

# Example: Document analysis crew
analyzer = Agent(
    role='Content Analyzer',
    goal='Analyze text and extract key insights',
    backstory='Expert at understanding and summarizing content',
    llm=your_ollama_client
)

summarizer = Agent(
    role='Summarizer',
    goal='Create concise summaries',
    backstory='Skilled at distilling information',
    llm=your_ollama_client
)

# Define tasks and create crew
# ...
```

### LangGraph Implementation Ideas

Create `app/agents/langgraph_example.py`:

```python
from langgraph.graph import StateGraph, END

# Example: Text processing pipeline
def analyze_node(state):
    # Your logic
    pass

def summarize_node(state):
    # Your logic
    pass

# Build the graph
workflow = StateGraph(dict)
workflow.add_node("analyze", analyze_node)
workflow.add_node("summarize", summarize_node)
# ...
```

## 📝 Suggested Learning Path

1. **Start Simple**: Create a 2-agent CrewAI workflow
   - One agent analyzes text
   - One agent summarizes findings
   - Connect to your OllamaClient

2. **Add API Endpoint**: Create `/agents/analyze` endpoint
   - Accepts text input
   - Runs your crew
   - Returns results

3. **Try LangGraph**: Build equivalent workflow
   - Same functionality as CrewAI version
   - Compare the developer experience

4. **Compare Frameworks**:
   - Which is easier to understand?
   - Which gives more control?
   - Which fits your use case better?

## 🔍 Project Structure

```
crewai-playground/
├── app/
│   ├── main.py                 # ✅ Ready
│   ├── utils.py                # ✅ Ready
│   ├── models/
│   │   └── schemas.py          # ✅ Ready
│   ├── routes/
│   │   ├── health.py           # ✅ Ready
│   │   └── llm.py              # ✅ Ready
│   ├── services/
│   │   └── ollama_client.py    # ✅ Ready
│   └── agents/                 # 👈 Create this for your agent code!
│       ├── crew_example.py     # Your CrewAI experiments
│       └── langgraph_example.py # Your LangGraph experiments
├── config.yaml                 # ✅ Ready
├── run.py                      # ✅ Ready to use
└── README.md
```

## 🐛 Troubleshooting

**Import errors?**
- Make sure you're running from project root
- Use `python run.py` not `python app/main.py`

**Ollama connection errors?**
- Check Ollama is running: `ollama ps`
- Verify config.yaml has correct base_url
- Make sure at least one model is pulled

**Config not found?**
- config.yaml must be in project root
- Check the path in load_config() calls

## 💡 Tips

- The FastAPI docs at `/docs` are your friend - use them!
- Check the logs for debugging info
- Start with simple 2-agent workflows
- Compare CrewAI vs LangGraph side-by-side

**You're all set! Focus on learning agents now.** 🎉
