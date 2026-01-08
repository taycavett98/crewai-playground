from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
from services.ollama_client import OllamaClient

# define shared state
class GraphState(TypedDict):
    text: str
    analysis: str
    summary: str

# Define nodes (functions that process state)
def analyze_text(state: GraphState) -> GraphState:

    client = OllamaClient()
    response = client.generate(f"Analyze this text: {state['text']}")
    state['analysis'] = response['response']
    return state

def summarize(state: GraphState) -> GraphState:

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

app = workflow.compile()

result = app.invoke({"text": "tell me about continual leearning"})
print(result)