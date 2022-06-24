import random

Player_Wins = 0
Computer_Wins = 0

def userOption():
    userAction = input("Enter a choice (Rock, Paper, Scissors): ")
    if userAction in ('Rock', 'rock', 'R', 'r'):
        userAction = 'R'

    elif userAction in ('Paer', 'paper', 'P', 'p'):
        userAction = 'P'

    elif userAction in ('Scissors', 'scissors', 'S', 's'):
        userAction = 'S'

    else:
        print('Invalid Input')
        userOption()
    return userAction

def computerChoice():
    computerAction = random.randint(1,3)
    if computerAction == 1:
        computerAction = 'R'

    elif computerAction == 2:
        computerAction = 'P'

    else:
        computerAction = 'S'

    return computerAction

while True:
    print ('')
    userAction = userOption()
    computerAction = computerChoice()
    print ('')

    if userAction == 'R':
        if computerAction == 'R':
            print (f"Both players selected {userAction}. It's a TIE!")

        elif computerAction == 'P':
            print ('Paper covers Rock! You LOSE!')
            Computer_Wins += 1

        elif computerAction == 'S':
            print ('Rock smashes Scissors! You WIN!')
            Player_Wins += 1

    elif userAction == 'P':
        if computerAction == 'P':
            print (f"Both players selected {userAction}. It's a TIE!")

        elif computerAction == 'S':
            print ('Scissors cuts Paper! You LOSE!')
            Computer_Wins += 1

        elif computerAction == 'R':
            print ('Paper covers Rock! You WIN!')
            Player_Wins += 1

    elif userAction == 'S':
        if computerAction == 'S':
            print (f"Both players selected {userAction}. It's a TIE!")

        elif computerAction == 'R':
            print ('Rock smashes Scissors! You LOSE!')
            Computer_Wins += 1

        elif computerAction == 'P':
            print ('Scissors cuts Paper! You WIN!')
            Player_Wins += 1

    print ('')
    print ('Player Wins: ' + str(Player_Wins))
    print ('Computer Wins: ' + str(Computer_Wins))
    print ('')

    play_again = input("Play again? (y/n): ")
    if play_again in ['Yes', 'yes', 'Y', 'y']:
        pass
    elif play_again in ['No', 'no', 'N', 'n']:
        break
    else:
        break