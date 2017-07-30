print('desafio005')
x=int(input('digite um número inteiro mané:'))
a=x-1
s=x+1
print('o antecessor é: {} \no sucessor é: {}'.format(a, s))
print('Você já viu calcular uma média entre duas coisas que não são números, sua anta??? digita um número seu burro.')

print('\ndesafio006')
d=x*2
t=x*3
r=x**1/2
print('o dobro é: {} \no triplo é: {} \na raiz2 é: {}\n'.format(d,t,r))

print('\ndesafio007')
nota1=float(input('qual é a nota 1?'))
nota2=float(input('qual é a nota 1?'))
m=(nota1+nota2)/2
print('a sua média é:',m)
if m<7:
    print('reprovado mané')
else:
    print('PAAASSOUUUUU... na cagada heim!!! Tu é burrão...')

print('\ndesafio008')
c=m*100
mili=m*1000
print('peguei sua nota e transformei em centímetros:',c)
print('agora eu transformei em milímetros:',mili)
print('viu como eu sou foda?????!!!')

print('\ndesafio009')
print('tabuada de',x)
t1=x*1
t2=x*2
t3=x*3
t4=x*4
t5=x*5
t6=x*6
t7=x*7
t8=x*8
t9=x*9
t10=x*10
print('1*{}={}\n2*{}={}\n3*{}={}\n4*{}={}\n5*{}={}\n6*{}={}\n7*{}={}\n8*{}={}\n9*{}={}\n10*{}={}'.format(x,t1,x,t2,x,t3,x,t4,x,t5,x,t6,x,t7,x,t8,x,t9,x,t10))
print('o Python sabe fazer tabuada, Guanabara')

print('\ndesafio010')
reais=int(input('Quantos reais você tem agora consigo mané??? Me diz aí para eu ver uma paradinha...'))
dollars=reais/3.27
print('Lek, dá pra comprar', dollars,'dólares com o que tu tem aí')

print('\ndesafio011')
l=float(input('qual é altura da parede?'))
h=float(input('qual é a largura da parede?'))
area=l*h
tinta=area/2
print('cara, tu vais precisar de {} litros de tinta'.format(tinta))

print('\ndesafio012')
preco=float(input('qual é o preço do produto'))
desconto=preco*0.05
precofinal=preco-desconto
print('o desconto foi de {}, e o que você vai pagar é {}'.format(desconto,precofinal))

print('\ndesafio013')
salario=float(input('qual é o salário?'))
aumento=salario*0.15
salarionovo=salario+aumento
print('o seu novo salário é {}, parabéns'.format(salarionovo))
