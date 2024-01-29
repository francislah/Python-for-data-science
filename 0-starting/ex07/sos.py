import sys


def NESTED_MORSE() -> dict:
    return {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....',   'I': '..',
            'J': '.---', 'K': '-.-',    'L': '.-..', 'M': '--',
            'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
            'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',  '2': '..---', '3': '...--',
            '4': '....-',  '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': '/'
            }


NESTED_MORSE.__doc__ = \
    "Function that returns Morse Code as a dictionnary"


def validate_args() -> str:
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        return sys.argv[1]
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)


validate_args.__doc__ = \
    "Function that validate the number of arguments and return the input"


def main() -> int:
    morse_result = ""
    for i, char in enumerate(validate_args()):
        try:
            assert char.isalnum() or char.isspace(), "the arguments are bad"
            assert char.upper() in NESTED_MORSE() or char.lower() in \
                NESTED_MORSE(), "You tricked the dictionnary"
            if i > 0:
                morse_result += " "
            morse_result += NESTED_MORSE()[char.upper()]
        except AssertionError as e:
            print(f"AssertionError: {e}")
            exit(2)
    print(morse_result)
    return 0


main.__doc__ = \
    "A program that takes a string as an argument \
and encodes it into Morse Code."


if __name__ == "__main__":
    main()
