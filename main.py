def welcome():
    print("Welcome to Aniel's Plain Vending Machine. 🔥🔥🔥")
    start_prompt = input("Would you like to use this Vending Machine? 'Y' or 'N': ")
    print()
    if start_prompt.upper() == 'Y':
        display_items()
    else:
        print("Goodbye!")

def display_items():
    items = {
        "drinks": ["Bottled Drinking Water", "Bottled Juice", "Bottled Cold Coffee"],
        "food": ["Biscuits", "Shawrma", "Pizza"]
    }

    for category, content in items.items():
        print(f"{category} contain {content}" )

welcome()