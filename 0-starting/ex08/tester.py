from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()
    return


main.__doc__ = \
    "Compare the real tqdm with my own ft_tqdm"


if __name__ == "__main__":
    main()
