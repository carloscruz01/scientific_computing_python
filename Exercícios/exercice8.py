caracteristicas = []
condicao = True
while condicao: 
    name_contrat = str(input('Insira o nome do contratante:'))
    if name_contrat > '':
        tipo_conta = str(input('Insira o tipo de conta:'))
        banco = str(input('Insira o nome do banco'))
        numeracao_conta = int(input('Numeração da conta:'))
        infos_user = {
            "Nome_do_contratante": name_contrat,
            "Tipo_de_conta": tipo_conta,
            "Banco": banco,
            "Numero_da_conta": numeracao_conta
        }
        caracteristicas.append(infos_user)
        for infos_user in caracteristicas:
            print(str('Nome do contratante:', caracteristicas['Nome_do_contratante']))
            print('Tipo de conta:', caracteristicas['Tipo_de_conta'])
            print('Banco:', caracteristicas['Banco'])
            print('Numero da conta', caracteristicas['Numero_da_conta'])
    break
        