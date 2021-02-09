# game.py

#first, import all modules and 3rd party packages
from dotenv import load_dotenv
import os
import random

#print the title of the game
print("Rock, Paper, Scissors, Shoot!")

#define the "options" variable
options = ['rock', 'paper', 'scissors']

print("-------------------")


load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file.

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable

#Welcome the user to the game using the PLAYER_NAME in the dotenv file
print(f"Welcome, {PLAYER_NAME} to my Rock-Paper-Scissors game...")
print("-------------------")

# ask user for input and display result
user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
user_choice = user_choice.lower()

print(f"You chose: {user_choice}")


# validate the user selection
# stop the program if the user choice is invalid
if user_choice in options:
    #print("GOOD")
    pass
else:
    print("Oops, please choose a valid option and try again")
    exit()

# simulate a computer output
options = ['rock', 'paper', 'scissors']

computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")

print("-------------------")

# determining who won
# this code was written during class but adapted from solution shared by Will P during class

if user_choice == computer_choice:
    print("It's a tie!")
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