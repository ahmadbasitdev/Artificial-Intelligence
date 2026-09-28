"""Task 4: Construct a diamond-shaped star pattern."""


def main() -> None:
    """Print the upper and lower halves of the pattern."""
    for count in range(1, 6):
        print("* " * count)
    for count in range(4, 0, -1):
        print("* " * count)


if __name__ == "__main__":
    main()
