import html
import random
import requests

URL = "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy"


def main():
    res = requests.get(URL, timeout=5)
    data = res.json()
    questions = data["results"]
    total_questions: int = len(questions)
    answered_correctly: int = 0

    question_num: int = 1

    for question in questions:
        correct_answer = html.unescape(question["correct_answer"].strip())

        options: list[str] = [
            html.unescape(ans).strip() for ans in question["incorrect_answers"]
        ]

        options.append(correct_answer)
        random.shuffle(options)

        print(f"\nQuestion {question_num}: {html.unescape(question['question'])}")
        for i, option in enumerate(options):
            print(f"  {i+1}. {option}")

        valid_selection = False
        selected_num: int = -1
        print("Please select an option:")

        while not valid_selection:
            selected_option = input("> ")

            if not selected_option.isnumeric() or not 0 < int(selected_option) <= len(
                options
            ):
                print("Invalid selection. Please try again.")
                continue

            selected_num = int(selected_option) - 1
            valid_selection = True

        if options[selected_num] == correct_answer:
            print("You are correct!")
            answered_correctly += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")

        question_num += 1

    print(f"\n*** You answered {answered_correctly} of {total_questions} correctly ***")


if __name__ == "__main__":
    main()
