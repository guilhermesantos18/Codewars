def solution(number):
    lista_num = []
    for num in range(number - 1, 0, -1):
        if num % 3 == 0:
            lista_num.append(num)
        if num % 5 == 0:
            lista_num.append(num)
            if lista_num.count(num) >= 2:
                lista_num.remove(num)
    return sum(lista_num)


print(solution(6))
