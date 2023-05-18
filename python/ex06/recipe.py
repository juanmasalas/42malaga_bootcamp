cookbook = {
    'Sandwich': {
    "ingredients": ["ham","bread","cheese","tomatoes"],
    "meal": "lunch",
    "prep_time": 10,
    },
    'Cake': {
    "ingredients": ["flour","sugar","eggs"],
    "meal": "dessert",
    "prep_time": 60,
    },
    'Salad': {
    "ingredients": ["avocado","arugula","tomatoes","spinach"],
    "meal": "lunch",
    "prep_time": 15,
    },
    }
def show_cookbook():
    print()
    for a in cookbook:
        print(a)
    print()
    menu_return()
def details_recipe():
    r = input("Please, imput a name of recipe for view details ")
    if r in cookbook:
        print(f"\nRecipe for {r}:")
        print(f"\tIngedients list:  {cookbook[r]['ingredients']}")
        print(f"\tTo be eaten for {cookbook[r]['meal']}.")
        print(f"\tTakes {cookbook[r]['prep_time']} minutes of cooking.\n")
    else:
        print("\nError: you should enter a correct recipe.\n")
    menu_return()
def delete_recipe():
    try:
        r = input("\nPlease, imput a name of recipe for remove: ")
        cookbook.pop(r)
        print(f"\nThe recipe {r} has has been deleted.\n")
    except KeyError:
        print("KeyError: You must enter a saved recipe.")
    menu_return()
def add_recipe():
    print()
    r1 = input("Enter a recipe name: ")
    ingredients=[]
    r2 = input("Enter a ingredient: ")
    while(len(r2) != 0):
        ingredients.append(r2)
        r2 =input("Enter a ingredient: ")
    r3 = input("Enter a meal type: ")
    r4 = input("Enter a preparation time: ")
    r = {
    r1: {
    "ingredients": ingredients,
    "meal": r3,
    "prep_time": r4
    }
    }
    cookbook.update(r)
    menu_return()
def quit():
    print(f"\nCookbook closed. Goodbye\n")
    exit()
def menu():
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")
    respuesta1 = input("Please select an option:")
    if not int(respuesta1.isnumeric()) or int(respuesta1) > 5 or int(respuesta1) == 0:
        print(f"\nError: You should enter a number of index.\n")
        menu_return()
    else:
        respuesta1 = int(respuesta1)
        switcher = {
            1: add_recipe,
            2: delete_recipe,
            3: details_recipe,
            4: show_cookbook,
            5: quit
        }
        func = switcher.get(respuesta1, "Error: Incorrect answer")
        func()
def menu_return():
    print("List of available option:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit")
    respuesta1 = input("Please select an option:")
    if not int(respuesta1.isnumeric()) or int(respuesta1) > 5 or int(respuesta1) == 0:
        print(f"\nError: You should enter a number of index.\n")
        menu_return()
    else:
        respuesta1 = int(respuesta1)
        switcher = {
            1: add_recipe,
            2: delete_recipe,
            3: details_recipe,
            4: show_cookbook,
            5: quit
        }
        func = switcher.get(respuesta1, "Error: Incorrect answer")
        func()
menu()