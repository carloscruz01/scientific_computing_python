def contagem():
    palavra = 'universo'
    cont = 0
    for i in palavra:
        if i == 'u':
            cont = cont + 1
    print('Quantidade de consoante/vogal:', cont)
    palavra = 'controle de versao'
    cont = 0
    for u in palavra:
        if u == 'o':
            cont = cont + 1
    print('Quantidade de consoante/vogal:', cont)
    numero = [0, 1, 0, 1, 0, 0, 1]
    cont = 0
    for c in numero:
        if c in numero:
            cont = cont + 1
    print('Quantidade de elementos na lista:', cont)
contagem()