import json
import requests


def make_request(url: str) -> dict:
    response = requests.get(url, timeout=20)
    if not response:
        raise ValueError("Error fetching request.")
    return json.loads(response.text)


def get_questions_for_specific_category_by_difficulty(category: str, difficulty: str) -> dict:
    if category == "":
        category = "general_knowledge"
    return make_request(f"https://the-trivia-api.com/v2/questions?categories={category}&type=text-choice&difficulties={difficulty}")


def get_questions_for_specific_category(category: str) -> dict:
    if category == "":
        category = "general_knowledge"
    return make_request(f"https://the-trivia-api.com/v2/questions?categories={category}&type=text-choice")


def get_all_category_names() -> list:
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





