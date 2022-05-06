# Desafio 044 - Elabore um programa que calcule o valor a ser pago por um produto,
# consideration o seu preço normal e a condição de pagamento:
# - A vista (Débito): 10% de desconto
# - Cartão de crédito 1x: 5% de desconto
# - Cartão de crédito 2x: Sem juros
# - Cartão de crédito 3x: 20% de juros.
p = float(input('Informe o preço do produto: R$'))
cond = int(input('''informe a condição de pagamento:
                 [ 0 ] - Débito (10% DE DESCONTO)
                 [ 1 ] - Crédito a vista (5% DE DESCONTO)
                 [ 2 ] - Crédito 2x SEM JUROS
                 [ 3 ] - 3x ou mais no crédito (JUROS DE 20% AO MÊS)
                 Condição: '''))
if cond == 0:
    print('Você ganhou 10% de desconto. O valor final ficou em R${:.2f}.'.format(p-(p*0.1)))
elif cond == 1:
    print('Você ganhou 5% de desconto. O valor final ficou em R${:.2f}.'.format(p-(p*0.05)))
elif cond == 2:
    print('O valor do produto ficou em R${:.2f}, parcelados em 2x de R${:.2f} sem juros.'.format(p, p / 2))
elif cond == 3:
    v = int(input('Informe o número de parcelas: '))
    print('O valor do produto ficou em R${:.2f}, parcelados em {} parcelas de R${:.2f}.'.format((p * 0.2) + p, v,
                                                                                                ((p * 0.2) + p) / v))
else:
    print('OPÇÃO INVÁLIDA. REINICIE O PROGRAMA.')
