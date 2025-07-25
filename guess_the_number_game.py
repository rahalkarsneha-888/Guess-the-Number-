

import random

def play_game():
    print("\n🎮 Welcome to the Advanced Guess the Number Game!")
    print("I’m thinking of a number between 1 and 100.")
    print("You have 5 chances to guess it!\n")

    secret_number = random.randint(1, 100)
    attempts = 5
    score = 100

    while attempts > 0:
        try:
            guess = int(input(f"Guess the number (Attempts left: {attempts}): "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {6 - attempts} attempts.")
            print(f"🏆 Your score: {score}")
            break

        attempts -= 1
        score -= 20

    else:
        print(f"\n😢 Sorry! You've run out of attempts.")
        print(f"The correct number was: {secret_number}")
        print("🏁 Better luck next time!")

    # Play again option
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again == "yes":
        play_game()
    else:
        print("👋 Thanks for playing!")

# Start the game
play_game()
