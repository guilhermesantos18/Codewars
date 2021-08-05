def expanded_form(num):
    num = str(num)
    x = len(num) - 1
    res = []
    for n in range(0, len(num) - 1):
        if num[n] != str(0):
            forma_expandida = num[n]
            forma_expandida += str(0)*x
            res.append(int(forma_expandida))
            x -= 1
        else:
            x -= 1
    if num[-1] != str(0):
        res.append(int(num[-1]))
    res = str(res)
    res = res.replace(',', ' +')
    res = res.replace(']', '')
    res = res.replace('[', '')
    return res


print(expanded_form(1532))
