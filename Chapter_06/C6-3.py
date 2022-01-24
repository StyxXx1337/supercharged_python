# This program replaces all multiple spaces with a single space and returns the string.

import re


def remove_doubles(string: str, ch: str = ' ') -> str:
    pat = r' {2,}'
    result = re.sub(pat, ch, string, flags=re.MULTILINE)

    return result


if __name__ == '__main__':
    print(remove_doubles("Hello this  is   a    test."))
    multiline_str = '''This is a test  for multi   
    line test. 
    What happens now?    '''
    print(remove_doubles(multiline_str))
    print("Nothing to change.")
    print("NoSpaceInHere")
