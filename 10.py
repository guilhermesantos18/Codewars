def count_positives_sum_negatives(arr):
    soma_pos = soma_neg = 0
    lista_soma_nums_neg_e_pos = []
    for num in arr:
        if abs(num) == num:
            soma_pos += num
        lista_soma_nums_neg_e_pos.append(soma_pos)



count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
