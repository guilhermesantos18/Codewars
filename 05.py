def summation(num):
    res = 0
    for n in range(num, 0, -1):
        res += n
    return res


print(summation(2))
print(summation(8))
