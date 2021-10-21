""" Construa um algoritmo que imprima no console a área de um losango. Deverá receber 2 valores através do input do teclado para que o usuário possa digitar a diagonal maior e a diagonal menor. Em seguida,deverá imprimir no consoleo cálculo da área."""

d_maior = float(input('Digite o valor da diagonal maior em cm: '))
d_menor = float(input('Digite o valor da diagonal menor em cm: '))

print('\nCalculo da área:\n')
print(f'S = ({d_maior} x {d_menor})/2')
print(f'S =  {(d_maior*d_menor)/2} cmˆ2')