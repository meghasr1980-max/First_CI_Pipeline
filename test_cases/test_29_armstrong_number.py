import importlib

module = importlib.import_module("29_armstrong_number")
is_armstrong = module.is_armstrong

def test_armstrong_true():
    assert is_armstrong(153) is True

def test_armstrong_false():
    assert is_armstrong(123) is False

def test_armstrong_single_digit():
    assert is_armstrong(9) is True

def test_armstrong_negative():
    assert is_armstrong(-153) is False