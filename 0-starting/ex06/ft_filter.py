
def ft_filter(condition: any or None, iterable: any) -> any:
    result = []
    try:
        for iter in iterable:
            if condition is None or condition(iter):
                result.append(iter)
    except TypeError as e:
        print(f"TypeError: {e}")
        exit(1)
    return result


ft_filter.__doc__ = \
    "ft_filter(function or None, iterable) --> filter object\n\n\
Return an iterator yielding those items of iterable for which function(item)\n\
is true. If function is None, return the items that are true."


def main() -> int:
    array = ["1", "2", "3"]
    print(f"{ft_filter.__doc__}\n")
    # result = ft_filter(lambda x: x == "1", array)
    result = ft_filter(None, array)
    print(result)
    return 0


main.__doc__ = "A program to reproduce the original fiter function behavior"

if __name__ == "__main__":
    main()
