import html
import random
import requests

URL = "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy"
BASE_URL = "https://opentdb.com/api.php?"

CATEGORIES = {
    9: "General Knowledge",
    10: "Entertainment- Books",
    11: "Entertainment- Film",
    12: "Entertainment- Music",
    13: "Entertainment- Musicals & Theater",
    14: "Entertainment- Television",
    15: "Entertainment- Video Games",
    16: "Entertainment- Board Games",
    17: "Science- Nature",
    18: "Science- Computers",
    19: "Science- Mathematics",
    20: "Mythology",
    21: "Sports",
    22: "Geography",
    23: "History",
    24: "Politics",
    25: "Art",
    26: "Celebrities",
    27: "Animals",
    28: "Vehicles",
    29: "Entertainment- Comics",
    30: "Science- Gadgets",
    31: "Entertainment- - Japanese Anime & Manga",
    32: "Entertainment- - Cartoon Animations",
}
QUESTION_TYPES = ["any", "multiple", "boolean"]
DIFFICULTIES = ["easy", "medium", "hard"]


def main():
    print("")

    # Select Category
    for category_id, category in CATEGORIES.items():
        print(f"{category_id}. {category}")

    selected_category = input("\nPlease select a category:\n> ")

    # Select Types of Question
    print("")
    for category_id, question in enumerate(QUESTION_TYPES):
        print(f"{category_id+1}. {question}")

    selected_type = input("\nPlease select a question type:\n> ")
    api_type = QUESTION_TYPES[int(selected_type) - 1]

    # Select Question Difficulty Level
    print("")
    for category_id, difficulty in enumerate(DIFFICULTIES):
        print(f"{category_id+1}. {difficulty}")

    selected_difficulty = input("\nPlease select a difficulty:\n> ")
    api_difficulty = DIFFICULTIES[int(selected_difficulty) - 1]

    # Select the number of questioins
    print("")
    selected_quantity = input("\nHow many questions do you want:\n> ")
    api_quantity = int(selected_quantity)

    # Add or remove api_type if "any" option was selected
    final_api_type = ""
    if api_type == "any":
        final_api_type = ""
    else:
        final_api_type = f"&type={api_type}"

    # Generate base URL
    url = (
        BASE_URL
        + f"amount={api_quantity}&category={selected_category}&difficulty={api_difficulty}{final_api_type}"
    )

    res = requests.get(url, timeout=5)
    data = res.json()

    questions = data["results"]
    total_questions: int = len(questions)

    # If no questions received, exit the program
    if not total_questions:
        print(
            "\n Sorry! Nothing found for selected combination. Please try again with different combinatinon or lower number of questions."
        )
        return

    # keep track of correctly answerd questions
    answered_correctly: int = 0
    question_num: int = 1

    for question in questions:
        correct_answer = html.unescape(question["correct_answer"].strip())

        options: list[str] = [
            html.unescape(ans).strip() for ans in question["incorrect_answers"]
        ]

        options.append(correct_answer)
        random.shuffle(options) # shuffle the answers

        # List question
        print(f"\nQuestion {question_num}: {html.unescape(question['question'])}")
        for i, option in enumerate(options):
            print(f"  {i+1}. {option}")

        valid_selection = False
        selected_num: int = -1
        print("\nPlease select an option:")

        # Get user input (validated)
        while not valid_selection:
            selected_option = input("> ")

            if not selected_option.isnumeric() or not 0 < int(selected_option) <= len(
                options
            ):
                print("Invalid selection. Please try again.")
                continue

            selected_num = int(selected_option) - 1
            valid_selection = True

        # Check if answer is correct
        if options[selected_num] == correct_answer:
            print("You are correct!")
            answered_correctly += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")

        question_num += 1

    # Display final result
    print(f"\n*** You answered {answered_correctly} of {total_questions} correctly ***")


if __name__ == "__main__":
    main()
