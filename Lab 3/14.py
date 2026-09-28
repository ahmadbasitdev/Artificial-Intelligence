"""Task 14: Count letters and digits in a string."""


def main() -> None:
    """Count alphabetic characters and digits."""
    text = input("Enter a string: ")
    letters = sum(character.isalpha() for character in text)
    digits = sum(character.isdigit() for character in text)
    print("Letters:", letters)
    print("Digits:", digits)


if __name__ == "__main__":
    main()
