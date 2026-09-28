"""Task 8: Skip selected values with the continue statement."""


def main() -> None:
    """Print values from 0 to 6 except 3 and 6."""
    for number in range(7):
        if number in (3, 6):
            continue
        print(number, end=" ")
    print()


if __name__ == "__main__":
    main()
