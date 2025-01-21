def welcome():
    print("Welcome to Aniel's Vending Machine Program ❤️  🔥 🌭!")
    print()

    print("Would you like to provide your name  to improve your experience while using this program?")
    print("Please be rest assured that the personal information that you enter will be deleted every time this program is rerun.")
    personal_info = input("Provide name? [👍Yes] or [👎No]: ")
    print()
    
    if personal_info.upper() == "YES":
        name = input("What is your good name?: ")
        name = name.title()
        print(f"Hello, {name}! Thank you for checking out my program!")
    else:
        name = None
        print("Okay loser.")
        
    print()
    start_program(name)


def start_program(name):
    print("Would you like to use the Vending Machine Program and see the stock?")
    prompt = input("[👍Yes] or [👎No = Quit]: ")
     
    if prompt.upper() == "YES":
        print()
        display_items()
    elif prompt.upper() == "NO":
        print("Understood! Thank you for checking out my program!")
    else:
        print()
        print(f"I'm sorry, {name}, but I didn't get that. Please try again.")
        start_program(name)


def display_items():
    food = {
        "Pizza House Pizza 🍕": (5, 5, "F1"),
        "Burger Kingdom Burger 🍔": (5, 5, "F2"),
        "Fire Fries 🍟": (5, 5, "F3"),
        "Crusty's Croissant 🥐" :(5, 5, "F4"),
        "Totally Magnificent Taco 🌮": (5, 5, "F5"),
        "Cheesy Cheesedogs Cheesdog 🌭": (5, 5, "F6"),
        "Los Pablos Burrito 🌯": (5, 5, "F7")
        }
    
    for food, (price, stock, code) in food.items():
        print(f"{food} : [code: {code}]")
    
welcome()