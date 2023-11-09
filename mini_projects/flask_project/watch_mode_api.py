import os
from dotenv import load_dotenv
import requests

# Load environment variables from the .env file
load_dotenv()


class WatchModeApi:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")

    def get_stream_sources(self, title_id: str):
        url = f"https://api.watchmode.com/v1/title/{title_id}/details/"

        params = {
            "apiKey": self.api_key,
            "append_to_response": "sources",
        }
        response = requests.get(url, params=params, timeout=5)
        return response.json()
