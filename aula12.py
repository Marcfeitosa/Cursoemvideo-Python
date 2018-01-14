nome = str(input('Qual é o seu nome? '))
if nome == 'Márcio':
    print('Esse nome é meu!!!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':\
        print('Seu nome é muito popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('nome bem feminino')
else:
    print("Seu nome é bem normal")
print('Tenha um bom dia, {}!'.format(nome))

print (3*'===============xx==============xx' + '==============')

print("""Desafio 36

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.""")

housevalue = float(input('Qual e o valor do imovel?'))
salary = float(input('Qual é o seu salário?'))
term = int(input('Em quantos anos você vai pagar?'))/12
parcel = housevalue/term
if (housevalue/term) > salary*0.30:
    print("este financiamento não é possível: ")
else:
    print('O seu financiamento será de {}'.format(parcel))

print (3*'===============xx==============xx' + '==============')

print("""DESAFIO 37

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

-1 para binário
-2 para octal
-3 para hexadecimal""")

print (3*'===============xx==============xx' + '==============')

print("""DESAFIO 38

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais""")

print (3*'===============xx==============xx' + '==============')

print("""Desafio 39

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar (e quanto tempo falta)
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento (quanto tempo passou)

O programa deve mostrar o tempo que falta e tempo que excedeu do alistamento""")

print (3*'===============xx==============xx' + '==============')

print("""DESAFIO 40

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO

- Média entre 5.0 e 6.9:
RECUPERAÇÃO

- Média 7.0 ou superior:
APROVADO""")

print (3*'===============xx==============xx' + '==============')

print("""DESAFIO 41

A confederação nacional de natação precisa de um programa que leia o ano de 
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: Sênior
- Acima: MASTER""")

print (3*'===============xx==============xx' + '==============')

print("""DESAFIO 42

Refaça o DESAFIO 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- EQUILATÉRO: todos os lados iguais

- ISÓSCELES: dois lados iguais

- ESCALENO: todos os lados diferentes""")

print (3*'===============xx==============xx' + '==============')

print("""ESAFIO 043

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcula seu IMC e mostre o seu status, de acordo
com a tabela abaixo:

- Abaixo de 18.5: Abaixo de Peso

- Entre 18.5 e 25: Peso ideal

- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: obesidade mórbida""")

print (3*'===============xx==============xx' + '==============')

print("""DESAFIO 044

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

- À VSITA: dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
""")

print (3*'===============xx==============xx' + '==============')

print("""DESAFIO 045

Crie um programa que faça o computador jogar Jokenpô com você""")