import json

import requests


def make_request(url: str):
    response = requests.get(url, timeout=5)
    if not response:
        raise ValueError("Error fetching request.")
    return json.loads(response.text)

