import math
# 1.filter
numbers = [3, 5, 7, 1, -2, 8, 18, -100, -3, -5, 9]


def positive_numbers(x):
    if x > 0:
        return True
    else:
        return False


def even_numbers(x):
    if x % 2 == 0:
        return True
    else:
        return False


def test_positive_numbers():
    assert positive_numbers(4)
    assert not positive_numbers(-3)
    assert not positive_numbers(-10)


def test_even_numbers():
    assert even_numbers(4)
    assert not even_numbers(-3)
    assert even_numbers(-10)


def test_filter():
    assert list(filter(positive_numbers, numbers)) == [3, 5, 7, 1, 8, 18, 9]
    assert list(filter(even_numbers, numbers)) == [-2, 8, 18, -100]
    assert list(filter(lambda x: x < 0, numbers)) == [-2, -100, -3, -5]


# 2.map
def test_map():
    assert list(map(lambda x: x + 1, numbers)) == [4, 6, 8, 2, -1, 9, 19, -99, -2, -4, 10]
    assert list(map(lambda x: x*x, numbers)) == [9, 25, 49, 1, 4, 64, 324, 10000, 9, 25, 81]


# 3.sorted
def test_sorted():
    assert list(sorted(numbers)) == [-100, -5, -3, -2, 1, 3, 5, 7, 8, 9, 18]
    assert list(sorted(numbers, reverse = True)) == [18, 9, 8, 7, 5, 3, 1 ,-2, -3, -5, -100]


# 4.pi
def test_pi():
    assert  3 < math.pi < 4


# 4.sqrt
def test_sqrt():
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4


# 5.pow
def test_pow():
    assert math.pow(9, 2) == 81
    assert math.pow(4, 0.5) == 2


# 5.hypot
def test_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(5, 12) == 13