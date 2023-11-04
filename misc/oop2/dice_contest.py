#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *


def main():
    """called at runtime"""

    # the player known as the swapper
    swapper = Cheat_Swapper()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()
    # heavily loaaded dice
    heavily_loaded_dice = CheatHeavilyLoaded()

    # track scores for both players
    swapper_score = 0
    loaded_dice_score = 0
    heavily_loaded_dice_score = 0

    # how many games we want to run
    number_of_games = 100000
    all_matched = 0
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        heavily_loaded_dice.roll()

        swapper.cheat()
        loaded_dice.cheat()
        heavily_loaded_dice.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        scores: list[int] = [
            sum(swapper.get_dice()),
            sum(loaded_dice.get_dice()),
            sum(heavily_loaded_dice.get_dice()),
        ]

        max_score: int = max(scores)

        def score_generator():
            for score in scores:
                yield score == max_score

        gen = score_generator()

        if all(match for match in gen):
            all_matched += 1
        else:
            for i, score in enumerate(scores):
                if score == max_score:
                    match i:
                        case 0:
                            swapper_score += 1
                        case 1:
                            loaded_dice_score += 1
                        case 2:
                            heavily_loaded_dice_score += 1

        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"All Matched: {all_matched}")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")
    print(f"Heavily Loaded dice won: {heavily_loaded_dice_score}")


if __name__ == "__main__":
    main()
