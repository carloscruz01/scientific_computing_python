def loop():
    historico = []
    condicao = True
    while condicao:
        mensagem = str(input('Insira sua mensagem:'))
        if mensagem != '':
            historico.append(mensagem)
        elif mensagem == '':
            condicao = False
            print(historico)
        else:
            print('Traceback, line 4.')
loop()     