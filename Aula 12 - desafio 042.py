# Desafio 042 - Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar
# que tipo de triangulo será formado:
# - EQUILÁTERO: Todos os lados iguais;
# - ISÓSCELES: Dois lados iguais;
# - ESCALENO: Todos os lados diferentes.
print('∆'*20)
print('ANALISADOR DE TRIANGULOS')
print('∆'*20)
s1 = float(input('informe o primeiro segmento: '))
s2 = float(input('informe o segundo segmento: '))
s3 = float(input('informe o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 \
        and s1 == s2 and s2 == s3:
    print('Os segmentos informados formam um triangulo EQUILÁTERO.')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 \
        and s1 == s2 or s2 == s3 or s1 == s3:
    print('Os segmentos informados formam um triangulo ISÓSCELES')
elif s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2 \
        and s1 != s2 and s2 != s3 and s1 != s3:
    print('Os segmentos informados formam um triangulo ESCALENO')
else:
    print('Os segmentos informados NÃO FORMAM um triangulo')
