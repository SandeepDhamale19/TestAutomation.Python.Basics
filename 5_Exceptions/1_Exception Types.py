import sys

DIGIT_MAP = {
    'Zero': '0',
    'One': '1',
    'Two': '2',
    'Three': '3',
    'Four': '4',
    'Five': '5',
    'Six': '6',
    'Seven': '7',
    'Eight': '8',
    'Nine': '9'
}


def convert(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x


print(convert("Nine Nine Three Zero Three One One Nine Zero Five".split()))
# print(convert("I am Two Eight year's old".split())) #Exception: KeyError

print("\n Handling exceptions:")
print("\tTry..catch")


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except KeyError:
        print("\tConversion failed!")
        x = -1
    return x


print("\t" + str(convert("I am Two Eight year's old".split())))  # Exception: KeyError Handled


# print(convert(51)) #Exception again: TypeError: 'int' object is not iterable

def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion Succeeded! x={x}")
    except (KeyError, TypeError):
        print("\tConversion failed!")
        x = -1
    return x


print("\t" + str(convert(51)))  # Exception again: TypeError: 'int' object is not iterable

print("\n1. Programmers error")
print("""
\tA. Indentation Error
\tB. Syntax error
\tC. Name Error""")
print("\tModify above program by initializing value for x:")


def convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except (KeyError, TypeError):
        pass  # pass is ignore statement. DOes nothing but prevents below error
    return x  # IndentationError: expected an indented block due empty expect block


print("\nGet error messages and error types")


def convert(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as ex:
        print(f"Exception: {ex!r}", file=sys.stderr)
    return -1


print("\t" + str(convert("fail".split())))
