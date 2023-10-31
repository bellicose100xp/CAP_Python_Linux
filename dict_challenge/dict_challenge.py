from pprint import pprint

nintendo = {
    "full_name": "Shigeru Miyamoto",
    "age": 70,
    "employer": "Nintendo",
    "title": "Representative Director",
    "occupations": [
        "Game Designer", 
        "Game Producer", 
        "Game Director"
        ],
    "notable_games": [
        "Mario", 
        "Donkey Kong", 
        "The Legend Of Zelda", 
        "F-Zero", 
        "Star Fox", 
        "Pikmin", 
        "Nintendogs"
        ]
}

def main():
    exit_menu = False
    while not exit_menu: 
        print("\n\n-- Nintendo Dictionary Manager ---")
        print("1. Get Item Value")
        print("2. Add Item")
        print("3. Remove Item")            
        print("4. Exit")

        option = input("Select an option: ")
        
        match option:
            case "1":
                handle_get_item()

            case "2":
                handle_add_item()

            case "3":
                handle_delete_item()
            
            case "4":
                exit_menu = True
                print("\nExiting...")
                exit()

            case _:
                print("\nInvalid option, please try again.")

def select_dict_key() -> str:
    key = ""  # placeholder  
    keys = list(nintendo.keys())

    # Display menu
    for idx, key in enumerate(keys):
        print(f"{idx}. {key}")

    # Get user selection
    invalid_key_selected = False
    while not invalid_key_selected:
        key_idx = input("Select a key: ")

        if key_idx.isnumeric() and 0 <= int(key_idx) <= len(keys):
            invalid_key_selected = True
            key_idx = int(key_idx)
            key = keys[key_idx]
        else:
            print("Invalid key, please try again.")
    return key

def handle_get_item():
    print("\n\n-- Get Item Value ---") 
    key = select_dict_key()
    print(f"\n{key}: { nintendo.get(key) }")
    
def handle_add_item():
    print("\n\n-- Add Item ---")
    key = input("Enter key: ")
    value = input("Enter value: ")
    nintendo[key] = value
    print(f"\nAdded {key} to dictionary.\n")
    pprint(nintendo)

def handle_delete_item():
    print("\n\n-- Remove Item --")
    key = select_dict_key()
    del nintendo[key]
    print(f"\nRemoved {key} from dictionary.\n") 
    pprint(nintendo)

if __name__ == "__main__":
    main()    