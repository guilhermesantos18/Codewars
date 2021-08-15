def high_and_low(numbers):
    lista = []
    numbers = numbers.split(' ')
    for numero in numbers:
        numero = int(numero)
        lista.append(numero)
    maior = max(lista)
    menor = min(lista)
    return f'{maior} {menor}'


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
