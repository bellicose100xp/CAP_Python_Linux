import random
from if_logic_data import characters, characteristics, characteristic_map
from if_logic_colors import Color


def display_banner():
    repeat = 40
    title = "  Dunder Mifflin Paper Company  "

    print("\n" + Color.YELLOW + "*" * repeat)
    print(f"{title:*^{repeat}}")
    print("*" * repeat + Color.RESET)


def main():
    # Banner
    display_banner()

    # Prompt user to select characteristic (4 at a time)
    selected_characteristics: list[str] = get_user_selections()

    # Calculate each character's rank based on selected characteristics
    ranks = calculate_rank(selected_characteristics)

    # Find the character with the highest rank, select one randomly if multiple characters matched
    matched_character = find_matched_character(ranks)

    # Display results
    print(
        f"\n{Color.BLUE}Your selected characteristics: {selected_characteristics} {Color.RESET}"
    )
    print(
        f"{Color.YELLOW}The Office character you matched with is: {Color.GREEN}{matched_character}{Color.RESET}"
    )


def get_user_selections() -> list[str]:
    selected_characteristics: list[str] = []
    seq: list[str] = ["1st", "2nd", "3rd", "4th"]

    i: int = 0
    while i < len(characteristics):
        print(
            f"\nChoose the {Color.CYAN}{seq[i//4]}{Color.RESET} characteristic you most align with,"
        )

        # Display Next 4 Characteristics Menu
        for j in range(i, i + 4):
            display_idx = j % 4
            print(f"  {display_idx + 1}. {characteristics[j]}")

        # Proceed only if valid selection
        valid_selection: bool = False
        while not valid_selection:
            selection: str = input("Selection: ")

            # Handle Invalid Selection
            if not selection.isnumeric() or int(selection) < 1 or int(selection) > 4:
                print(
                    f"{Color.RED}Invalid selection. Selection must be between 1 and 4. Please try again!{Color.RESET}\n"
                )
                continue

            selected_idx = int(selection) - 1 + i
            selected_characteristics.append(characteristics[selected_idx])
            valid_selection = True

        # Increment by 4 to select 4 characteristics
        i += 4
    return selected_characteristics


def calculate_rank(selected_characteristics: list[str]) -> list[int]:
    ranks: list[int] = [0] * len(characters)
    for i, character in enumerate(characters):
        for characteristic in selected_characteristics:
            ranks[i] += characteristic_map[character].get(characteristic, 0)
    return ranks


def find_matched_character(ranks: list[int]) -> str:
    max_rank: int = max(ranks)
    matched_characters: list[str] = []
    for i, rank in enumerate(ranks):
        if rank == max_rank:
            matched_characters.append(characters[i])

    # choose one character randomly
    matched_character = random.choice(matched_characters)
    return matched_character


if __name__ == "__main__":
    main()
