def find(n):
    res = 0
    for i in range(3, n+1):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res
