import os
import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()
GITHUB_TOOLS_ALLOWLIST = {
    "get_file_contents",
}

def get_mcp_client() -> MultiServerMCPClient:
    github_pat = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
    if not github_pat:
        raise ValueError("GITHUB_PERSONAL_ACCESS_TOKEN not found. Set it in your .env file.")

    return MultiServerMCPClient(
        {
            "github": {
                "url": "https://api.githubcopilot.com/mcp/",
                "transport": "streamable_http",
                "headers": {
                    "Authorization": f"Bearer {github_pat}",
                },
            }
        }
    )
async def get_mcp_tools():
    client = get_mcp_client()
    all_tools = await client.get_tools()

    # Print name and description for each tool
    print(f"Total count of tools {len(all_tools)}")
    print("Available tools from all servers:")
    for t in all_tools:
        print(f"- **{t.name}**: {t.description}")

    filtered = [t for t in all_tools if t.name in GITHUB_TOOLS_ALLOWLIST]

    print("\nTools actually loaded:")
    for t in filtered:
        print(f"- **{t.name}**: {t.description}")

    return filtered

if __name__ == "__main__":
 asyncio.run(get_mcp_tools())