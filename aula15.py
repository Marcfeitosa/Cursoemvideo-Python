n = s = c = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é {s}.')

"""Desafio 066
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre qantos números foram digitados e qual foi a soma entre eles.
(desconsiderando o Flag)"""

"""Desafio 067

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitados for negativo."""

"""Desafio 068

Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

"""Desafio 069

Crie um program que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o
usuário quer ou não continuar. No final mostre:

A) quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos."""

"""Desafio 070

Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000,00
C) Qual é o nome do produto mais barato."""

"""Desafio 071

Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas células de cada valor serão entregues.

Obs. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""
