
import random

def number_guessing_game():

    number_answer = random.randint(1, 100)

    previous_guesses = []

    guess = None

    print("Welcome to the Number Guessing Game.")
    print("Please guess a number 1 through 100 and I'll help along the way!")

    while guess != number_answer:

        try:
            guess = int(input("Enter your guess: "))

            if guess in previous_guesses:

                print("You already guessed that number! Try something new.")
                continue

            previous_guesses.append(guess)


            if guess < number_answer:

                print("Too low!")
            elif guess > number_answer:

                print("Too high!")
            else:
                print(f"You got it! The number was {number_answer}.")

                print(f"It took you {len(previous_guesses)} guesses.")
                print("Number of Attempts:", previous_guesses)
        except ValueError:
             print("Please enter a valid number.")

number_guessing_game()

