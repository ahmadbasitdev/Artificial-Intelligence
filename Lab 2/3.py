"""Lab 2 - Task 3: Demonstrate loop control statements."""


def main() -> None:
    """Demonstrate continue and break."""
    print("Continue example:")
    for character in "geeksforgeeks":
        if character in "es":
            continue
        print(character, end="")
    print()

    print("Break example:")
    for character in "geeksforgeeks":
        if character in "es":
            break
        print(character, end="")
    print()


if __name__ == "__main__":
    main()
