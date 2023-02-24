#Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última
c=""
cad=input('ingese un valor: \n')
def cadena(c,cad):
    for i in cad:
        c+=i
        if len(c)>1:
            print(c)
cadena(c,cad)