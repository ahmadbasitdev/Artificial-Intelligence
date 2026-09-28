"""Lab 2 - Task 4: Demonstrate Python functions."""


def greet(name: str, country: str = "Pakistan") -> None:
    """Print a greeting using a required and a default parameter."""
    print(f"{name} is from {country}.")


def multiply_by_five(value: int) -> int:
    """Return five times the supplied value."""
    return value * 5


def main() -> None:
    """Demonstrate parameters, default values, lists, and return values."""
    greet("A student")
    greet("Emil", "Sweden")
    print("Result:", multiply_by_five(3))

    print("List parameter:")
    for fruit in ["apple", "banana", "cherry"]:
        print(fruit)


if __name__ == "__main__":
    main()
