def valid_parentheses(string):
    parenteses_direita = 0
    parenteses_esquerda = 0
    for i in string:
        if i == '(':
            parenteses_direita = string.count(i)
        else:
            parenteses_esquerda = string.count(i)
    if parenteses_esquerda == parenteses_direita:
        return True
    else:
        return False


print(valid_parentheses('())('))

