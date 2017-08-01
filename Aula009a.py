frase = 'Curso em Video Python'
frase2 = '   curso em video python  '

print(frase[0:4])
print(frase[::2])
print(frase[0:15:2])
print(frase.upper())
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase2))
print(len(frase2.strip()))
frase3 = frase.replace('Python','Android')
print(frase3)
print(frase.find('Curso'))
print(frase.split())
dividido = frase3.split()
print(dividido[1])
print(dividido[3][2])

print("""O brasileiro de hoje em dia é aquele sujeito valente que teme olhares e caretas como se fossem balas de canhão, que enfia o rabo entre as pernas à simples ideia de que falem mal dele, que troca a honra e a liberdade por um olhar de simpatia paternal de quem o despreza.” 
- http://kdfrases.com/autor/olavo-de-carvalho""")

print("""DESAFIO DA AULA 09
Desafio 022
Criar um programa que leia o nome  completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome""")

print('Desafio 022')
nome = str(input('Digite o seu nome completo: '))
print(nome.upper())
print(nome.lower())
lista_nome = nome.split()
letras = '-'.join(lista_nome)
print('O seu nome tem {} letras.'.format(len(letras)-letras.count('-')))
print('O seu primeiro nome tem {} letras.'.format(len(lista_nome[0])))

print("""Desafio 023
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
ex: Digite um número: 1834

unidade: 4
dezena:3
centena:8
milhar:1""")


while True:
    x = input( 'Digite um número de 0 a 9999: ' )
    if len(x) > 0 and len(x) <= 4:
        break
    print('Errroooooou')

# 1346
#milhar = x / 1000 # 1
#x -= 1000 * milhar  #346
#centena = x / 100 # 3
#x -= 100 * centena # 46
#dezena = x / 10 # 4
#x -= 10 * dezena # 6
#unidade = x #6

unidades = ['unidade', 'dezena', 'centena', 'milhar']

for i in range(len(x), 0, -1):
    print('{} = {}'.format(unidades[len(x)-i], int( x[i-1] ) ) )


    #x = input('Digite um número de 0 a 9999: ')
    #y = int(x)
#print('unidade = {}'.format(int(x[3])))
#print('dezena = {}'.format(int(x[2])))
#print('centena = {}'.format(int(x[1])))
#print('milhar = {}'.format(int(x[0])))