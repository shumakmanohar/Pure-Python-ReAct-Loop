from app.agent.events import (
    ActionEvent,
    FinalAnswerEvent,
    ObservationEvent,
    ThoughtEvent,
)
from app.agent.status import AgentStatus
from app.schemas.parser import parse_response
from app.agent.prompts import build_prompt
from app.agent.state import AgentState
from app.llm.client import generate
from app.tools.registry import execute_tool
from app.console import (
    show_iteration,
    show_action,
    show_final,
    show_goal,
    show_observation,
    show_thought,
)


async def run_agent(state: AgentState):
    """
    Main ReAct execution loop.

    Responsibilities:
        - Build prompt
        - Call LLM
        - Parse response
        - Execute tool
        - Store observations
        - Repeat
    """
    state.status = AgentStatus.RUNNING
    show_goal(state.goal)

    while True:
        # Guard 1
        if state.iteration >= state.max_iterations:
            state.status = AgentStatus.FAILED
            state.finished = True
            state.final_answer = "Max iterations reached."
            return state

        state.iteration += 1

        show_iteration(state.iteration)

        # Build prompt
        prompt = build_prompt(state)

        # print("=" * 60)
        # print(f"\n Prompt : {prompt} \n")
        # print("=" * 60)

        # Ask LLM
        response_text = await generate(prompt)

        # Parse response
        parsed = parse_response(response_text)

        # Thought
        if parsed.thought:
            state.current_thought = parsed.thought
            state.add_event(ThoughtEvent(thought=parsed.thought))
            show_thought(parsed.thought)

        # Finished?
        if parsed.final_answer:
            state.status = AgentStatus.FINISHED
            state.finished = True
            state.final_answer = parsed.final_answer
            state.add_event(FinalAnswerEvent(answer=parsed.final_answer))
            show_final(parsed.final_answer)
            return state

        # Action
        if parsed.action is None:
            raise RuntimeError("LLM did not return an action.")

        if parsed.action_input is None:
            raise RuntimeError("LLM did not return action input.")

        state.current_action = parsed.action
        state.add_event(ActionEvent(tool=parsed.action, tool_input=parsed.action_input))

        # Execute tool
        show_action(parsed.action, parsed.action_input)

        result = await execute_tool(parsed.action, parsed.action_input)

        show_observation(result.content)

        state.add_event(ObservationEvent(observation=result.content))
