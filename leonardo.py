def leonardo(numb):
    if numb < 0:
        raise ValueError
    if numb <= 1:
        return 1
    else:
        return leonardo(numb - 1) + leonardo(numb - 2) + 1


if __name__ == '__main__':
    print(leonardo(3))
