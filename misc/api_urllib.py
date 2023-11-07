from pprint import pprint
from urllib.request import Request, urlopen
import json


def main():
    req = Request(
        url="https://anapioficeandfire.com/api/books/1",
        headers={"User-Agent": "Mozilla/5.0"},
    )

    with urlopen(req) as res:
        data = res.read()
        decoded = data.decode("utf-8")
        json_data = json.loads(decoded)
        pprint(json_data)


if __name__ == "__main__":
    main()
