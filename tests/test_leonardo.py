from leonardo import leonardo
import pytest


def test_third_elem():
    assert leonardo(3) == 5, "Test failed"


def test_wrong_elem():
    assert leonardo(2) == 9, "Test expected value 3"


def test_wrong_format():
    with pytest.raises(TypeError):
        assert leonardo("2")


def test_negative_n():
    with pytest.raises(ValueError):
        assert leonardo(-4)
