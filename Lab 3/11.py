"""Task 11: Generate a multiplication matrix."""


def main() -> None:
    """Create an m by n matrix where each value is row multiplied by column."""
    try:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
    except ValueError:
        print("Rows and columns must be whole numbers.")
        return

    if rows < 0 or columns < 0:
        print("Rows and columns cannot be negative.")
        return

    matrix = [[row * column for column in range(columns)] for row in range(rows)]
    print("Generated 2D array:")
    print(matrix)


if __name__ == "__main__":
    main()
