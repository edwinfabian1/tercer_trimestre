# Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez
c=''
ca=input('ingrese un valor ')
def cadena(a,c):
    for i in a:
        if i not in c and i.isalpha()==True:
            c+=i
    return len(c)

print(cadena(ca,c))