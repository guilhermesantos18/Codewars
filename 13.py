def diamond(n):
    if n % 2 == 0 or n <= 0:
        return None
    elif n % 2 == 1:
        for num in range(1, n + 1, 2):
            expected = str('*'*num).center(n)
            print(expected)
        for num in range(n-2, 0, -2):
            expected = str('*'*num).center(n)
            print(expected)


diamond(63)
