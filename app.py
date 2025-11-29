# app.py

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def is_strong_password(pwd: str) -> bool:
    """
    Very simple password strength check:
    - At least 8 characters
    - Contains at least one digit
    """
    if not isinstance(pwd, str):
        raise TypeError("Password must be a string")

    has_min_length = len(pwd) >= 8
    has_digit = any(ch.isdigit() for ch in pwd)

    return has_min_length and has_digit


if __name__ == "__main__":
    # Small manual check so running `python app.py` does something.
    print("2 + 3 =", add(2, 3))
    print("Is 'abcd1234' strong?", is_strong_password("abcd1234"))
