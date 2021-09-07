def highest_rank(arr):
    lista_cont_num = []
    lista_nums = []
    cont = 0
    for num in arr:
        lista_cont_num.append(str(arr.count(num)))
    maior_num = max(lista_cont_num)
    for i in range(len(lista_cont_num)):
        if lista_cont_num[i] == maior_num:
            lista_nums.append(arr[i])
    return max(lista_nums)


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))
