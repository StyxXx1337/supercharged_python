# This Program creates an generator of perfect squares and prints it
# The second part checks if the number entered is a perfect square.
from typing import Iterable


def perfect_square_gen(size: int) -> Iterable[int]:
    for base in range(size):
        square = base ** 2
        if square > size:
            break

        yield square


if __name__ == "__main__":
    for i in perfect_square_gen(50):
        print(i)

    number = int(input("Enter a number:"))

    if number in (perfect_square_gen(number)):
        print("True")
    else:
        print("False")
