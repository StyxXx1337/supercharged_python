# This function asks for a string and returns the string without the first 2 and last 2 characters.

def cut_both_sides(string: str, amount: int = 2):
    if (amount < 0):
        amount = amount * -1

    return string[amount:-amount]


if __name__ == '__main__':
    assert (cut_both_sides("Hello World", 3) == "lo Wo")
    assert (cut_both_sides("Hello World") == "llo Wor")
    assert (cut_both_sides("I am") == "")
    assert (cut_both_sides("") == "")
    assert (cut_both_sides("I am", 9) == "")
