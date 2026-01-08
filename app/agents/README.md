# Agents Directory

This is where you'll implement your CrewAI and LangGraph experiments!

## Getting Started with CrewAI

Create `crew_example.py` and try building a simple multi-agent workflow.

### Example Structure:

```python
from crewai import Agent, Task, Crew, Process
from app.services.ollama_client import OllamaClient

# Initialize your LLM
client = OllamaClient()

# Create agents
analyst = Agent(
    role='Text Analyst',
    goal='Analyze text and identify key themes',
    backstory='You are an expert at understanding text and finding patterns.',
    verbose=True,
    allow_delegation=False
)

summarizer = Agent(
    role='Summarizer',
    goal='Create concise, clear summaries',
    backstory='You excel at distilling complex information into clear summaries.',
    verbose=True,
    allow_delegation=False
)

# Create tasks
task1 = Task(
    description='Analyze this text and identify the main themes: {text}',
    agent=analyst,
    expected_output='A list of 3-5 main themes'
)

task2 = Task(
    description='Summarize the themes in 2-3 sentences',
    agent=summarizer,
    expected_output='A concise summary'
)

# Create crew
crew = Crew(
    agents=[analyst, summarizer],
    tasks=[task1, task2],
    process=Process.sequential  # Tasks run one after another
)

# Run it!
result = crew.kickoff(inputs={'text': 'Your text here...'})
print(result)
```

## Getting Started with LangGraph

Create `langgraph_example.py` for state machine workflows.

### Example Structure:

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

# Define your state
class GraphState(TypedDict):
    text: str
    analysis: str
    summary: str

# Define nodes (functions that process state)
def analyze_text(state: GraphState) -> GraphState:
    # Your analysis logic here
    client = OllamaClient()
    response = client.generate(f"Analyze this text: {state['text']}")
    state['analysis'] = response['response']
    return state

def summarize(state: GraphState) -> GraphState:
    # Your summary logic here
    client = OllamaClient()
    response = client.generate(f"Summarize: {state['analysis']}")
    state['summary'] = response['response']
    return state

# Build the graph
workflow = StateGraph(GraphState)

# Add nodes
workflow.add_node("analyze", analyze_text)
workflow.add_node("summarize", summarize)

# Add edges (define flow)
workflow.set_entry_point("analyze")
workflow.add_edge("analyze", "summarize")
workflow.add_edge("summarize", END)

# Compile
app = workflow.compile()

# Run it!
result = app.invoke({"text": "Your text here..."})
print(result)
```

## Comparison Points

As you build with both frameworks, consider:

### CrewAI
- **Pro**: Very intuitive role-based design
- **Pro**: Built-in memory and delegation
- **Pro**: Great for simulating teams of specialists
- **Con**: Less control over exact execution flow
- **Con**: More opinionated structure

### LangGraph
- **Pro**: Complete control over state and flow
- **Pro**: Flexible graph-based architecture
- **Pro**: Great for complex conditional logic
- **Con**: More boilerplate code
- **Con**: Steeper learning curve

## Next Steps

1. Implement a simple example in both frameworks
2. Create API endpoints to expose them
3. Compare developer experience
4. Choose the one that fits your use case better
5. Build something more complex!

Happy experimenting! 🚀
