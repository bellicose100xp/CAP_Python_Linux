from if_logic_data import characters, characteristics, characteristicMap
import random
from if_logic_colors import Color


def displayBanner():
    repeat = 40
    title = f"  Dunder Mifflin Paper Company  "

    print("\n" + Color.YELLOW + "*" * repeat)
    print(f"{title:*^{repeat}}")
    print("*" * repeat + Color.RESET)


def main():
    # Banner
    displayBanner()

    # Prompt user to select characteristic (4 at a time)
    selectedCharacteristics: list[str] = getUserSelections()

    # Calculate each character's rank based on selected characteristics
    ranks = calculateRank(selectedCharacteristics)

    # Find the character with the highest rank, select one randomly if multiple characters matched
    matchedCharacter = findMatchedCharacter(ranks)

    # Display results
    print(
        f"\n{Color.BLUE}Your selected characteristics: {selectedCharacteristics} {Color.RESET}"
    )
    print(
        f"{Color.YELLOW}The Office character you matched with is: {Color.GREEN}{matchedCharacter}{Color.RESET}"
    )


def getUserSelections() -> list[str]:
    selectedCharacteristics: list[str] = []
    seq: list[str] = ["1st", "2nd", "3rd", "4th"]

    i: int = 0
    while i < len(characteristics):
        print(
            f"\nChoose the {Color.CYAN}{seq[i//4]}{Color.RESET} characteristic you most align with,"
        )

        # Display Next 4 Characteristics Menu
        for j in range(i, i + 4):
            displayIdx = j % 4
            print(f"  {displayIdx + 1}. {characteristics[j]}")

        # Proceed only if valid selection
        validSelection: bool = False
        while not validSelection:
            selection: str = input("Selection: ")

            # Handle Invalid Selection
            if not selection.isnumeric() or int(selection) < 1 or int(selection) > 4:
                print(
                    f"{Color.RED}Invalid selection. Selection must be between 1 and 4. Please try again!{Color.RESET}\n"
                )
                continue

            selectedIdx = int(selection) - 1 + i
            selectedCharacteristics.append(characteristics[selectedIdx])
            validSelection = True

        # Increment by 4 to select 4 characteristics
        i += 4
    return selectedCharacteristics


def calculateRank(selectedCharacteristics: list[str]) -> list[int]:
    ranks: list[int] = [0] * len(characters)
    for i, character in enumerate(characters):
        for characteristic in selectedCharacteristics:
            ranks[i] += characteristicMap[character].get(characteristic, 0)
    return ranks


def findMatchedCharacter(ranks: list[int]) -> str:
    maxRank: int = max(ranks)
    matchedCharacters: list[str] = []
    for i, rank in enumerate(ranks):
        if rank == maxRank:
            matchedCharacters.append(characters[i])

    # choose one character randomly
    matchedCharacter = random.choice(matchedCharacters)
    return matchedCharacter


if __name__ == "__main__":
    main()
