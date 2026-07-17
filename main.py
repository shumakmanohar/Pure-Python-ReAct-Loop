import asyncio
import sys

from app.agent.engine import run_agent
from app.agent.state import AgentState


async def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print('python3 main.py "Your goal"')
        return

    goal = sys.argv[1]
    state = AgentState(goal=goal)
    await run_agent(state)


asyncio.run(main())
