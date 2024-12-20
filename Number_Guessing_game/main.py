from art import logo
import random

# Global Variables
SECRET_NUM = 0
GUESS = 0
ATTEMPTS = 0

# Function to generate random number
def generate_random_number():
    secret_num = 0
    secret_num = random.randint(1,100)
    return  secret_num

# returning the random number generated to the global variable
# SECRET_NUM = generate_random_number()

def make_a_guess():
    guess = int(input("Make a guess: "))
    return guess
# GUESS = make_a_guess()


def mode_selector():
    global ATTEMPTS
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if mode == "easy":
        ATTEMPTS = 10
    elif mode == "hard":
        ATTEMPTS = 5
    else:
        print("Invalid mode. Setting default mode to 'easy'.")
        ATTEMPTS = 10


def game():
    global SECRET_NUM, GUESS, ATTEMPTS

    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    SECRET_NUM = generate_random_number()

    mode_selector()

    print(f"You have {ATTEMPTS} remaining to guess the number.")

    while ATTEMPTS > 0:
        GUESS = make_a_guess()

        if GUESS > SECRET_NUM:
            print("Too high")
        elif GUESS < SECRET_NUM:
            print("Too low")
        elif GUESS == SECRET_NUM:
            print(f"Congratulations! You've guessed the number {SECRET_NUM}.")

        ATTEMPTS -= 1
        print(f"You have {ATTEMPTS} remaining.")

    print(f"You ran out of attempts, the secret number was {SECRET_NUM} Better luck next time!")

# Start the game
game()
