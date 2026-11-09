from google.adk.agents.llm_agent import Agent
from google.adk.tools.langchain_tool import LangchainTool
from langchain_tavily import tavilySearch

#create the langchain tavily tool
tavily_search = tavilySearch(
    max_results = 5,
    topic = "general",
)
#wrap it so that adk can use it
tavily_tool = LangchainTool(tool=tavily_search)


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction=('Answer user questions to the best of your knowledge'
    "use google search when you need current information"
    "or need to verify facts."),
    tools = [tavily_tool],
)
