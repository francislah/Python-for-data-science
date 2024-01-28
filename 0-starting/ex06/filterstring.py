import sys


def validateArgs():
    try:
        assert len(sys.argv) == 3 and sys.argv[2].isdigit(), \
            "the arguments are bad"
        for char in sys.argv[1]:
            assert char.isalpha() or char.isspace()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)


validateArgs.__doc__ = \
    "Validate the arguments provided to the program"


def getInt() -> int:
    try:
        return int(sys.argv[2])
    except ValueError as verr:
        print(f"ValueError: {verr}")
    except Exception as ex:
        print(f"Exception: {ex}")
    exit(1)


getInt.__doc__ = \
    "Validate the conversion from string to int even though the limit \
is the available memory in python3"


def filterString(condition) -> []:
    return [word for word in sys.argv[1].split(' ') if condition]


def main():
    validateArgs()
    N = getInt()
    words = filterString(lambda word: len(word) > N)
    print(words)
    return 0


main.__doc__ = \
    "A program that filters words of a string from the length provided"


if __name__ == "__main__":
    main()
