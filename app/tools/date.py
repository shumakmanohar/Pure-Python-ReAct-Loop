from datetime import datetime
from app.tools.models import ToolResult


async def get_current_date(_: str) -> ToolResult:
    return ToolResult(success=True, content=datetime.now().strftime("%Y-%m-%d"))
