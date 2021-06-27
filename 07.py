cont = 0


def is_valid_walk(walk):
    lista_pos_sentidos = []
    ida_destino = walk
    voltar_onde_partiu = []
    global cont
    # Consegue ir para o destino em 10 min
    if len(ida_destino) == 10:
        # Consegue voltar de onde partiu
        for sentido in range(len(ida_destino) - 1, -1, -1):
            voltar_onde_partiu.append(ida_destino[sentido])
        for pos in range(0, len(ida_destino)):
            if ida_destino[pos] == 's' or 'n' or 'w' or 'e':
                lista_pos_sentidos.append(pos)
        # print(ida_destino)
        # print(voltar_onde_partiu)
        for sentido in lista_pos_sentidos:
            if ida_destino[sentido] == 'n' and voltar_onde_partiu[sentido] == 's':
                cont += 1
            elif ida_destino[sentido] == 's' and voltar_onde_partiu[sentido] == 'n':
                cont += 1
            elif ida_destino[sentido] == 'w' and voltar_onde_partiu[sentido] == 'e':
                cont += 1
            elif ida_destino[sentido] == 'e' and voltar_onde_partiu[sentido] == 'w':
                cont += 1
        # Se o cont for igual ao comprimento da lista quer dizer que todas as posições estão corretas
        if cont == len(voltar_onde_partiu):
            return True
        else:
            return False
    else:
        return False


print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
