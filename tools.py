import os
import requests
from dotenv import load_dotenv
from crewai.tools import tool

load_dotenv()

@tool("Search the web for information")
def serper_search_tool(query: str):
    """
    Searches the web using Serper API and returns top 5 results
    including title, link, and snippet.
    """
    url = "https://google.serper.dev/search"

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    payload = {"q": query}

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            return f"Error: {response.status_code}"

        data = response.json()
        results = data.get("organic", [])

        cleaned_results = [
            {
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet", "")
            }
            for item in results[:5]
            if item.get("title") and item.get("link")
        ]

        return cleaned_results

    except Exception as e:
        return f"Error: {str(e)}"