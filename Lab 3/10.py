"""Task 10: Print FizzBuzz from 1 through 50."""


def main() -> None:
    """Print FizzBuzz values."""
    for number in range(1, 51):
        if number % 15 == 0:
            result = "FizzBuzz"
        elif number % 3 == 0:
            result = "Fizz"
        elif number % 5 == 0:
            result = "Buzz"
        else:
            result = str(number)
        print(result)


if __name__ == "__main__":
    main()
