# Desafio 041 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
# atleta e mostre a sua categoria, de acordo com a idade:
# - até 9 anos: MIRIN
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 25 anos: Senior
# - acima disso: MASTER
from datetime import date
i = int(input('Informe o ano de seu nascimento: '))
t = date.today()
c = t.year - i
if c <= 9:
    print('Você possui {} anos e será classificado na categoria Mirim.'.format(c))
elif c <= 14:
    print('Você possui {} anos e será classificado na categoria Infantil.'.format(c))
elif c <= 19:
    print('Você possui {} anos e será classificado na categoria Júnior.'.format(c))
elif c <= 25:
    print('Você possui {} anos e será classificado na categoria Senior.'.format(c))
else:
    print('Você possui {} anos e será classificado na categoria Master.'.format(c))
