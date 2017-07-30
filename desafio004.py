x=input('Digita aí mané:')
if x.isnumeric():
    print('isso é um número mané')
else:
    print('não é número..')
#print('isso é alpha?',x.isalpha())
if x.isalpha():
    print('isso é uma letra mané')
else:
    print('não é letra..')
#print('isso é um alpha numérico?',x.isalnum())
if x.isalnum():
    print('isso é alpha-num mané')
else:
    print('não é alpha-num..')
#print('isso é um espaço seu palhaço?',x.isspace())
if x.isspace():
    print('isso é um espaço seu palhaço?')
else:
    print('não é espaço...')
#print('isso é um dígito?',x.isdigit())
if x.isdigit():
    print('isso é um dígito mané')
else:
    print('não é dígito...')
#print('isso é caixa baixa?',x.islower())
if x.islower():
    print('isso é um minúsculo mané')
else:
    print('não é minúsculo...')

if x.isnumeric():
    print('isso é um número mané? SIM')
else:
    print('isso é um número mané? NÃO')