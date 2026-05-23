import random

print("Welcome to the Number Guessing Game!")

# Random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    print(f"Attempts left: {max_attempts - attempts}")

if guess != secret_number:
    print(f"Game Over! The correct number was {secret_number}")

