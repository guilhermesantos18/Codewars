def highest_rank(arr):
    lista_cont_num = []
    lista_nums = []
    cont = 0
    for num in arr:
        lista_cont_num.append(str(arr.count(num)))
    maior_num = max(lista_cont_num)
    for i in lista_cont_num:
        if i == maior_num:
            print(i)
            lista_nums.append(arr[lista_cont_num.index(i) + cont])
            cont += 1
    return max(lista_nums)


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))
