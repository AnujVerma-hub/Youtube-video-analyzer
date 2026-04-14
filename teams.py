from agno.agent import Agent
from agno.models.groq import Groq
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()


eng_member = Agent(name="English Agent", role="Answer in English")
chi_member = Agent(name="Chinese Agent", role="Answer in Chinese")
hindi_member = Agent(name="Hindi Agent", role="Answer in Hindi")

team_leader = Team(
    name="Language Translator",
    members=[eng_member, chi_member, hindi_member],
    model=Groq(id="qwen/qwen3-32b"),
    markdown=True,
    instructions="""All the members must answer the query in their specific language. 
                    Do not route to just one agent. Output must contain all agent responses."""
)


team_leader.print_response("What is the capital of India?")
