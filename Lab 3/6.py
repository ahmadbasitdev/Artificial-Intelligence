"""Task 6: Count even and odd numbers in a series."""


def main() -> None:
    """Count and display even and odd values."""
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    even_count = sum(number % 2 == 0 for number in numbers)
    odd_count = len(numbers) - even_count
    print("Number of even numbers:", even_count)
    print("Number of odd numbers:", odd_count)


if __name__ == "__main__":
    main()
