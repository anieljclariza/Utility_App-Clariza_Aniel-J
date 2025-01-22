import random

def rng():
    random_number_generator = random.randint(1,10)
    return random_number_generator

foods = {

        "F1": (rng(), rng(), "Pizza Hat pizza 🍕"),
        "F2": (rng(), rng(), "Burger Emperor burger 🍔"),
        "F3": (rng(), rng(), "McRonald's fries 🍟"),
        "F4" :(rng(), rng(), "Quasant's croissant 🥐"),
        "F5": (rng(), rng(), "Tuesdays' taco 🌮"),
        "F6": (rng(), rng(), "New York Foods Society cheesedog 🌭"),
        "F7": (rng(), rng(), "Los Pablos burrito 🌯")

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
    print("Quality of the item is directly proportial to its price. The higher the price of the item the higher the quality.")

    print()
    start_program()


def start_program():
    print("Would you like to use the Vending Machine Program and see the stock?")
    prompt = input("[👍Yes] or [👎No = Quit]: ")
     
    if prompt.upper() == "YES":
        print()
        display_items()
    elif prompt.upper() == "NO":
        print("Understood! Thank you for checking out my program!")
    else:
        print()
        print(f"I'm sorry but I didn't get that. Please try again.")
        start_program()



def display_items():
    selection = input("Please select a category to see [Foods = F][Drinks = D][Random Items = R] [QUIT PROGRAM = Q]: ")
    
    if selection.upper() == "FOODS" or selection.upper() == "F":
        selection = foods
    elif selection.upper() == "DRINKS" or selection.upper() == "D":
        selection = drinks
    elif selection.upper() == "RANDOM ITEMS" or selection.upper() == "R":
        selection = random_items
    elif selection.upper() == "QUIT PROGRAM" or selection.upper() == "Q":
        print("Understood! Thank you for checking out my program!")
    else:
        print(f"I'm sorry  but I didn't get that. Please try again.")
        print()
        display_items()
    print()

    for code, (price, stock, item) in selection.items():
        print(f"[{code}]{item}: [price: {price} AED] [stock: {stock}]")
        
    print()

    ask = input("Would you like to [BUY] now or [SEE] the stock again?: ")
    if ask.upper() == "BUY":
        code = input("Input the code of the item you wish to buy: ")
        code = code.upper()
        code = selection
        print(f"[{code}]{code.get(item)} [{code.get(price)} AED] [{code.get(stock)} pieces]")
        ask = int(input("How many would you like to buy?: "))
        total = ask * price
        print(f"Total is {total} AED for {ask} {item}s.")
    elif ask.upper() == "SEE":
        display_items()


welcome()