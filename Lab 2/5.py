"""Lab 2 - Task 5: Demonstrate classes and objects."""


class Person:
    """Represent a person with a name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> None:
        """Print a greeting from this person."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


def main() -> None:
    """Create a Person object and call its method."""
    person = Person("John", 36)
    print("Name:", person.name)
    print("Age:", person.age)
    person.introduce()


if __name__ == "__main__":
    main()
