#entrada do numero e escolha da opção
from time import sleep
num = int(input('entre com um número para a conversão - '))
opc = int(input('''\33[1;30;41m###### entre com a opção Dejesada #######\33[m - 
[ 0 ] - Sair do programa
[ 1 ] - Binário -
[ 2 ] - Octal -
[ 3 ] - hexadec - 
Sua Opção -  '''))

#validação da opção com retorno ao menu
while opc >= 4:
    print ('\33[1;31;40m    OPÇÃO INVÁLIDA     \33[m')
    opc = int(input('''\33[1;;30;41m#####entre com a opção Dejesada###### \33[m - 
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
    print ('o numero {} em binário é  - {}'.format (num, bin(num)[2:]))
if opc == 2:
    print ('o número {} em octal é -  {}'.format(num, oct(num)[2:]))
if opc == 3:
    print('o número {} em HEXADECIMAL é -  {}'.format(num, hex(num)[2:]))

