import sys


def f_assert(comparision: any, err: str) -> bool:
    try:
        assert comparision, err
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return False
    return True


def whatis() -> int:
    n_args = len(sys.argv)
    if n_args == 1:
        return 0
    if not f_assert(n_args == 2, "more than one argument is provided"):
        return 1
    if not f_assert(sys.argv[1].isdigit(), "argument is not an integer"):
        return 2
    match int(sys.argv[1]) % 2:
        case 0:
            print("I'm Even.")
        case 1:
            print("I'm Odd.")


whatis()
