def get_order(order):
    comida = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'milkshake', 'coke', 'onionrings']
    lista_pos = []
    for i in comida:
        if i in order:
            lista_pos.append(order.find(i))
    print(lista_pos)


get_order('milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza')
