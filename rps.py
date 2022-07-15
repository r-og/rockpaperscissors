import random  # computer will use this to choose a random choice in RPS

# dictionary to hold the different options of rock paper scissors
rps = {0: """
    _______
---'   ____)
      (_____)
rock  (_____)
      (____)
---.__(___)
""",
       1: """
     _______
---'    ____)____
           ______)
 paper    _______)
         _______)
---.__________)
""",
       2: """
    _______
---'   ____)____
          ______)
scissors ________)
      (____)
---.__(___)
"""}

name = input('Please enter your name: ')
welcome_message = f'Hello {name}, welcome to RPS!\n In this game the rules are as follows:\n1. Rock beats Scissors\n2. Paper beats Rock\n3. Scissors beats Paper\nReady to play?? Lets go!\n\n'


# function for the computer to randomly choose an option to play against the user(you)
def computer_choice(rps):
    return random.choice(rps)


# allows the user to enter their own choice of rock, paper, or scissors
def user_choice():
    while True:
        try:
            rps_choice = int(
                input('What do you choose? \n0 = Rock\n1 = Scissors\n2 = Paper\n'))
            if rps_choice > 3:
                print('Not a valid choice! Try again!\n')
                continue
            return rps[rps_choice]
        except ValueError:
            if rps_choice > 3:
                print('Wrong input! Try again...')
                continue


# allows the player to play again once game is completed
def playAgain():
    while True:
        try:
            again = int(input('Play again? 1 = yes 2 = no\n'))
            if again == 1:
                game()
            else:
                print(f'Thanks for playing {name}, have a good day!')
                exit()
        except ValueError:
            print('Incorrect input.. try again\n')
            continue


def game():
    computer_input = computer_choice(rps)

    while True:
        ask_user = user_choice()

        if ask_user == computer_input:
            print(
                f'You tied! computer chose: {computer_input} and you chose: {ask_user}\n')
            break
        elif ask_user == 'rock' and computer_input == 'scissors':
            print('You win! Rock beats scissors\n')
            break
        elif ask_user == 'scissors' and computer_input == 'paper':
            print('You win! Scissors beats paper\n')
            break
        elif ask_user == 'paper' and computer_input == 'rock':
            print('You win! Paper beats rock\n')
            break
        else:
            print(f'You lost.. {computer_input} beats {ask_user}!\n')
            break

    playAgain()


print(welcome_message)
game()
