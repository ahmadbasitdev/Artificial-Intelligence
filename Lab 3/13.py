"""Task 13: Find four-digit binary values divisible by 5."""


def main() -> None:
    """Read comma-separated binary values and print matching values."""
    values = input("Enter comma-separated 4-digit binary numbers: ").split(",")
    divisible_values = []

    for value in values:
        value = value.strip()
        if len(value) != 4 or any(bit not in "01" for bit in value):
            print(f"Skipping invalid binary value: {value}")
            continue
        if int(value, 2) % 5 == 0:
            divisible_values.append(value)

    print("Numbers divisible by 5:", ",".join(divisible_values))


if __name__ == "__main__":
    main()
