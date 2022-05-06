"""Desafio 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal.
Obs: Ao se usar os conversores dentro do format, fica um "prefixo" antes da sequência pretendida. desta forma,
uma forma mais fácil de fazer a conversão é utilizar a formatação dentro das chaves do format, desta forma:
print('{} em BINÁRIO é {:b}'.format(num, num))
a opção :b dentro das {} exibe o valor da variável num já convertido em binário, sem o 0b no início.
:b - binário
:o - octal
:x - hexadecimal com letras minúsculas
:X - hexadecimal com letras maiúsculas
OBS2: Poderíamos usar também o fatiamento da str, porém, essa solução não permitiria a conversão de números negativos,
além de, no caso do número a ser convertido ser negativo, ficaria um dos caracteres do "prefixo" no print."""


# from time import sleep
print('=-=' * 10 + ' Conversor Numérico ' + '=-=' * 10)
n = int(input('Informe um número decimal para conversão: '))
o = int(input('Qual será a base para conversão? Informe:\n'
              '[1] - Para Binário;\n'
              '[2] - Para Octal; \n'
              '[3] - Para Hexadecimal.\n'
              'Sua base: '))
print('Estamos calculando o seu resultado...')
# sleep(2)
if o == 1:
    print('O número decimal {} convertido para Binário fica {:b}.'.format(n, n))
elif o == 2:
    print('O número decimal {} convertido para Octal fica {:o}.'.format(n, n))
elif o == 3:
    print('O número decimal {} convertido para Hexadecimal fica {:x}.'.format(n, n))
else:
    print('OPÇÃO INVÁLIDA. REINICIE O PROGRAMA.')
