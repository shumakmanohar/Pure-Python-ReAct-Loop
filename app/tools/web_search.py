from app.tools.models import ToolResult
from ddgs import DDGS


async def web_search(query: str) -> ToolResult:

    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
        if not results:
            return ToolResult(success=False, content="No search results found.")

        formatted = []

        for result in results:
            formatted.append(
                f"""Title:{result["title"]}URL: {result["href"]}Snippet: {result["body"]}"""
            )

        return ToolResult(success=True, content="\n-----------\n".join(formatted))
