#Crie um programa que leia um número Real qualquer
#pelo teclado e mostre na tela a sua porção inteira
from math import floor
def software_inters():
    condicao = True
    while condicao:
        n = float(input('Entre com um número:'))
        if n != '':
            n_int = floor(n)
            print('O número real {} tem a parte inteira {}'.format(n, n_int))
            break
software_inters()