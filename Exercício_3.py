"""
Construa um algoritmo que imprima no console a quantidade de dias, horas, minutos e segundos quetivemosem um determinado ano. Deverá receber apenas 1 valor através do input do teclado, para que o usuário possa digitar a quantidade de dias que teve no ano em que deseja saber os dados abaixo. Em seguida, deverá imprimir no console os seguintes dados:
Quantidade de horas no ano§Quantidadedeminutos no ano§Quantidade de segundos no ano
"""

ano = int(input('Digite o ano que deseja saber: '))
infos = 365
if ((ano % 4) ==0):
    infos = 366
    print('Ano bissexto = 366 dias')
    print(f'Quantidade de horas do ano: {infos*24} horas')
    print(f'Quantidade de minutos do ano: {infos*24*60} min')
    print(f'Quantidade de segundos do ano: {infos*24*60*60} segundos')
else:
    print(f'Quantidade de horas do ano: {infos*24} horas')
    print(f'Quantidade de minutos do ano: {infos*24*60} min')
    print(f'Quantidade de segundos do ano: {infos*24*60*60} segundos')
    





