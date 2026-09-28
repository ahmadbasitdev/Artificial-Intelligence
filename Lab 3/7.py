"""Task 7: Display each value and its data type."""


def main() -> None:
    """Print the values in a mixed-type collection."""
    values = [
        1452,
        11.23,
        1 + 2j,
        True,
        "w3resource",
        (0, -1),
        [5, 12],
        {"class": "V", "section": "A"},
    ]
    for value in values:
        print(f"Item: {value} | Type: {type(value).__name__}")


if __name__ == "__main__":
    main()
