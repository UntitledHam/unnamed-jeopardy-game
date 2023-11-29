import json

from api_request import make_request


def main():
    test = make_request("https://the-trivia-api.com/v2/questions/")
    print(test)
    with open("test.json", "w") as f:
        json.dump(test, f, indent=4)
main()