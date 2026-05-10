import random

def guessing_game():
    """A simple number guessing game where the user tries to guess a secret number."""
    secret_number = random.randint(1, 100)
    max_guesses = 10
    guesses_taken = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_guesses} guesses.")

    while guesses_taken < max_guesses:
        try:
            guess = int(input("Enter your guess: "))
            guesses_taken += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {guesses_taken} guesses!")
                return

        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(f"Sorry, you ran out of guesses. The secret number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()
