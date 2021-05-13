from time import sleep
from random import randint
from sys import exit
print ('{:=^40}'.format(' PEDRA / PAPEL / TESOURA'))
jogador = input('Digite seu Nome Jogador: ')
opc = int(input('''Escolha a sua opção - 
[ 0 ] - PEDRA.
[ 1 ] - PAPEL.
[ 2 ] - TESOURA.
[ 3 ] - Sair do Jogo
Sua Opção -  '''))


#validação da opção com retorno ao menu
while opc > 3:
    print ('####### FAÇA A SUA JOGADA ######')
    opc = int(input('''Escolha a sua opção - 
[ 0 ] - PEDRA.
[ 1 ] - PAPEL.
[ 2 ] - TESOURA.
[ 3 ] - Sair do Jogo
    Sua Opção -  '''))
if opc == 3:
    print('Saindo do Jogo...............')
    sleep(1)
    print ('+++++++ FIM DE JOGO ++++++++++')
    exit()


lista = ('PEDRA', 'PAPEL', 'TESOURA')
jogada = randint(0, 2)

print ('JO')
sleep(1)
print ('KEN')
sleep (1)
print ('PÔ')
sleep(1)

print ('VOCÊ ESCOLHEU \33[1;30;41m{}\33[m '.format(lista[opc]))
print ('E O COMPUTADOR ESCOLHEU \33[1;31;40m{}\33[m'.format(lista[jogada]))

if opc == jogada:
    print ('DEU EMPATE')
elif opc == 0 and jogada ==1:
    print ('VOCÊ PERDEU EU SOU O MAIOR - TENTE NOVAMENTE')
elif opc == 0 and jogada == 2 :
    print ('VOCÊ VENCEU PARABÉNS')
elif opc == 1 and jogada == 2 :
    print ('VOCÊ PERDEU EU SOU O MAIOR - TENTE NOVAMENTE')
elif opc == 1 and jogada == 0 :
    print ('VOCÊ {} VENCEU PARABÉNS'.format(jogador))
elif opc == 2 and jogada == 0 :
    print ('VOCÊ PERDEU EU SOU O MAIOR - TENTE NOVAMENTE')
elif opc == 2 and jogada == 1 :
    print ('VOCÊ VENCEU {} PARABÉNS'.format(jogador))
