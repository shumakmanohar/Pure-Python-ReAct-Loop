async def execute_tool(
    tool_name: str,
    tool_input: str,
) -> str:

    if tool_name == "web_search":
        return """
    Company:
    Stripe

    CEO:
    Patrick Collison

    Product:
    Online Payment Infrastructure

    Website:
    https://stripe.com
    """

    if tool_name == "scrape_page":
        return f"Mock HTML for: {tool_input}"

    raise ValueError(f"Unknown tool: {tool_name}")
