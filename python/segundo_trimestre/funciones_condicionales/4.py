"""Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. 
manera:
Si trabaja 40 horas o menos se le paga $2600 por hora
Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40 
horas y $5000 por cada hora extra"""
def salarios(n):
    salario=0
    if horas <= 40:
        return (salario)
    else:
        salario = 40 * 2600
    return (salario + extra)

horas = float(input("Ingrese cantidad de horas laboradas "))
salario = horas * 2600
extra = (horas - 40) * 5000

print(salarios(horas))
