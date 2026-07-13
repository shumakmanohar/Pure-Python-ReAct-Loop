import asyncio

from app.agent.engine import run_agent
from app.agent.state import AgentState
import app.tools

async def main():
  state = AgentState(
        goal="""
Research Stripe.

Find:

- Company Description

- CEO

- Main Product

Then provide a summary.
"""
    )
  
  result = await run_agent(state)
  print("\n")
  print("=" * 60)
  print("FINAL ANSWER")
  print("=" * 60)
  print(result.final_answer)
  
asyncio.run(main())