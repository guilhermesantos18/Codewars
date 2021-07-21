def high(x):
    abecedario_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    var = []
    x = x.split()
    for palavra in x:
        soma_pos_letras = 0
        for letra in palavra:
            if letra in abecedario_minusculas:
                soma_pos_letras += abecedario_minusculas.index(letra) + 1
        var.append(soma_pos_letras)
    maior_num = max(var)
    return x[var.index(maior_num)]


print(high('man i need a taxi up to ubud'))
