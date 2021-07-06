def diamond(n):
    expected = ''
    if n % 2 == 0 or n <= 0:
        return None
    elif n % 2 == 1:
        for num in range(1, n + 1, 2):
            print(num)
            expected += str('*'*num).center(n)
            if num >= 3:
                expected += str('*'*num).center(n)
        return expected


print(diamond(3))
