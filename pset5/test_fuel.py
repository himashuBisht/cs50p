from fuel import convert, gauge
import pytest


def main():
    test_zero_division()
    test_value_error()
    test_gauge()
    test_convert()


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(22)=="22%"


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")


if __name__ == "__main__":
    main()
