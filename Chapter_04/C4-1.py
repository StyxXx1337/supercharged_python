# This program offers various functions to print a sizexsize square of '*'

import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        gap = after-before
        print("It took {:.8f} seconds".format(gap))

    return wrapper


@timer
def bruteforce(size: int):
    for k in range(size):
        for i in range(size):
            print('*', end='')
        print()


@timer
def rows(size: int):
    row = '*' * size
    for i in range(size):
        print(row)


@timer
def assemble_str(size: int):
    row = '*' * size
    string = ''

    for i in range(size):
        string = string + row + '\n'
    print(string)


@timer
def join_str(size: int):
    row = '*' * size
    rList = []
    for i in range(size):
        rList.append(row)

    print('\n'.join(rList))


if __name__ == '__main__':
    numbers = 20
    bruteforce(numbers)
    print('\n' + '=' * 20 + '\n')
    rows(numbers)
    print('\n' + '=' * 20 + '\n')
    assemble_str(numbers)
    print('\n' + '=' * 20 + '\n')
    join_str(numbers)
    print('\n' + '=' * 20 + '\n')
