# Desafio 040 - Crie um programa que leia duos notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input('Informe a nota do primeiro bimestre: '))
n2 = float(input('Informe a nota do segundo bimestre: '))
n3 = float(input('Informe a nota do terceiro bimestre: '))
n4 = float(input('Informe a nota do quarto bimestre: '))
m = (n1 + n2 + n3 + n4)/4
if m < 5.0:
    print('Sua média no ano foi de {:.1f}. Você foi REPROVADO.'.format(m))
elif 5 < m < 7:
    print('Sua média no ano foi de {:.1f}. Você está em RECUPERAÇÃO.'.format(m))
else:
    print('Sua média no ano foi de {:.1f}. PARABÉNS, VOCÊ ESTÁ APROVADO!!!'.format(m))
