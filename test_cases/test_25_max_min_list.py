import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min

def test_max_min_normal():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)

def test_max_min_single():
    assert find_max_min([5]) == (5, 5)

def test_max_min_negatives():
    assert find_max_min([-5, -1, -10]) == (-1, -10)

def test_max_min_empty_raises_error():
    with pytest.raises(ValueError):
        find_max_min([])