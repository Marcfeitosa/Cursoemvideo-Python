nome = str(input('Qual é o seu nome? '))
if nome == 'Márcio':
    print('Seu nome é Normal')
else:
    print('Seu nome também é Normal, não se preocupe.')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
m = (n1 + n2) / 2
print('Parabéns.' if m >= 7.0 else 'Estude Mais.')
# if m >= 7.0:
# print('Sua média foi boa! Parabéns!')
# else:
# print('Estude mais.')

from random import choice

print("""Desafio 028
Escreva um programa que faça o computador em um número inteiro entre 0 e 5 e 
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador:

O programa deverá escrever na tela se o usuário venceu ou perdeu.""")

print('Eu vou pensar em um número entre 0 e 5, você consegue descobrir qual é o número?')
cpu = [0, 1, 2, 3, 4, 5]
m = choice(cpu)
tu = int(input('Digite o número no qual eu pensei: '))
print('Parabéns, você acertou.' if m == tu else 'você errou meu camarada, o número que eu escolhi é o {}.'.format(m))

print("""Desafio 029
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.""")

vel = float(input('qual é a velocidade do carro? '))
print('Multado, a multa vai custar {}'.format((vel - 80.00) * 7) if vel > 80.00 else 'continue assim.')

print("""Desafio 30
Escreva um programa que diga se um número é par ou impar""")
x = float(input('Escreva um número: '))
if x % 2 != 0:
    print('Número impar')
else:
    print('Número par')

print("""Desafio 31
Escreva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando
R$ 0,50 por KM para viagens de até 200Km e R$ 0,45 para viagens mais longas.""")
dist = float(input('Qual é a distância a ser percorrida? '))
if dist > 200:
    print('O preço da passagem será de R${:2f}.'.format(float(dist * 0.45)))
else:
    print("O preço da passagem será de R${:2f}.".format(float(dist * 0.50)))

print("""Desafio 32
Faça um programa que leia um ano qualquer e diga se ele é bissexto ou não""")
ano = int(input('Digite um ano qualquer: '))
if (ano%2) > 0:
    print('O ano não é bissexto')
else:
    print('O ano é bissexto')

print("""Desafio 33
Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor""")
f = int(input('Digite o primeiro número: '))
g = int(input('Digite o segundo número: '))
h = int(input('Digite o terceiro número: '))
list_sort = [f, g, h].
print('O menor número é {}.'.format(list_sort(min())))
print('O maior número é {}.'.format(list_sort(max())))

print("""Desafio 34
Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.200,00 calcule um aumento de 10%.
Para salários inferiores ou iguais, o aumento é de 15%""")
sal = float(input('Qual é o seu salário? '))
if sal > 1200.00:
    print('Parabéns, ganhou um aumento de 15%, o seu novo salário é de {}.'.format(sal*1.15))
else:
    print('Parabéns, ganhou um aumento de 10%, o seu novo salário é de {}.'.format(sal*1.10))

print("""Desafio 35
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo""")
r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))
if (r2 - r3) < r1 < (r2 + r3):
    print('As medidas formam um triângulo')
elif (r1 - r3) < r2 < (r1 + r3):
    print('As medidas formam um triângulo')
elif (r1 - r2) < r3 < (r1 + r2):
    print('As medidas formam um triângulo')
else:
    print('As medidas não formam um triângulo')

