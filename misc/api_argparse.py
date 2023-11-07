#!/usr/bin/python3

## for accepting arguments from the cmd line
import argparse

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

api_url = "http://pokeapi.co/api/v2/item/"


def main(args: argparse.Namespace):
    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{api_url}?limit=1000")
    items = items.json()

    # create a list to store items with the word searched on
    matched_words: list[str] = []

    # Loop through data, and print pokemon names
    # item.get("results") will return the list
    # mapped to the key "results"
    for item in items.get("results"):
        # check to see if the current item's VALUE mapped to item["name"]
        # contains the search word
        if args.searchWord in item.get("name"):
            # if TRUE, add that item to the end of list matchedWords
            matched_words.append(item.get("name"))

    finished_list = matched_words.copy()
    ## map our matchedWord list to a dict with a title
    word_matches: dict[str, list[str]] = {}
    word_matches["matched"] = finished_list

    ## list all words containing matched word
    print(
        f"There are {len(finished_list)} words that contain the word '{args.searchWord}' in the Pokemon Item API!"
    )
    print(f"List of Pokemon items containing '{args.searchWord}': ")
    print(word_matches)

    ## export to excel with pandas
    # make a dataframe from our data
    items_df = pandas.DataFrame(word_matches)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    items_df.to_excel("pokemon_items.xlsx", index=False)  # type: ignore

    print("Gotta catch 'em all!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pass in a word to search\
    the Pokemon item API"
    )
    parser.add_argument(
        "--searchWord",
        metavar="<Search_Word>",
        type=str,
        default="ball",
        help="Pass in any word. Default is 'ball'",
    )
    args = parser.parse_args()
    main(args)
