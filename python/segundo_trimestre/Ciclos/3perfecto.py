"""Determinar si un número es o no es perfecto. Un numero es
perfecto si la suma de sus divisores sin incluir el propio
número es igual a este"""

n = int(input("Ingrese un nro: "))
suma = 0

for i in range(1,n):
    if n % i == 0:
        suma += i
if suma == n:
    print("El nro SI es perfecto")
else: print("El nro NO es perfecto")