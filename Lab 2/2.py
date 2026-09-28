"""Lab 2 - Task 2: Demonstrate for-in loops."""


def main() -> None:
    """Iterate over a list, tuple, string, and indexed sequence."""
    fruits = ["apple", "banana", "cherry"]
    print("List:")
    for fruit in fruits:
        print(fruit)

    print("Tuple:")
    for item in ("first", "second", "third"):
        print(item)

    print("String:")
    for character in "Python":
        print(character)

    print("By index:")
    for index in range(len(fruits)):
        print(fruits[index])


if __name__ == "__main__":
    main()
