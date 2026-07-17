from pydantic import BaseModel


class ToolResult(BaseModel):
    success: bool
    content: str
    metadata: dict | None = None
