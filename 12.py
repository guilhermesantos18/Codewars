def alphabet_position(text):
    abecedario_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'w', 'x', 'y', 'z']
    abecedario_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
    var = []
    for letra in text:
        if letra in abecedario_maiusculas:
            var.append(abecedario_maiusculas.index(letra) + 1)
        elif letra in abecedario_minusculas:
            var.append(abecedario_minusculas.index(letra) + 1)
    return str(var)


print(alphabet_position('The sunset sets at twelve o clock.'))
