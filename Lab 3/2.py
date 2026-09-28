"""Task 2: Convert temperatures between Celsius and Fahrenheit."""


def main() -> None:
    """Display sample temperature conversions."""
    celsius = 60
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius} C is {fahrenheit:.0f} F")

    fahrenheit = 45
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit} F is {celsius:.0f} C")


if __name__ == "__main__":
    main()
