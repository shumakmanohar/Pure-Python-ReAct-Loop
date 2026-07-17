from app.tools.models import ToolResult
from app.tools.web_search import web_search
from app.tools.scrape_page import scrape_page
from app.tools.date import get_current_date


async def execute_tool(
    tool_name: str,
    tool_input: str,
) -> ToolResult:

    if tool_name == "web_search":
        return await web_search(tool_input)

    if tool_name == "scrape_page":
        return await scrape_page(tool_input)

    if tool_name == "get_current_date":
        return await get_current_date(tool_input)

    return ToolResult(
        success=False,
        content=f"Unknown tool: {tool_name}",
    )
