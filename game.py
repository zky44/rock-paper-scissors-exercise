# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

options = ['rock', 'paper', 'scissors']






print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# asking user for input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

print(f"You chose: {user_choice}")

user_choice.lower()

if user_choice in options:
    #print("GOOD")
    pass
else:
    print("OOPS, please choose a valid option and try again")
    exit()


# simulating a computer output

options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)


# simulating a computer output
print(f"The computer chose: {computer_choice}")

print("-------------------")

# validate the user selection

# stop the program (not try to setermine the winner)
# ... if the user choice is invalid


# determining who won

if user_choice == computer_choice:
    print("It's tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Congrats")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Oh! The computer won, that's ok!")


print("-------------------")
print("Thanks for playing. Please play again!")