

def test_func():
    name = input("What is your name? ")
    address = input("Tell me your address: ")
    age = input("How old are you?")


    print(f"Hello {name} from {address}. You look younger than {age}")


if __name__ == '__main__':
    test_func()