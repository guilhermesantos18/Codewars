def comp(matriz1, matriz2):
    cont = 0
    if str(matriz1[-1]**2) in str(matriz2[0]):
        cont += 1
    for pos in range(0, len(matriz1) - 1):
        if str(matriz1[pos]**2) in matriz2:
            cont += 1
    print(cont)
    if cont == len(matriz2):
        return True
    else:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))
