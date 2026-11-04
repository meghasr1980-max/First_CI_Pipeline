import importlib
import pytest

module = importlib.import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary

def test_decimal_to_binary_normal():
    assert decimal_to_binary(10) == "1010"

def test_decimal_to_binary_zero():
    assert decimal_to_binary(0) == "0"

def test_decimal_to_binary_one():
    assert decimal_to_binary(1) == "1"

def test_decimal_to_binary_negative_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)