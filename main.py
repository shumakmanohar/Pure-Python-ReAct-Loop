import asyncio

from app.agent.engine import run_agent
from app.agent.state import AgentState


async def main():
    state = AgentState(
        goal="""
Summarize today's AI news.
Include:

- Major announcements
- Companies involved
- Why each story matters

Produce a concise summary.
"""
    )

    result = await run_agent(state)
    print("\n")
    print("=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)
    print(result.final_answer)


asyncio.run(main())
