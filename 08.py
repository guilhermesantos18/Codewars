def comp(matriz1, matriz2):
    cont = 0
    if len(matriz1) == 8:
        if str(matriz1[-1]**2) in str(matriz2[0]):
            cont += 1
        for pos in range(0, len(matriz2) - 1):
            if matriz2[pos]**0.5 in matriz1:
                cont += 1
        print(cont)
        if cont == len(matriz2):
            return True
        else:
            return False
    else:
        return False


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a, b))
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))
b1 = [121, 144, 19, 161, 19, 144, 19, 11]
b2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(b1, b2))
c1 = [121, 144, 19, 161, 19, 144, 19, 11]
c2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(c1, c2))
