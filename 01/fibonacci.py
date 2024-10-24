def fibonacci_sequence(n: int) -> bool:
    sequence: list = [0, 1]
    index: int = 2
    while (not n in sequence):
        add: int = sequence[index - 1]+sequence[index-2]
        if(add > n):
            return False
        sequence.append(add)
        index = index + 1

    return True


def fibonacci():
    pass


def main():
    n = int(input())
    print(fibonacci_sequence(n))

if __name__ == "__main__":
    main()

