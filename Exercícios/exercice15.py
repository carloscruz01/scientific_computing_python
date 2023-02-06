def desv_condi3():
    while True:
        a = int(input('Entre com um número:'))
        if a == 0:
            print('Você ganhou 4x', 'Ganhou:', 4*a)
            break
        elif a >= 3:
            print('Você ganhou 2x', 'Ganhou:', 2*a)
            break
        elif a == 1:
            print('Você ganhou 3x', 'Ganhou:', 3*a)
            break
        else:
            print('Você não obtêve nenhum ganhou.')
