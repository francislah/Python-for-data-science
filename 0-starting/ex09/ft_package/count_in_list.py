
def count_in_list(lst: [], find: any) -> int:
    count = 0
    for item in lst:
        if item == find:
            count += 1
    return count


count_in_list.__doc__ = \
    "Function that counts the number of item to find present in a list"
