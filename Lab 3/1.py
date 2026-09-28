"""Task 1: Find numbers divisible by 7 and 5."""


def main() -> None:
    """Print numbers from 1500 through 2700 divisible by 7 and 5."""
    numbers = [
        number
        for number in range(1500, 2701)
        if number % 7 == 0 and number % 5 == 0
    ]
    print(", ".join(map(str, numbers)))


if __name__ == "__main__":
    main()
