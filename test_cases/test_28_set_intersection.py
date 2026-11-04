import importlib

module = importlib.import_module("28_set_intersection")
set_intersection = module.set_intersection

def test_intersection_normal():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}

def test_intersection_disjoint():
    assert set_intersection({1, 2}, {3, 4}) == set()

def test_intersection_empty():
    assert set_intersection(set(), {1, 2}) == set()

def test_intersection_identical():
    assert set_intersection({1, 2}, {1, 2}) == {1, 2}