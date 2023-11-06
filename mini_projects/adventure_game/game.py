#!/usr/bin/python3
"""Text Based Adventure Game"""
from typing import TypeAlias, Literal
from room import Room, kitchen, dining_room, basement, garden
from player import Player, PlayerState
from styling import Color, Style
from utils import clear_terminal
from directions import Direction, get_direction_from_str


# Type aliases
Commands: TypeAlias = list[Literal["go"] | Literal["collect"] | Literal["get"]]
Collectibles: TypeAlias = list[
    Literal["key"] | Literal["watch"] | Literal["potion"] | Literal["broomstick"]
]

VALID_COMMANDS: Commands = ["go", "collect", "get"]
COLLECTIBLES: Collectibles = ["key", "watch", "potion", "broomstick"]
STARTER_ROOM: Room = dining_room


def main():
    # Set initial room for player
    current_room: Room = STARTER_ROOM

    # Initialize a sample player. Name will be added in the next steps
    player = Player(name="", items=[], state=PlayerState.ALIVE, weapons=[], steps=0)

    ## Get player name
    print(f"{Color.YELLOW}Welcome to the adventure game!{Color.RESET}")
    get_player_name(player)

    # breaking this while loop means the game is over
    game_loop(current_room, player)


# Shows various stats about the player
def show_player_status(player: Player):
    width: int = 40
    print("-" * width)

    print(f"Name: {player.name}")
    print(f"Steps: {player.steps}")

    # Show items only if player has them
    if player.items:
        print(f"Items: {player.items}")

    # Show weapons only if player has them
    if player.weapons:
        print(f"Weapons: {player.weapons}")

    print("-" * width)


def get_player_name(player: Player):
    print("What is your name?")
    valid_name = False
    while not valid_name:
        player_name = input("> ")

        # Check if player name is empty
        if player_name:
            player.name = player_name
            valid_name = True


# Main game loop, that runs until player wins or dies
def game_loop(current_room: Room, player: Player):
    while True:
        # Clear terminal on each run (both unix and windows terminal are accounted for)
        clear_terminal()

        # show player stats at the top of the page
        show_player_status(player)

        # Print room info including the next steps player needs to take
        print(current_room.get_description())

        # Process user input and get next room
        current_room = process_user_input(current_room, player)

        # Check is in room with contains dangerous elements that can kill player
        # Check if player can survive with the weapon he currently has
        match current_room.name:
            case kitchen.name:
                # Check if there's an danger in Kitchen
                if kitchen.danger:
                    # Check if player has the weapon to kill the monster
                    if "flamethrower" in player.weapons:
                        print(
                            f"{Color.GREEN}Monster lunged at you but you defeated the monster with your flamethrower!{Color.RESET}"
                        )

                        player.weapons.remove("flamethrower")
                        kitchen.danger = ""
                        input("\nPress any key to continue")
                    else:
                        print(
                            f"{Color.RED}Monster lunged at you and killed you!{Color.RESET}"
                        )
                        player.state = PlayerState.DEAD
                        break

            case basement.name:
                # Check if there's a danger in basement
                if basement.danger:
                    # Check if player has the weapon to kill the witch
                    if "spell" in player.weapons:
                        print(
                            f"{Color.GREEN}Witch was about to grab you and put you in hot cauldron, but you cast your spell to kill the witch!{Color.RESET}"
                        )

                        player.weapons.remove("spell")
                        basement.danger = ""
                        input("\nPress any key to continue")
                    else:
                        print(
                            f"{Color.RED}Witch grabbed you, put you in hot cauldron, and killed you!{Color.RESET}"
                        )
                        player.state = PlayerState.DEAD
                        break

            case _:
                pass

        # Check if player won
        if current_room == garden:
            missing_items: list[str] = [
                item for item in COLLECTIBLES if item not in player.items
            ]

            if not missing_items:
                print(
                    f"{Color.GREEN}{Style.BRIGHT}Congratulations! You won! You have collected all the items, and made it to the garden room safely{Color.RESET}"
                )
                break
            else:
                print(
                    f"{Color.ORANGE}You have not collected all the items yet!. Missing Items: {missing_items}{Color.RESET}"
                )
                input("\nPress any key to continue...")

        # Keep track of player steps, this could be used in future to make the game more challenging
        # by limiting the amount of steps a player can take.
        player.steps += 1


# Gets and processes user input for different suffixes ('go', 'get', 'collect')
def process_user_input(current_room: Room, player: Player) -> Room:
    valid_input = False

    # Loop continues until the valid user input is provided
    while not valid_input:
        command = input("> ")

        # Check if the command is empty
        if not command:
            continue

        parts = command.lower().strip().split(" ", 1)
        prefix = parts[0]

        # Check if the command prefix is valid
        if prefix not in VALID_COMMANDS:
            print(f"{Color.RED}Uh oh! That command is not quite right!{Color.RESET}")
            continue

        # Check if 2nd part of the command was provided
        if len(parts) == 1:
            print(f"{Color.RED}Darn! That command is incomplete  {Color.RESET}")
            continue

        # Process input according to selected "prefix"
        match prefix:
            # Direction Case
            case "go":
                # Get corresponding direction Enum
                direction: Direction | None = get_direction_from_str(parts[1])

                if not direction:
                    print(f"{Color.RED}Oops! That's not a direction!{Color.RESET}")
                    continue

                if direction not in current_room.directions:
                    print(
                        f"{Color.RED}Oops! That's not a direction we can go from this room!{Color.RESET}"
                    )
                    continue

                # Get the next room in the 'direction' that user wants to go
                current_room = current_room.go_to_adjacent_room(direction)
                valid_input = True
                break

            # Collectible Items Case
            case "collect":
                input_item: str = parts[1]

                if not current_room.items or not input_item in current_room.items:
                    print(f"{Color.RED}No such item to collect here!{Color.RESET}")
                    continue

                player.items.append(input_item)
                current_room.items.remove(input_item)
                print(f"{Color.GREEN}You collected {input_item}!{Color.RESET}")
                input("\nPress any key to continue...")
                valid_input = True
                break

            # Weapons Case
            case "get":
                input_weapon: str = parts[1]

                if not current_room.weapon or input_weapon != current_room.weapon:
                    print(f"{Color.RED}No such weapon to get here!{Color.RESET}")
                    continue

                player.weapons.append(input_weapon)
                current_room.weapon = ""
                valid_input = True
                print(f"{Color.GREEN}You got {input_weapon}!{Color.RESET}")
                input("\nPress any key to continue...")
                break

    return current_room


if __name__ == "__main__":
    main()
