"""Task 5: Reverse a word."""


def main() -> None:
    """Read a word and print it in reverse order."""
    word = input("Enter a word to reverse: ")
    print("Reversed word:", word[::-1])


if __name__ == "__main__":
    main()
