def count_positives_sum_negatives(arr):
    cont_pos = soma_neg = cont_0 = 0
    lista_soma_nums_neg_e_pos = []
    if arr:
        for num in arr:
            if num == 0:
                cont_0 += 1
            if num == 0 and cont_0 == len(arr):
                cont_pos = 0
            elif abs(num) == num and num != 0:
                cont_pos += 1
            else:
                soma_neg += num
        lista_soma_nums_neg_e_pos.append(cont_pos)
        lista_soma_nums_neg_e_pos.append(soma_neg)
        return lista_soma_nums_neg_e_pos
    else:
        return lista_soma_nums_neg_e_pos


print(count_positives_sum_negatives([]))
