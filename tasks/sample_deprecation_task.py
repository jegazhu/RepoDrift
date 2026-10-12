"""
Sample Benchmark Task definition for RepoDrift.
Demonstrates the transition from a deprecated utility function to its modern equivalent.
"""

def legacy_fetch_data(endpoint: str):
    """[DEPRECATED in v1.0] Use modern_async_fetch instead."""
    import urllib.request
    with urllib.request.urlopen(endpoint) as response:
        return response.read()

async def modern_async_fetch(endpoint: str):
    """[ACTIVE] Modern asynchronous client implementation."""
    import httpx
    async with httpx.AsyncClient() as client:
        response = await client.get(endpoint)
        return response.text
