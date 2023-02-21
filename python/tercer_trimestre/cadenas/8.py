#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin.
c="murcielago"
cad=input('ingese un texto \n')
def texto(cad,c):
    for i in cad:
        if i in c:
            cad=cad.replace(i,str(c.index(i)))
    return cad

print(texto(cad,c))