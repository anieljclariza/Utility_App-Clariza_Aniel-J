# Imported random module to use its function, randint()
import random

#Defined rng() function to generate random integers for stock and price
def rng():
    random_number_generator = random.randint(1,10)
    return random_number_generator

# 3 dictionaries containing the three categories in the vending machine
# Key = Code, Value 1 = Price, Value 2 = Stock, Value 3 = Item
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
       
        "D1": (rng(), rng(), "Dark & White coffee ☕️"),
        "D2": (rng(), rng(), "Japan Foods and Drinks Company tea 🍵"),
        "D3": (rng(), rng(), "Feathermill Mixed Fruit Juice 🧃"),
        "D4" :(rng(), rng(), "Earth & Nature bottled drinking water 🥤"),
        "D5": (rng(), rng(), "Boba Fett boba tea 🧋"),
        "D6": (rng(), rng(), "Nature's Finest bottled full cream milk 🥛")

        }

random_items = {
       
        "R1": (rng(), rng(), "I LOVE THIS EMOJI 😍"),
        "R2": (rng(), rng(), "A MECHANICAL ARM?! 🦾"),
        "R3": (rng(), rng(), "NARUTO SHIPPUDEN! 🥷"),
        "R4" :(rng(), rng(), "WHERE DID YOU GET A DRAGON?! 🐉"),
        "R5": (rng(), rng(), "THE WHOLE PLANET?! 🌏"),
        "R6": (rng(), rng(), "NOW IT'S SATURN LIKE CMON MAN! 🪐"),
        "R7": (rng(), rng(), "Peace Sign ☮️")

        }


#Defined welcome() function as starting screen to the vending machine program
def welcome():

    print("Welcome to Aniel's Randomized Vending Machine Program ❤️  🔥 🌭!")

    #Used while True: loop to ask if user wants to use vending machine program or quit, and keeps looping if responses are invalid
    while True: 
        
        print("Would you like to use the Vending Machine Program and see the stock?")
        prompt = input("[👍Yes] or [👎No = Quit]: ")
     
        if prompt.upper() in ("Y", "YES"):
            print()
            main_program()
        elif prompt.upper() in ("N", "NO"):
            print("Understood! Thank you for checking out my program!")
            break
        else:
            print()
            print(f"I'm sorry but I didn't get that. Please try again.")

    print()

# Defined main program where it displays stock and does the transaction as well
def main_program():
    while True:

        prompt = input("Please enter the category you wish to see [F = FOODS] [D = DRINKS] [R = RANDOM ITEMS]: ")
        if prompt.upper() in ["F", "FOODS"]:
            selection = foods
            break
        elif prompt.upper() in ["D", "DRINKS"]:
            selection = drinks
            break
        elif prompt.upper() in ["R", "RANDOM ITEMS"]:
            selection = random_items
            break
        else:
            print()
            print("I'm sorry but I didn't get that. Please try again.")
    
    print()

    for code, (price, stock, item) in selection.items():
        print(f"[{code}]{item}: [price: {price} AED][stock: {stock}]")

    print()
    
    while True:
        prompt = input("Please enter the [CODE] of the item that you wish to buy: ")
        print()

        item_code = prompt.upper()
        
        if item_code in selection:
            price, stock, item = selection[item_code]
            print(f"You have selected [{item_code}]{item}: [price: {price} AED] [stock: {stock}].")
            while True:
                qty = int(input("How many would you like to buy?: "))
                total = qty * price
                if qty <= stock and qty > 0:
                    
                    print(f"Total is {total} AED.")
                    money = int(input("Please enter cash to complete the purchase: "))
                    print()
                    if money >= total:
                        change = money - total
                        print("Thenk you very much for using my Vending Machine Program!")
                        print(f"You have bought a {qty} piece {item} totalling {total} AED.")
                        print(f"Change is {change}.")
                        print()
                        break
                    else:
                        print("Invalid response or insufficient money entered. Please try again.")
                else: 
                    print("I'm sorry but the amount you want to but is more than the stock or your response was invalid. Please try again.")
        
        else:        
            print()
            print("I'm sorry but I didn't get that. Please try again.")
        break

welcome()