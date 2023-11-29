import json

from api_request import get_questions_of_specific_category


def main():
    test = get_questions_of_specific_category("music")
    print(test)
    with open("test.json", "w") as f:
        json.dump(test, f, indent=4)
        
main()