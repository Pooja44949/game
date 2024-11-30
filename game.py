import random

def get_computer_choice():
    choices=['rock','paper','scissors']
    return random.choice(choices)

def get_user_choice():
    while True:
        user_input=input("Enter your choice(rock,paper,or scissors):").lower()
        if user_input in ['rock','paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice, please choose again.")

            def determine_winner(user_choice, computer_choice):
                if user_choice==computer_choice:
                    return"It's a tie!"
                elif(user_choice=='rock'and computer_choice=='scissors')or\
                     (user_choice=='scissors'and computer_choice=='paper')or\
                     (user_choice=='paper'and computer_choice=='rock'):
                    return "You win!"
                else:
                    return "Computer wins!"