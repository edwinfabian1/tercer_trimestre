#Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el valor numerico de acuerdo a los códigos del alfabeto
c=0
cad=input('ingese un valor \n')

def cadena(a,c):
    for i in a:
        c+=ord(i)
        print(ord(i))
    print(c)
cadena(cad,c)