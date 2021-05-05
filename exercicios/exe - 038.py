#entrada dos dados
num = input(' Digite o primeiro número - ').strip()
num2 = input(' Digite o segundo número - ').strip()

#analise dos dados
ana = num.isnumeric()
ana2 = num2.isnumeric()

#validação dos dados
while ana == False or ana2 == False:
    print ('#####Por Favor Digite Apenas números#######')
    num = input(' Digite o primeiro número - ').strip()
    num2 = input(' Digite o segundo número - ').strip()
    ana = num.isnumeric()
    ana2 = num2.isnumeric()

# comparação e resultado dos dados
if num > num2:
    print (' O Primeiro numero {} é maior que o Segundo número {}'.format(num, num2))

elif num2 > num:
    print(' O segundo numero {} é maior que o primeiro número {}'.format(num2, num))

else:
    print(' Os numeros {} é {} São Iguais'.format(num, num2))

