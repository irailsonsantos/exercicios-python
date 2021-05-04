#entrada do numero e escolha da opção
from time import sleep
num = int(input('entre com um número para a conversão - '))
opc = int(input('''entre com a opção Dejesada - 
[ 0 ] - Sair do programa
[ 1 ] - Binário -
[ 2 ] - Octal -
[ 3 ] - hexadec - 
Sua Opção -  '''))

#validação da opção com retorno ao menu
while opc >= 4:
    print ('escolha opção correta')
    opc = int(input('''entre com a opção Dejesada - 
    0 - Sair do programa
    1 - Binário -
    2 - Octal -
    3 - hexadec - 
    Sua Opção -  '''))
    #lista de conversões de acordo com ao opção
if opc == 0:
    print ('saindo.......')
    sleep(2)
if opc == 1:
    print ('o numero em binário é  - {}'.format (bin(num)[2:]))
if opc == 2:
    print ('o número em octal é -  {}'.format(oct(num)[2:]))
if opc == 3:
    print('o número em octal é -  {}'.format(hex(num)[2:]))

