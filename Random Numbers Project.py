import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the target:"))
    
    if (userChoice == target):
        print("Success! you have guessed it correct")
        break
    elif (userChoice < target):
        print("Guessed number is too small. Guess some big number!")
    else:
        print("Guessed number is too big. Guess some small number")

print("---- GAME OVER ----")
