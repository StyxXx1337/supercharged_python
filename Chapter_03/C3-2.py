# This program takes a list and returns the median

def get_median(lst: list[int]) -> float:
    lst.sort()
    middle = len(lst) // 2

    if len(lst) == 1:
        return lst[0]
    elif len(lst) % 2 == 0:
        return (lst[middle - 1] + lst[middle])/2

    return lst[middle]


if __name__ == '__main__':
    print(get_median([1, 3, 2, 4, 5]))  # 3
    print(get_median([10000, 1, 2, 3]))  # 2.5
    print(get_median([1])) # 1
