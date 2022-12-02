from datetime import datetime
info_animais = []
declaracao_processo = True
while declaracao_processo:
    nome_animal = str(input('Nome do Animal:'))
    if nome_animal > '':
        especie_animal = str(input('Espécie do Animal:'))
        peso_animal = int(input('Peso do Animal:'))
        data_nascimento_animal = input('Insira a data de nascimento do animal:')
        modificao_data = datetime.strptime(data_nascimento_animal, '%d/%m/%Y')
        
        nome_tutor = str(input('Nome do Tutor:'))
        animal = {
            'nome_do_animal': nome_animal,
            'especie': especie_animal,
            'peso': peso_animal,
            'nome_do_tutor': nome_tutor,
            'data_nascimento_animal': modificao_data
        }
        info_animais.append(animal)
    else:
        declaracao_processo = False
    for animal in info_animais:
        print('__________________')
        print('Nome do Pet:', animal['nome_do_animal'])
        print('Espécie:', animal['especie'])
        print('Peso do Animal:', animal['peso'], 'kg')
        print('Data de Nascimento:', datetime.strftime(animal['data_nascimento_animal'], '%d/%m/%Y'))
        print('Nome do Tutor:', animal['nome_do_tutor'])
        print('__________________')