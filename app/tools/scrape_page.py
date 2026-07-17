from app.tools.models import ToolResult
import httpx
from bs4 import BeautifulSoup


async def scrape_page(url: str) -> ToolResult:
    try:
        async with httpx.AsyncClient(
            follow_redirects=True,
            timeout=20,
        ) as client:
            response = await client.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            text = text[:6000]
            return ToolResult(success=True, content=text)
    except Exception as e:
        return ToolResult(success=False, content=str(e))
