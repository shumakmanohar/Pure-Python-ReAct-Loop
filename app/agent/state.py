from pydantic import BaseModel, Field 
from typing import Union
from app.agent.status import AgentStatus
from app.agent.events import (
    ThoughtEvent,
    ActionEvent,
    ObservationEvent,
    ErrorEvent,
    FinalAnswerEvent,
)

AgentEvent = Union[
    ThoughtEvent,
    ActionEvent,
    ObservationEvent,
    ErrorEvent,
    FinalAnswerEvent,
]

class AgentState(BaseModel):
    """
    Stores the complete runtime state of the agent.
    """
  
    goal :str
    status: AgentStatus = AgentStatus.IDLE
    iteration:int = 0
    max_iterations:int = 10
    events: list[AgentEvent] = Field(default_factory=list)
    finished: bool = False
    final_answer: str | None = None
    current_thought: str | None = None
    current_action: str | None = None
    token_usage: int = 0
    
    def add_event(self, event: AgentEvent):
        self.events.append(event)