#Entendendo um Algoritmo e um Programa
    #Um algoritmo é uma sequência finita de passos. Podendo produzir uma entrada e uma saída.
    #O programa é algo que possui um algoritmo e é executado pela máquina.
#Aritmética básica; Tipos de Dados e Operadores.

#Desvios Condicionais
def desv_condi():
    a = int(input('Entre com um número:'))
    if a == 1:
        print('É um binário')
    elif a == 0:
        print('É um binário')
    else:
        print('Não é um binário')

def desv_condi2():
    y = 1 + 2
    x = input('Tente advinhar qual o número que irá aparecer:')
    if y == x:
        print("Parabéns, você advinhou!")
    else:
        print("Você não acertou, que tal tentar mais uma vez?")

