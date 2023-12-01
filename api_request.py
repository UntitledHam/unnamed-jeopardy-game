import json
import requests


def make_request(url: str) -> dict:
    response = requests.get(url, timeout=5)
    if not response:
        raise ValueError("Error fetching request.")
    return json.loads(response.text)


def get_questions_of_specific_category(category: str) -> dict:
    if category == "":
        category = "general_knowledge"
    return make_request(f"https://the-trivia-api.com/v2/questions?categories={category}&type=text-choice")


def get_all_categories() -> list:
    categories = []
    request_json = make_request(f"https://the-trivia-api.com/v2/categories")
    for category, subcategory in request_json.items():
        categories.append(subcategory)
    return categories
