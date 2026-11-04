import importlib

module = importlib.import_module("26_sum_of_list")
sum_of_list = module.sum_of_list

def test_sum_normal():
    assert sum_of_list([1, 2, 3, 4]) == 10

def test_sum_empty():
    assert sum_of_list([]) == 0

def test_sum_negative():
    assert sum_of_list([-1, -2, 3]) == 0

def test_sum_single():
    assert sum_of_list([42]) == 42