import random  # computer will use this to choose a random choice in RPS

# dictionary to hold the different options of rock paper scissors
rps = {0: 'rock',
       1: 'scissors',
       2: 'paper'}

name = input('Please enter your name: ')
welcome_message = f'Hello {name}, welcome to RPS! Ready to play?? Lets go!\n\n'

def computer_choice(rps):
    return random.choice(rps)


def user_choice():
    while True:
        try:
            rps_choice = int(input('What do you choose? \n0 = Rock\n1 = Scissors\n2 = Paper\n'))
            return rps[rps_choice]
        except ValueError:
            print('Thats not a number! Try again...')
            continue

def playAgain():
    while True:
        try:
            again = int(input('Play again? 1 = yes 2 = no\n'))
            if again == 1:
                game()
            else:
                exit()
        except ValueError:
            print('Incorrect input.. try again\n')
            continue

def game():
    computer_input = computer_choice(rps)
    
    while True:
        ask_user = user_choice()

        if ask_user == computer_input:
            print(f'You tied! computer chose: {computer_input} and you chose: {ask_user}\n')
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

