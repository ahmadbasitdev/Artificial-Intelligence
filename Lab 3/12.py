"""Task 12: Convert input lines to lowercase."""


def main() -> None:
    """Read lines until an empty line is entered, then print lowercase text."""
    print("Enter lines of text (press Enter on an empty line to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line.lower())

    print("\nLines in lowercase:")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
