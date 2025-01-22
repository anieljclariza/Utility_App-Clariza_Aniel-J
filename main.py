import random

def rng():
    random_number_generator = random.randint(1,10)
    return random_number_generator

foods = {

        "Pizza Hat pizza 🍕": (rng(), rng(), "F1"),
        "Burger Emperor burger 🍔": (rng(), rng(), "F2"),
        "McRonald's fries 🍟": (rng(), rng(), "F3"),
        "Quasant's croissant 🥐" :(rng(), rng(), "F4"),
        "Tuesdays' taco 🌮": (rng(), rng(), "F5"),
        "New York Foods Society cheesedog 🌭": (rng(), rng(), "F6"),
        "Los Pablos burrito 🌯": (rng(), rng(), "F7")

        }
    
drinks = {
       
        "Dark & White coffee ☕️": (rng(), rng(), "D1"),
        "Japan Foods and Drinks Company tea 🍵": (rng(), rng(), "D2"),
        "Feathermill Mixed Fruit Juice 🧃": (rng(), rng(), "D3"),
        "Earth & Nature bottled drinking water 🥤" :(rng(), rng(), "D4"),
        "Boba Fett boba tea 🧋": (rng(), rng(), "D5"),
        "Nature's Finest bottled full cream milk 🥛": (rng(), rng(), "D6")

        }

random_items = {
       
        "I LOVE THIS EMOJI 😍": (rng(), rng(), "R1"),
        "A MECHANICAL ARM?! 🦾": (rng(), rng(), "R2"),
        "NARUTO SHIPPUDEN! 🥷": (rng(), rng(), "R3"),
        "WHERE DID YOU GET A DRAGON?! 🐉" :(rng(), rng(), "R4"),
        "THE WHOLE PLANET?! 🌏": (rng(), rng(), "R5"),
        "NOW IT'S SATURN LIKE CMON MAN! 🪐": (rng(), rng(), "R6"),
        "Peace Sign ☮️": (rng(), rng(), "R7")

        }

def welcome():
    print("Welcome to Aniel's Randomized Vending Machine Program ❤️  🔥 🌭!")
    print()

    print("Would you like to provide your name  to improve your experience while using this program?")
    print("Please be rest assured that the personal information that you enter will be deleted every time this program is rerun.")
    personal_info = input("Provide name? [👍Yes] or [👎No]: ")
    print()

    if personal_info.upper() == "YES":
        name = input("What is your good name?: ")
        name = name.title()
        name = name.replace(" ", "")
        name = name.strip()
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
        display_items(name)
    elif prompt.upper() == "NO":
        print("Understood! Thank you for checking out my program!")
    else:
        print()
        print(f"I'm sorry {name} but I didn't get that. Please try again.")
        start_program(name)



def display_items(name):
    selection = input("Please select a category to see [Foods = F][Drinks = D][Random Items = R]: ")
    
    if selection.upper() == "FOODS" or selection.upper() == "F":
        selection = foods
    elif selection.upper() == "DRINKS" or selection.upper() == "D":
        selection = drinks
    elif selection.upper() == "RANDOM ITEMS" or selection.upper() == "R":
        selection = random_items
    else:
        print(f"I'm sorry {name} but I didn't get that. Please try again.")
        print()
        display_items(name)
    print()

    for item, (price, stock, code) in selection.items():
        print(f"[{code}]{item}: [price: {price} AED] [stock: {stock}]")
        
    print()
    selection_again(name)



def selection_again(name):
    selection_again = input("Would you like to [BUY] now, [SEE] the stock again, or do [ANOTHER] thing?: ")
    if selection_again.upper() == "BUY":
        selection_again = buy()
    elif selection_again.upper() == "SEE":
        selection_again = display_items(name)
    elif selection_again.upper() == "ANOTHER":
        print()
        menu = input("Okay! Where would you like to go? [1 = Welcome Screen] [2 = Start Screen] [3 = Quit]: ")
        if menu.upper() == "1" or menu.upper() == "WELCOME SCREEN":
            print()
            welcome()
        elif menu.upper() == "2" or menu.upper() == "START SCREEN":
            print()
            start_program()
        elif menu.upper() == "3" or menu.upper() == "QUIT":
            print("Understood! Good bye and thanks for checking out my program.")
        else:
            print(f"I'm sorry {name} but I didn't get that. Please try again.")
            print()
            selection_again()
    else:
        print(f"I'm sorry {name} but I didn't get that. Please try again.")
        print()
        selection_again() 

def buy():
    print("Buy")

welcome()