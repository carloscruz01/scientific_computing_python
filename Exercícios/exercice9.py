fruit = "banana"
x = fruit[1]
print(x)
#1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Hello World!")

#2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
n = int(input('Entre com um número:'))
print("O número informado foi:", n)

#3 - Faça um Programa que peça dois números e imprima a soma.
def somar():
    n1 = int(input("Entre com um número:"))
    n2 = int(input("Entre com outro número:"))
    soma = n1 + n2
    print('Resultado:', soma)
somar()

def nota_escolar():
    nota1 = int(input('Entre com a nota do primeiro bimestre:'))
    nota2 = int(input('Entre com a nota do segundo bimestre:'))
    nota3 = int(input('Entre com a nota do terceiro bimestre:'))
    if nota1 >= 0 and nota2 >= 0 and nota3 >= 0:
        media = (nota1 + nota2 + nota3) / 3
        print('A média alcançada ao longo dos três bimestres foram:', media)
    else:
        print("Por favor, digite um número.")
nota_escolar()

