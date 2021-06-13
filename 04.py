def xo(s):
    cont_x = cont_o = 0
    for letra in s:
        if letra == 'x' or letra == 'X':
            cont_x += 1
        elif letra == 'o' or letra == 'O':
            cont_o += 1
    if cont_x == cont_o:
        return True
    else:
        return False


print(xo('ooxx'))
print(xo('xooxx'))
print(xo('ooxXm'))
print(xo('zpzpzpp'))
print(xo('zzoo'))