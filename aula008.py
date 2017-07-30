import math, random, emoji

num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {:.2f} é igual a {:.2f}".format(num, raiz))

def arrend(numero):
    if num2 - math.floor(num2) < 0.5:
        numero = math.floor(num2)
        return numero
    else: return math.ceil(num2)
num2 = float(input("digite um número não inteiro: "))
print("o número inteiro correspondente é: {}".format(arrend(num2)))

catetooposto = float(input('qual é o comprimento do cateto oposto: '))
catetoadjacente = float(input('qual é o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetooposto, catetoadjacente)
print("a hipotenusa é igual à {}.".format(math.sqrt((catetooposto ** 2) + (catetoadjacente ** 2))))
print('tirando a prova dos nova com a Hipotenusa: {}'.format(hipotenusa))

h = float(input('Digite um ângulo: '))
sen = math.sin(h)
cos = math.cos(h)
tang = math.tan(h)
print("O seno do ângulo {:.2f} é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}".format(h,sen,cos,tang))

#fazer com que o Python escolhe um aluno da lista
elementolist = random.randint(0, 3)
listalunos = ["Vivian","Arthur","Eu","Gucci"]
print('Escolher o aluno que vai apagar o quadro. O Python escolheu o aluno {}'.format(listalunos[elementolist]))
listatrabalhos = random.sample(listalunos, 4)
print("Escolher a lista de alunos para apresentação de trabalho: {}".format(listatrabalhos))

print(emoji.emojize('Python é, :rugby_football:'))