from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()


def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3-32b"),
        markdown=True,
        add_history_to_context=True,
        debug_mode=True
    )


agent = build_agent()

agent.print_response("What is the capital of Himachal Pradesh?")
agent.print_response("What is the best time or season to visit it?")
