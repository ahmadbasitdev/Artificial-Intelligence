"""Task 9: Print the Fibonacci series below 50."""


def main() -> None:
    """Display Fibonacci values less than 50."""
    previous, current = 0, 1
    while current < 50:
        print(current, end=" ")
        previous, current = current, previous + current
    print()


if __name__ == "__main__":
    main()
