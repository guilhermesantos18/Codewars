def step(g, m, n):
    lista = []
    seg = cont = 0
    for num in range(m, n + 1):
        if cont == 0:
            if num % g == float:
                seg = num + g
                cont += 1
        if seg % 2 == float:
            lista.append(num)
            lista.append(seg)
        else:
            continue


step(2,100,110)
