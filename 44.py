def highest_rank(arr):
    lista_cont_num = []
    lista_num = []
    for num in arr:
        lista_cont_num.append(arr.count(num))


print(highest_rank([12, 10, 8, 8, 14, 14, 14, 14, 2, 4, 10, 12, 10, 10]))
