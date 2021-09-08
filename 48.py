def persistence(n):
    n = str(n)
    mult_nums = cont = 0
    while len(n) != 1:
        for num in n:
            print(num)
#     n = str(mult_nums)
#     cont += 1
    # return cont


print(persistence(39))
