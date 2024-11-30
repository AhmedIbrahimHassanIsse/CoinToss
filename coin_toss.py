# Name: Ahmed (Nur) Hassan
# User ID: Hass0338
# Assignment: NET2008 - Fall 2024 - Assignment 4
# Student Number: 040917085
# Date: 11/25/2024

import random

def get_user_choice():
    """Get the user's choice and validate input."""
    choices = ['heads', 'tails', 'end']
    choice = input("Welcome to the generic coin toss game. Enter Heads, Tails, or type 'End' to finish the game: ").lower()
    if choice in choices:
        return choice
    else:
        print("HEY, enter either HEADS, TAILS OR END. We can do this all day if you won't cooperate.")
        return get_user_choice()

def flip_coin():
    """Simulate a coin flip."""
    return random.choice(['heads', 'tails'])

def play_game():
    """Play the Coin Toss Game with scoring and endgame options."""
    print("Welcome to the Coin Toss Game!")
    correct_guesses = 0
    incorrect_guesses = 0

    while True:
        user_choice = get_user_choice()

        if user_choice == 'end':
            break

        result = flip_coin()
        print(f"The coin landed on {result}.")

        if user_choice == result:
            print("You guessed right!")
            correct_guesses += 1
        else:
            print("You guessed wrong.")
            incorrect_guesses += 1

        # Calculate and display current score
        final_score = correct_guesses - incorrect_guesses
        print(f"Current Score: {correct_guesses} correct, {incorrect_guesses} incorrect.")
        print(f"Your current final score is: {final_score}\n")

    # Game over message and final score calculation
    print("\nGame Over!")
    print(f"Final Score: {final_score} (Correct: {correct_guesses}, Incorrect: {incorrect_guesses})")

    # Determine outcome
    if final_score > 0:
        print("Congratulations - are you some kind of genius?")
    elif final_score < 0:
        print("Guess the cards weren't in your favor this time around?")
    else:
        print("It's stalemate! You gotta keep playing to break the stalemate mate!")

if __name__ == "__main__":
    play_game()
