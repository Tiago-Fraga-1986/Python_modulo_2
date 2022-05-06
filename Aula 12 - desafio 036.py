# Desafio 036 - Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa cai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai
# pagar. Calcule o valor da prestação mensal, sendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.
c = float(input('Qual o valor do imóvel? R$'))
s = float(input('Informe o seu salário: R$'))
t = int(input('Informe em anos qual será o período de pagamento: '))
p = t*12
e = c/p
if e < (s*0.3):
    print('O seu empréstimo no valor de R${:.2f} será debitado em {} parcelas no valor de R${:.2f}. Seu crédito foi '
          'aprovado.'.format(c, p, e))
else:
    print('O empréstimo no valor de R${:.2f} ficaria em {} parcelas de R${:.2f}. \n '
          'Seu crédito não foi aprovado pois a parcela ultrapassa 30% do seu salário. \n'
          .format(c, p, e))
    print('Dentro do seu salário, a parcela máxima seria de R${:.2f}. \n'
          'Para saldar o crédito, você precisaria de um período de {:.0f} anos.'.format(s*0.3, (c/(s*0.3))/12))
