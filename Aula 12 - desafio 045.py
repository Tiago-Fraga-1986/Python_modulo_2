# Desafio 045 - Crie um programa que faça o computador jogar Jokenpô com você.
"""
#Programa usando "Choice"
from random import choice
from time import sleep
print('-=-' * 15)
print(' Pedra, Papel e Tesoura - O jogo. ')
print('-=-' * 15)
print('Bem vindo ao jogo Pedra, Papel ou Tesoura!')
vc = str(input('Escolha seu elemento: ').strip().lower())
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')
print('-=-'*15)
if vc == 'pedra' and pc == 'tesoura' or vc == 'papel' and pc == 'pedra' or vc == 'tesoura' and pc == 'papel':
    print('Você escolheu {}.'.format(vc))
    print('O Computador escolheu {}.'.format(pc))
    print('{} ganha de {}.'.format(vc, pc))
    print('-=-'*15)
    print('VOCÊ GANHOU!')
elif pc == 'pedra' and vc == 'tesoura' or pc == 'papel' and vc == 'pedra' or pc == 'tesoura' and vc == 'papel':
    print('Você escolheu {}.'.format(vc))
    print('O Computador escolheu {}.'.format(pc))
    print('{} ganha de {}.'.format(vc, pc))
    print('-=-'*15)
    print('VOCÊ PERDEU!')
elif pc == vc:
    print('Você escolheu {}.'.format(vc))
    print('O Computador também escolheu {}.'.format(pc))
    print('-=-' * 15)
    print('Houve um EMPATE!')
else:
    print('VOCÊ NÃO ESCOLHEU UMA OPÇÃO VÁLIDA.')
    print('-=-'*15)
    print('GAME OVER.')"""

# Programa usando "Randint"
from random import randint
from time import sleep

print('-=-' * 15)
print(' Pedra, Papel e Tesoura - O jogo. ')
print('-=-' * 15)
print('Bem vindo ao jogo Pedra, Papel ou Tesoura! digite:\n'
      '         [ 0 ] Para "Pedra"\n'
      '         [ 1 ] Para "Papel"\n'
      '         [ 2 ] Para "Tesoura"')
vc = int(input('Escolha seu elemento: '))
lista = ['pedra', 'papel', 'tesoura']
pc = randint(0, 2)
sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!')
print('-=-' * 15)
if vc == 0 and pc == 2 or vc == 1 and pc == 0 or vc == 2 and pc == 1:
    print('Você escolheu {}.'.format(lista[vc]))
    print('O Computador escolheu {}.'.format(lista[pc]))
    print('{} ganha de {}.'.format(lista[vc], lista[pc]))
    print('-=-' * 15)
    print('VOCÊ GANHOU!')
elif pc == 0 and vc == 2 or pc == 1 and vc == 0 or pc == 2 and vc == 1:
    print('Você escolheu {}.'.format(lista[vc]))
    print('O Computador escolheu {}.'.format(lista[pc]))
    print('{} ganha de {}.'.format(lista[pc], lista[vc]))
    print('-=-' * 15)
    print('VOCÊ PERDEU!')
elif pc == vc:
    print('Você escolheu {}.'.format(lista[vc]))
    print('O Computador escolheu {}.'.format(lista[pc]))
    print('-=-' * 15)
    print('Houve um EMPATE!')
else:
    print('VOCÊ NÃO ESCOLHEU UMA OPÇÃO VÁLIDA.')
    print('-=-' * 15)
    print('GAME OVER.')
