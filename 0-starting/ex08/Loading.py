def ft_tqdm(lst: range) -> None:
    percent = 0
    total = len(lst)
    spaces = " " * 121
    for i, x in enumerate(lst):
        yield x
        percent = '{:3.0f}'.format(i / total * 100)
        loading = spaces.replace(' ', '█', round(i / total * len(spaces)))
        print(f"{percent}%|{loading}| {i + 1:>{len(str(total))}}/{total}", end='\r')


ft_tqdm.__doc__ = \
    "Function that copy the tqdm loading bar"
