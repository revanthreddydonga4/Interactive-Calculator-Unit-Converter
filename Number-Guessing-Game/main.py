import random


def number_guessing_game():
    print("\n===== Number Guessing Game =====")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess == secret_number:
                score = (max_attempts - attempts + 1) * 10
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
                print(f"🏆 Your Score: {score}")
                return
            elif guess < secret_number:
                print("Too Low!")
            else:
                print("Too High!")

            print(f"Attempts Left: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid number.")

    print(f"\n❌ Game Over! The correct number was {secret_number}.")


def word_counter():
    print("\n===== Word Counter =====")

    filename = input("Enter text file name (example: sample.txt): ")

    try:
        with open(filename, "r") as file:
            text = file.read().lower()

        words = text.split()

        print("\nTotal Words:", len(words))

        frequency = {}

        for word in words:
            word = word.strip(".,!?;:\"'()[]")
            frequency[word] = frequency.get(word, 0) + 1

        print("\nWord Frequency:")
        for word, count in sorted(frequency.items()):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found!")


def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


main()