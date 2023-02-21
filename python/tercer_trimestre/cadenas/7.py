#De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.

cad=input("digite un valor:\n ")
def vocales():
    vocal=""
    consonante=""
    tilde=""
    caracter=""
    
    for i in cad:
        if i.isalpha()==True:
            if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
                vocal+=i 
            elif i=="á" or i=="é" or i=="í" or i=="ó" or i=="ú":
                tilde+=i
            else:
                consonante+=i
        else:
            caracter+=i
    print(len(vocal),"vocales")
    print(len(tilde),"vocales con tilde")
    print(len(consonante),"consonantes")
    print(len(caracter),"caracteres")
    
vocales()