def is_valid_walk(walk):
    lista_pos_n = lista_pos_s = lista_pos_w = lista_pos_e = []
    ida_destino = walk
    voltar_onde_partiu = []
    entrou = False
    # Consegue ir para o destino em 10 min
    if len(ida_destino) == 10:
        # Consegue voltar de onde partiu
        for sentido in range(len(ida_destino)-1, -1, -1):
            voltar_onde_partiu.append(ida_destino[sentido])
        for pos in range(0, len(ida_destino)):
            if ida_destino[pos] == 'n':
                lista_pos_n.append(pos)
            elif ida_destino[pos] == 's':
                lista_pos_s.append(pos)
            elif ida_destino[pos] == 'w':
                lista_pos_w.append(pos)
            elif ida_destino[pos] == 'e':
                lista_pos_e.append(pos)
    print(lista_pos_n)
    print(lista_pos_s)
    print(ida_destino)
    print(voltar_onde_partiu)
    # else:
    #     return False


is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])
