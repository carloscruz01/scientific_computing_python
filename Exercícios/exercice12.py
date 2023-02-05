import json
caminho_arquivo = 'personagens.json'
criaturas = []
def ler_arquivo():
    with open('personagens.json') as arquivo:
        criaturas = json.load(arquivo)
    return criaturas