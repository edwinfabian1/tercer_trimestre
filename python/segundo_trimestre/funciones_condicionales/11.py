"""Encontrar un número natural n más pequeño tal que la suma
de los n primeros números naturales (1 + 2 + 3 + 4.....)
exceda de una cantidad (máximo) introducida por el teclado.
Es decir cuantos números de la serie de los naturales debo
sumar para superar el dato máximo."""
def numeros():
    n = int(input("Ingrese un nro: "))
    cont = 0
    suma = 0
    for i in range (n):
        suma += i
        if suma <= n:
            cont += 1
    print (cont)
numeros()