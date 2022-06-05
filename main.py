import random

while True:
    userAction = input("Enter a choice (R, P, S): ")

    try:
        userAction = input()

    except ValueError:
        print (f"Invalid Input")
        continue

    possibleActions = ["R", "P", "S"]
    computerAction = random.choice(possibleActions)

    print(f"\nYou chose {userAction}, computer chose {computerAction}.\n")

    if userAction == computerAction:
        print(f"Both players selected {userAction}. It's a tie!")
    elif userAction == "R":
        if computerAction == "S":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif userAction == "P":
        if computerAction == "R":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif userAction == "S":
        if computerAction == "P":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")

    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != "y":
        break
