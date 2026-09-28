"""Task 15: Validate a password."""


def is_valid_password(password: str) -> bool:
    """Return whether a password meets all required security rules."""
    if not 6 <= len(password) <= 16:
        return False

    return (
        any(character.islower() for character in password)
        and any(character.isupper() for character in password)
        and any(character.isdigit() for character in password)
        and any(character in "$#@" for character in password)
    )


def main() -> None:
    """Read a password and display its validation result."""
    password = input("Enter password: ")
    if is_valid_password(password):
        print("Valid password")
    else:
        print("Invalid password")


if __name__ == "__main__":
    main()
