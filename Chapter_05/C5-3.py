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
    print_2dArray([[1.11, 1, 1, 2.2],
                   [1.2222222, 1/3, 1.3, 2.2],
                   [1, 1, 1, 2],
                   [1, 1, 1, 2]
                   ])
    print("\n\n")
    print_2dArray([[1.0, 1, 1, 2],
                   [1.0, 1, 1, 2],
                   [1.0, 1, 1, 2],
                   [1, 1, 1, 2]
                   ])
    print("\n\n")
