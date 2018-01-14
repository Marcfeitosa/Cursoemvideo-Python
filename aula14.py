c = 1
while c < 10:
    print(c)
    c = c + 1
    print("C'est la fin")

c = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('VocÊ digitou {} numeros pares e {} números ímpares!'.format(par, impar))

print("""Desafio 057
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.""")

print("""Desafio 058
Melhore o jogo do DESAFIO 028 onde o computador vai pensar em um número de 0 a 10. Sò que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer""")

print("""DESAGIO 059
Crie um program aque cria dois valores e coloque o menu na tela:

[1]SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA

Seu programa deverá deverá realizar a operação solicitada em cada caso.""")

print("""DESAFIO 060
Faça um programa que leia um núemro qualquer e mostre o seu fatorial

Ex:
5! = 5x4x3x2x1=120""")

print("""DESAFIO 61

Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
progressão usando a estrutura while""")

print("""DESAFIO 62

Melhore o desafio 61, pergunte para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.""")

print("""DESAFIO 63

Escreva um programa que leia um numro n inteiro qualquer e mostre na tela os n primeiros elementos de uma
seqüência de Fibonacci.

Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8""")

print("""DESAFIO 64

Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
a soma entre eles(desconsiderando o flag '999')""")

print("""DESAFIO 065

Crie um programa que leia varios números inteiros no teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.""")