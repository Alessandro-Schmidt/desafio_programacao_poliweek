"""Data a matriz A abaixo, construa um algoritmo que imprima no consoleos valores desta matriz naordemcontrária, do último elemento (5) até o primeiro elemento (2). A sequencia deverá ficar na seguinte forma:
519076212
"""

A = [[2,1,2],[6,7,0],[9,1,5]]

i = 2 
k = 2
while i>=0: 
    print(A[i][k], end='')
    k-=1
    if k == -1:
        k=2
        i-=1
    

