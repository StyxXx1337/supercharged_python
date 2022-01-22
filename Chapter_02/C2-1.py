# This program asks for an input and counts the vowels

vowels = "aeiou"


def count_vowels(line: str) -> tuple[int, int]:
    c = 0
    v = 0

    for ch in line:
        if ch in vowels:
            v = v + 1
        elif ch not in vowels:
            c = c + 1

    return c, v


if __name__ == '__main__':
    line = input("Please input a string: ")
    consonants, vowels = count_vowels(line)
    print(f"There are {consonants} consonants and {vowels} vowels in your string.")
