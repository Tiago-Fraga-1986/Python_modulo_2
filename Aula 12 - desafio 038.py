# Desafio 038 - Escreva um programa que leia dois números inteiros e compare-os, mostrando na
# tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior. Os dois são iguais.
n1 = int(input('Informe a distância percorrida na primeira viagem: '))
n2 = int(input('Informe a distância percorrida na segunda viagem: '))
if n1 > n2:
    print('A primeira distância informada foi de {} e a segunda distância foi de {}. A primeira viagem foi maior.'
          .format(n1, n2))
elif n2 > n1:
    print('A primeira distância informada foi de {} e a segunda distância foi de {}. A segunda viagem foi maior.'
          .format(n1, n2))
else:
    print('A primeira distância informada foi de {} e a segunda distância também foi de {}. '
          'Ambas as distâncias são iguais.'.format(n1, n2))
