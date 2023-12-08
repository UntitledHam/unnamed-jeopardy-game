import json
import requests


def make_request(url: str) -> dict:
    """
    Makes a request to the api using url
    :param url: url to make a request
    :raise ValueError: if there is no response from the request
    :return: Response from API
    """
    response = requests.get(url, timeout=20)
    if not response:
        raise ValueError("Error fetching request.")
    return json.loads(response.text)


def get_questions_for_specific_category_by_difficulty(category: str, difficulty: str) -> dict:
    """
    Returns json from a url that makes a call to get questions from a specific category and difficulty
    :param category: category to get from
    :param difficulty: difficulty to get from
    :return: result of the api call
    """
    if category == "":
        category = "general_knowledge"
    return make_request(f"https://the-trivia-api.com/v2/questions?categories={category}&type=text-choice&difficulties={difficulty}")


def get_questions_for_specific_category(category: str) -> dict:
    """
    Returns json from a url that makes a call to get questions from a specific category
    :param category: category to get from
    :return: result of the api call
    """
    if category == "":
        category = "general_knowledge"
    return make_request(f"https://the-trivia-api.com/v2/questions?categories={category}&type=text-choice")


def get_all_category_names() -> list:
    """
    Makes a call to retrieve all categories from the api
    :return: List of string categories
    """
    categories = []
    request_json = make_request(f"https://the-trivia-api.com/v2/categories")
    for category, subcategory in request_json.items():
        if category == "Film & TV" or category == "Arts & Literature":
            categories.append(subcategory[2])
            continue
        else:
            categories.append(subcategory[0])
    return categories


def generate_category_dropdowns():
    """
    Generates dropdowns for categories
    :return: html of dropdowns of categories
    """
    all_category_names = get_all_category_names()
    output_html = ""
    for i in range(5):
        output_html += f"""<br><select name="option-{i}">
        <option value="random" selected>Random</option>
        """
        for category_name in all_category_names:
            modified_category_name = category_name.replace("_", " ").title()
            output_html += f"""
            <option value="{category_name}">{modified_category_name}</option><br>"""
        output_html += """</select>"""
    return output_html





