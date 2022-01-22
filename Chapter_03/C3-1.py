# This program takes a list and does the following:
# 1. Calculates the mean
# 2. Calculates the difference of each element to the mean
# 3. Squares the result and returns the list
import functools


def get_cubic_deviation(lst: list) -> list:
    mean = functools.reduce(lambda x, y: x + y, lst) / len(lst)
    delta_mean = [i - mean for i in lst]
    square_mean = [i * i for i in delta_mean]

    return square_mean


if __name__ == '__main__':
    print(get_cubic_deviation([1, 2, 3, 4, 5]))
    print(get_cubic_deviation([100, 100, 110, 100, 100]))
