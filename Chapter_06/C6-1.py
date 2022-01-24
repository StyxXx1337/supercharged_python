# This program checks an america phone number for correctness.
# With or without country and area code
# +1 123 456 7890
#  ^   ^------------ area code
#  ^--------------- country code

import re


def valid_phone_number(number: str) -> bool:
    pat = r'(\d{3}[- ])?\d{3}[ -]\d{4}'
    if re.match(pat, number):
        # print(re.match(pat, number))
        return True
    return False


if __name__ == '__main__':
    print("====== True Cases =========")
    print(valid_phone_number("234-456-7890"))
    print(valid_phone_number("456-7890"))
    print(valid_phone_number("234 456 7890"))
    print(valid_phone_number("456 7890"))

    print("\n====== False Cases =========")
    print(valid_phone_number("7890"))
    print(valid_phone_number("45 7890"))
    print(valid_phone_number("12 456 7890"))
    print(valid_phone_number("1 123 456 7890"))
    print(valid_phone_number("+81-234-456-7890"))
    print(valid_phone_number("+81+234+456+7890"))
