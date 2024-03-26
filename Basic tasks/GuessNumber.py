import random

def number_guessing_game():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    max_attempts = 10
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"Guess a number between {lower_bound} and {upper_bound}.")

    while attempts < max_attempts:
        user_guess = get_user_input(lower_bound, upper_bound)
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Try again! Your guess is too low.")
        else:
            print("Try again! Your guess is too high.")

    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The secret number was {secret_number}.")

def get_user_input(lower_bound, upper_bound):
    while True:
        try:
            user_guess = int(input(f"Enter your guess ({lower_bound}-{upper_bound}): "))
            if lower_bound <= user_guess <= upper_bound:
                return user_guess
            else:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()
