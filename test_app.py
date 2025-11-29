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

    # Invalid type should raise
    from pytest import raises

    with raises(TypeError):
        is_strong_password(1234)  # type: ignore
