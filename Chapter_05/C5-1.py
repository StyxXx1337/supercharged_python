# This is a hex summation tool

def calculator():

    sum = 0
    inp = input("Enter a hex number to add: ")

    while inp.isalnum():
        sum += int(inp, 16)
        print("{:X}".format(sum))
        inp = input("Enter a hex number to add: ")

    print("\n === Exited ===")


if __name__ == "__main__":
    calculator()

