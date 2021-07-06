def alphabet_position(text):
    abecedario_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    abecedario_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    var = []
    for letra in text:
        if letra in abecedario_maiusculas:
            var.append(abecedario_maiusculas.index(letra) + 1)
        elif letra in abecedario_minusculas:
            var.append(abecedario_minusculas.index(letra) + 1)
    var = str(var)
    var = var.replace(',', '')
    var = var.replace(']', '')
    var = var.replace('[', '')
    return f"'{var}'"


print(alphabet_position("The sunset sets at twelve o' clock."))
