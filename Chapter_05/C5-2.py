# This program writes a matrix to the CLI formatted to the largest number in the array

def print_2dArray(lst: list):
    # simple solution
    width = 1
    row_string = ''

    for r in lst:
        for c in r:
            temp = len(str(c))
            if temp > width:
                width = temp

    for r in lst:
        for c in r:
            print("{:^{w}}".format(c, w=width + 2), end='')
        print()


if __name__ == '__main__':
    print_2dArray([[1, 10, 100, 200],
                   [1, 10, 100, 200],
                   [1, 10, 100, 200],
                   [1, 10, 10000, 200]
                   ])
    print("\n\n")
    print_2dArray([[10000000, 1, 10, 20],
                   [1, 10, 10, 20],
                   [1, 10, 10, 20],
                   [1, 10, 10, 20]
                   ])
    print("\n\n")
    print_2dArray([[1, 1, 1, 2],
                   [1, 1, 1, 2],
                   [1, 1, 1, 2],
                   [9, 1, 1, 9]
                   ])
    print("\n\n")
    print_2dArray([[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]
                   ])
    print("\n\n")
    print_2dArray([[9.99999999, 1, 10, 20],
                   [1, 10, 10, 20],
                   [1, 10, 10, 20],
                   [1, 10, 10, 20]
                   ])
