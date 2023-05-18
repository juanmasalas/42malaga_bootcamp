import random
random_num = random.randint(1, 99)
intentos = 0
print("This is an interactive guessing game!")
print("You have to enter a number between 1 an 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print()
while True:
    print("What's your guess between 1 an 99?")
    intentos += 1
    guess_number = input()    
    try:
         guess_number = int(guess_number)
    except ValueError:
         guess_number = str(guess_number)
         if guess_number == "exit":
                print(f"\n>>> Goodbye!\n")
                exit()
         else:
                 print(f"\nInvalid option, please enter a number or 'exit'\n")
    else:
         guess_number = int(guess_number)
         if guess_number > 99:
                 print('The number must be between "1 and 99"')
         elif guess_number == 0:
                 print('"0" is not in the range')
         elif guess_number > random_num:
            print("Too high!")
         elif guess_number < random_num:
            print("Too low!")
         
    if guess_number == 42 and random_num == 42 and intentos == 1:
                    guess_number == 42 and random_num == 42
                    print(f"The answer to the ultimate question of life, the universe and everything is 42.")
                    print("Congratulations! You got it on your first try!")
                    exit()
                    
    elif guess_number == random_num and intentos == 1:
                    print("Congratulations! You got it on your first try!")
                    exit()

    elif guess_number == 42 and random_num == 42:
            print(f"The answer to the ultimate question of life, the universe and everything is 42.")
            print(f"You won in {intentos} attempts ")
            exit()
         
    elif guess_number == random_num:
                    print("Congratulations, you've got it!")
                    print(f"You won in {intentos} attempts ")
                    exit()