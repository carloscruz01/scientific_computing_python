def padroes():
    condicao = True
    while condicao:
        padrao = 0
        for c in [10, 24, 34, 44, 54, 64, 74]:
            padrao = (padrao+1)
            print('Padrão:', padrao, 'Loop:', c)
        print('Padrão:', padrao)
        break
padroes()
