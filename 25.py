lista_primos = []


def step(g, m, n):
    global lista_primos
    lista_primos_g = []
    for num in range(m, n):
        e_primo(num)
    if lista_primos:
        for num in lista_primos:
            if num + g in lista_primos:
                lista_primos_g.append(num)
                lista_primos_g.append(num + g)
            if len(lista_primos_g) == 2:
                break
        return lista_primos_g
    else:
        return None


def e_primo(num):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        lista_primos.append(num)


print(step(6, 100, 110))
