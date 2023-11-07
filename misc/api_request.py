from pprint import pprint
import requests


def main():
    url = "https://anapioficeandfire.com/api/books/1"

    # 'data' is of type HTTP response
    res = requests.get(url)
    json_data = res.json()
    # pprint(json_data)
    pprint(json_data["authors"])


if __name__ == "__main__":
    main()
