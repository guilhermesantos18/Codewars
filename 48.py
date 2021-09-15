def persistence(n):
    n = str(n)
    cont = 0
    while len(n) != 1:
        mult_nums = int(n[0])
        for num in n[1:]:
            mult_nums *= int(num)
        n = str(mult_nums)
        cont += 1
    return cont


print(persistence(25))
