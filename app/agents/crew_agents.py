from crewai import Agent, Task, Crew, Process, LLM
from app.services.ollama_client import OllamaClient
import os
import warnings

# Suppress all warnings and litellm logging
os.environ['LITELLM_LOG'] = 'CRITICAL'
warnings.filterwarnings('ignore')

client = OllamaClient()

ollama_llm = LLM(
    model=f"ollama/{client.model}",  # Uses "gpt-oss:20b" from your config
    base_url=client.base_url  # Uses "http://localhost:8080" from your config
)

# crew
analyst = Agent(
    role='Text Analyst',
    goal='Analyze text and identify key themes',
    backstory='You are an expert at understanding text and finding patterns.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

summarizer = Agent(
    role='Summarizer',
    goal='Create concise, clear summaries',
    backstory='You excel at distilling complex information into clear summaries.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

# tasks
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

# establish crew
crew = Crew(
    agents=[analyst, summarizer],
    tasks=[task1, task2],
    process=Process.sequential  # Tasks run one after another
)


def run_analysis_crew(text: str) -> str:
    """
    Run the analysis crew on the provided text.

    Args:
        text: Text to analyze

    Returns:
        str: The final summary from the crew
    """
    result = crew.kickoff(inputs={'text': text})
    return str(result)


if __name__ == "__main__":
    # Example usage
    input_text = 'I am interested in getting more knowledgable about the stock market. what factors should i look at daily?'
    result = run_analysis_crew(input_text)

    print("\n" + "="*80)
    print("FINAL RESULT:")
    print("="*80)
    print(result)
    print("="*80)