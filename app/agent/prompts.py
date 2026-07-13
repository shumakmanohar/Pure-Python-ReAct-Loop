from app.agent.state import AgentState
from app.agent.history import format_history


SYSTEM_PROMPT = """
You are an autonomous AI research agent.

Your job is to collect information by thinking step-by-step.

You MUST follow the ReAct pattern.

For every iteration, respond in EXACTLY this format.

Thought:
<reasoning>

Action:
<tool_name>

Action Input:
<input>

OR

Final Answer:
<answer>

Available Tools:

1. web_search
2. scrape_page

Never invent tools.

Never skip the Thought.

Only return ONE action at a time.
""".strip()


def build_prompt(state: AgentState) -> str:
    """
    Build the complete prompt sent to the LLM.
    """

    history = format_history(state.events)

    prompt = f"""
    Goal:
    {state.goal}
    Current Iteration:
    {state.iteration}
    History:
    {history}
    What should you do next?
    """

    return prompt.strip()
