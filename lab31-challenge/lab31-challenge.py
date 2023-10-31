import random


def main():
    wordbank: list[int | str] = ["indentation", "spaces"]
    tlgstudents: list[str] = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James',
                              'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    wordbank.append(4)
    print("")
    print(wordbank)

    selected = False
    while not (selected):
        num_str = input( f"\n\033[1;34mEnter a number between 1 and {len(tlgstudents)}:\033[0m")

        if num_str.isnumeric() and 1 <= int(num_str) <= len(tlgstudents):
            selected = True
        else:
            print(f"Number must be between 0 and {len(tlgstudents)}")

    student_name = tlgstudents[int(num_str)-1]

    print(
        f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.")

    random_student = random.choice(tlgstudents)
    # Alternative using random.randint(start, end)
    # random_idx = random.randint(0, len(tlgstudents) - 1)
    # random_student = tlgstudents[random_idx]
    print("\n\033[1;30m--- Random Student Selection ---\033[0m")
    print(
        f"{random_student} always uses {wordbank[-1]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
