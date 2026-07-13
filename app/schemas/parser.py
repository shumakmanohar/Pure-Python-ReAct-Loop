from pydantic import BaseModel
import re


class ParsedResponse(BaseModel):
  """A parsed response from the LLM."""
  
  thought: str | None = None
  action: str | None = None
  action_input: str | None = None
  final_answer: str | None = None
  
  

def parse_response(text: str) -> ParsedResponse:
  text = text.strip()
  
  if "Final Answer:" in text:
    # If the response contains a final answer, extract it
    final_answer = text.split("Final Answer:")[-1].strip()
    return ParsedResponse(final_answer=final_answer)
  
  thought = re.search(
        r"Thought:\s*(.*?)\nAction:",
        text,
        re.DOTALL,)
  
  action = re.search(
        r"Action:\s*(.*?)\nAction Input:",
        text,
        re.DOTALL,
  )

  action_input = re.search(
        r"Action Input:\s*(.*)",
        text,
        re.DOTALL,
  )
  
  return ParsedResponse(
        thought=thought.group(1).strip() if thought else None,
        action=action.group(1).strip() if action else None,
        action_input=action_input.group(1).strip() if action_input else None,
  )
  
  
  