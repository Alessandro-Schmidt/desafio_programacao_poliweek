"""
Construa um algoritmo que calcule a tabuada dos números de 1 a 10. Não é necessário nenhuma entrada pelo input do teclado. Deverá apenas construir sua lógica para imprimir no console a tabuada de todos os números de 1 a 10, exatamente no formato de saída ao lado:
"""

i = 1
while i<11:
    a = 0
    print(f'TABUADA DO {i}')
    while a <11:
        print(f'{a} * {i} = {a*i}')
        a+=1
    i+=1
