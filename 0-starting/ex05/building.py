import sys


def getInput() -> str:
    if len(sys.argv) > 2:
        print("Wrong number of arguments")
        exit(1)
    elif len(sys.argv) == 2 and len(sys.argv[1]) > 0:
        return sys.argv[1]
    else:
        return input("What is the text to count?\n")


getInput.__doc__ = \
    "Returns the string retrieved from arguments or user input, \
        or exit the program."


def countCharacters(text: str):
    upper_case = sum(1 for char in text if char.isupper())
    lower_case = sum(1 for char in text if char.islower())
    punctuations = sum(1 for char in text if "?!.,\"';:-[]()/".find(char) > -1)
    spaces = sum(1 for char in text if char.isspace())
    digits = sum(1 for char in text if char.isdigit())

    print(f"{upper_case} upper letters")
    print(f"{lower_case} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


countCharacters.__doc__ = \
    "Counts thee number of specific characters and print the value of each"


def main():
    user_input = getInput()
    print(f"The text contains {len(user_input)} characters:")
    countCharacters(user_input)
    # print(main.__doc__)


main.__doc__ = \
    "A program that takes a single string argument \
and displays the sums of its upper-case characters, lower-case characters, \
punctuation characters, digits and spaces."

if __name__ == "__main__":
    main()
