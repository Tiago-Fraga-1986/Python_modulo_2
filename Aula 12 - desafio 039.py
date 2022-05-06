# Desafio 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de
# acordo com sua idade:
# - Se ele ainda vai de alistar no serviço militar;
# - Se é a hora de se alistar;
# - Se já passou do tempo de alistamento.
# Seu programa também deve mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nasc = int(input('Informe o seu ano de nascimento: '))
h = date.today()
y = h.year
sm = y - nasc
if sm == 18:
    v1 = str(input('Você já efetuou o seu alistamento? Digite "S" para "sim" e "N" para "não": ').lower().strip())
    if v1 == 's':
        print('A Nação agradece seu empenho!')
    elif v1 == 'n':
        print('Você que completa 18 anos neste ano, ALISTE-SE NO SERVIÇO MILITAR!')
if sm < 17:
    print('Ainda faltam {} anos para o seu alistamento militar. Seu alistamento será em {}'.format(18 - sm, nasc + 18))
elif sm == 17:
    print('Fique atento: No próximo ano você precisa se alistar.')

elif sm > 18:
    v2 = str(input('Você fez o seu alistamento quando você completou 18 anos? Digite "S" para "sim" e "N" para "não": ')
             .lower().strip())
    if v2 == 's':
        print('A Nação agradece seu empenho!')
    elif v2 == 'n':
        print('Seu bisonho! Você deveria ter feito seu alistamento a {} anos!!!'.format(sm - 18))
