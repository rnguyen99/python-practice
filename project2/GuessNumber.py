'''
Project 2: Number Guessing Game

Milestones
    Generate random number
    Loop until guessed correctly
    Give high/low hints

Stretch Goals
    Difficulty levels
    Limited attempts
    Score tracking to file

You’ll Learn
    Loops
    random
    Game logic
'''
import random

def get_difficulty_level() -> int:
    while True:
        level = input("Choose difficulty level - Easy (1), Medium (2), Hard (3): ").strip()
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_max_attempts(level: int) -> int:
    if level == 1:
        return 10
    elif level == 2:
        return 7
    elif level == 3:
        return 5
    else:
        raise ValueError("Invalid difficulty level.")
    
def save_score(level: int, attempts: int, result: str) -> None:
    with open("project2/scores.txt", "a") as file:
        file.write(f"Level: {level}, Attempts: {attempts}, Result: {result}\n")


def main():
    print("Welcome to the Number Guessing Game!")
    level = get_difficulty_level()
    max_attempts = get_max_attempts(level)
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            save_score(level, attempts, "Win")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        save_score(level, attempts, "Lose")

if __name__ == "__main__":
    main()