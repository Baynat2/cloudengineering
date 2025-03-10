import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        # Ask the user for their guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()