import importlib

module = importlib.import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort

def test_sort_normal():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]

def test_sort_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_sort_empty():
    assert bubble_sort([]) == []

def test_original_list_unchanged():
    original = [3, 1, 2]
    sorted_arr = bubble_sort(original)
    assert original == [3, 1, 2]
    assert sorted_arr == [1, 2, 3]