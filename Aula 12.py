"""Aula 12 - Condições aninhadas:

As estruturas de condição, como visto nas aulas anteriores, são denominadas "if"(se) e "else"(senão). Contudo, a grande
maioria das situações não são "binárias", havendo ocasiões onde simplesmente um "se" e um "senão" não bastam.
Nesse raciocínio,  surge o "elif", que é uma condição que "aninha" mais uma opção dentro de um "if".

Na estrutura do código, os elementos apresentam-se da seguinte forma:

if condição.1():
    bloco de informações 1
elif condição.2():
    bloco de informações 2
else:
    bloco de informações 3

Dentro dessa estrutura, se necessário for, pode ser colocadas quantas "elif" forem necesárias para completar as
possibilidades.

Obs.: Dentro da estrutura, o único elemento obrigatório é o "if". Pode ser inseridos um "if" e vários "elif"; um "if",
um ou mais "elif" e um "else" ou, simplesmente um "if" (neste caso, qualquer coisa que não seja a condição imposta no
"if" será considerado um "else". Nos outros casos, o else é considerado como qualquer coisa que fuja do if ou dos
"elif".)

EXEMPLOS PRÁTICOS:

c = str(input('Que carro você tem? ').lower().strip())
if c in 'voyage, cobalt, honda city, logan, prisma, onix':
    print('Seu carro é um Sedan médio')
elif c in ('polo, argo, ka, hb20, sandero, cruze, celta, palio'):
    print('Seu carro é um hatch')
elif c in ('bandeirante, f-1000, f1000, ram, c10, d20, '):
    print('Seu carro é uma caminhonete.')
else:
    print('Que carro diferente!')

"""
