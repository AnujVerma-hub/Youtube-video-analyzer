from agno.agent import Agent

from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools

from dotenv import load_dotenv

load_dotenv()


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(),Newspaper4kTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True,
        debug_mode=True
    )

groq_agent = build_agent()

groq_agent.print_response("Is it safe to travel to UAE today?. And also summarize news articles for this context in economic times and New York Times.")