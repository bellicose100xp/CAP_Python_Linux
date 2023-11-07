#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

API = "https://www.anapioficeandfire.com/api"


def main():
    ## Send HTTPS GET to the API of ICE and Fire
    res = requests.get(API)

    ## Decode the response
    available_apis = res.json()

    characters_api = available_apis["characters"]
    books_api = available_apis["books"]
    houses_api = available_apis["houses"]

    books_res = requests.get(books_api)
    books_res_json = books_res.json()

    # characters_res = requests.get(characters_api)
    # characters_res_json = characters_res.json()

    # i: int = 1
    # for character in characters_res_json:
    #     name = f" {character['name']}" if character["name"] else ""
    #     aliases = f" {','.join(character['aliases'])}" if character["aliases"] else ""
    #     print(f"{i}.{name}{aliases}")
    #     i += 1

    char_idx = input("Enter a number between 1 and 1000\n> ")
    char_api = f"{characters_api}/{char_idx}"
    char_res = requests.get(char_api)
    char_res_json = char_res.json()

    print(f"\nName: {char_res_json['name']}")
    print(f"\nAliases: {', '.join(char_res_json['aliases'])}")

    print("\nBooks: ")
    for book in char_res_json["povBooks"]:
        book_idx = book.split("/")[-1]
        book_name = books_res_json[int(book_idx) - 1]["name"]
        print(f"* {book_name}")

    print("\nHouses: ")
    for house in char_res_json["allegiances"]:
        house_idx = house.split("/")[-1]
        house_req = f"{houses_api}/{house_idx}"
        house_res = requests.get(house_req)
        house_res_json = house_res.json()
        house_name = house_res_json["name"]
        print(f"* {house_name}")


if __name__ == "__main__":
    main()
