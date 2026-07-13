from app.agent.events import (
    ThoughtEvent,
    ActionEvent,
    ObservationEvent,
    ErrorEvent,
    FinalAnswerEvent,
)


def format_history(events: list) -> str:
    sections = []

    for event in events:
        if isinstance(event, ThoughtEvent):
            sections.append(f"Thought:\n{event.thought}")

        elif isinstance(event, ActionEvent):
            sections.append(
                f"Action:\n{event.tool}\n\nAction Input:\n{event.tool_input}"
            )

        elif isinstance(event, ObservationEvent):
            sections.append(f"Observation:\n{event.observation}")

        elif isinstance(event, ErrorEvent):
            sections.append(f"Error:\n{event.error}")

        elif isinstance(event, FinalAnswerEvent):
            sections.append(f"Final Answer:\n{event.answer}")

    return "\n\n".join(sections)
