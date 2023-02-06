def repeti_fo():
    print('Hello World!')
    lista_alimentos = ['Biscoito', 'Chá Matte', 'Pães', 'verduras']
    for i in range(4):
        print(lista_alimentos)
    for i in lista_alimentos:
        print(lista_alimentos[0:4])
    for i, lista in enumerate(lista_alimentos):
        print(lista)
repeti_fo()