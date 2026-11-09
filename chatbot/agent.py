from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import Litellm
from google.genai import types



root_agent = Agent(
    model=Litellm(model="openai/gpt-4o"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    generate_content_config=types.GenerateContentConfig(
        temperature = 0.3,
        max_output_tokens=800,

    )
)
