def get_order(order):
    comida = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'onionrings', 'milkshake', 'coke']
    lista_comida = []
    for i in comida:
        if i in order:
            cont_comida = order.count(i)
            if cont_comida == 1:
                lista_comida.append(i.capitalize())
            else:
                for f in range(0, cont_comida):
                    lista_comida.append(i.capitalize())
    return ' '.join(lista_comida)


print(get_order('milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza'))
