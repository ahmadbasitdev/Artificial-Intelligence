"""Task 3: Guess a number between 1 and 9."""

from random import randint


def main() -> None:
    """Continue asking until the randomly selected number is guessed."""
    target = randint(1, 9)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 9: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if guess == target:
            print("Well guessed!")
            return
        print("Try again.")


if __name__ == "__main__":
    main()
