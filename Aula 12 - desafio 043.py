# Desafio 043 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: ABAIXO DO PESO
# - Entre 18.5 e 25: PESO IDEAL
# - 25 a 30: SOBREPESO
# - 30 a 40: OBESIDADE
# - Acima de 40: OBESIDADE MORBIDA.
p = float(input('informe o seu peso (Kg): '))
a = float(input('informe a sua altura (M): '))
imc = p / (a ** 2)
if imc < 18.4:
    print('Seu IMC é {:.1f}. Você está abaixo do peso.'.format(imc))
elif 18.5 < imc < 24.9:
    print('Seu IMC é {:.1f}. Você está dentro do peso ideal. Parabéns!'.format(imc))
elif 25 < imc < 29.9:
    print('Seu IMC é {:.1f}. Você está com sobrepeso. Atenção.'.format(imc))
elif 30 < imc < 39.9:
    print('Seu IMC é {:.1f}. Você está OBESO. PROCURE AUXÍLIO PROFISSIONAL.'.format(imc))
else:
    print('Seu IMC é {:.1f}. Você está em obesidade mórbida. PROCURE AUXÍLIO PROFISSIONAL IMEDIATAMENTE!'.format(imc))
