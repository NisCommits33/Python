import random


def play_game():
    """Contains the main logic for a single game of number guessing."""
    correct_number = random.randint(1, 10)
    guess_chances = 3

    print("I'm thinking of a number between 1 and 10. You have 3 tries to guess it.")

    for attempt in range(guess_chances):
        try:
            guessed_number = int(input("Enter your number: "))
        except ValueError:
            print("That's not a valid number! Please enter an integer.")
            continue  # Skips to the next loop iteration

        if 1 <= guessed_number <= 10:
            if guessed_number == correct_number:
                print(f"✅ Correct! You win in {attempt + 1} attempt(s).")
                return  # Exits the function and ends the game
            elif guessed_number > correct_number:
                print("❌ Your guess is too high.")
            else:
                print("❌ Your guess is too low.")

            remaining = guess_chances - (attempt + 1)
            if remaining > 0:
                print(f"You have {remaining} chance(s) remaining.")
        else:
            print("Please enter a number between 1 and 10.")

    # This block only runs if the loop finishes without a 'return' statement.
    print(f"\n❌ You lose! The correct number was {correct_number}.")


# Main game loop to allow the user to play again
while True:
    play_game()
    start_again = input("Do you want to play again? (yes/no): ").lower()
    if start_again != "yes":
        break

print("Thanks for playing!")