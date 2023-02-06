def desv_condi4():
    listacao_alimentos = ['Biscoito Negresco', 'Carne Bovina', 'Pães', 'Feijão Branco']
    listei = [listacao_alimentos, 'Hello World!', 5, True, 4.6, False]
    for i in range(5):
        print(listacao_alimentos)
    for i in range(4, 9):
        print(listacao_alimentos)
    for i in range(10, 3, -1):
        print(listacao_alimentos)
    for i, item in enumerate(listacao_alimentos):
        print(i, item)
desv_condi4()