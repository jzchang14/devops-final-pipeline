# test_app.py

from app import add, is_strong_password


def test_add_simple():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_is_strong_password_valid():
    assert is_strong_password("abcd1234")
    assert is_strong_password("P@ssw0rd123")


def test_is_strong_password_invalid():
    # Too short
    assert not is_strong_password("short1")

    # No digits
    assert not is_strong_password("onlyletters")

    # Invalid type should raise TypeError
    try:
        is_strong_password(1234)  # type: ignore
    except TypeError:
        pass  # Expected
    else:
        raise AssertionError("TypeError was not raised for non-string password")


if __name__ == "__main__":
    # Allow running tests with: python3 test_app.py
    test_add_simple()
    test_is_strong_password_valid()
    test_is_strong_password_invalid()
    print("All tests passed.")
