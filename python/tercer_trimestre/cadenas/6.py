#Determinar en que tiempo esta conjugado un verbo

cadena = input("Introduce una cadena: ")

for i in range(2**len(cadena)):   # Se iterará 2^n veces, donde n es el número de caracteres en la cadena
    formato = "{0:0" + str(len(cadena)) + "b}"   # Crea una cadena de bits con tantos caracteres como la cadena de entrada
    binario = formato.format(i)   # Obtiene la representación binaria del índice actual
    nueva_cadena = ""   # Inicializa una nueva cadena vacía
    for j in range(len(cadena)):
        if binario[j] == "0":
            nueva_cadena += cadena[j].upper()   # Convierte el carácter actual a mayúscula si el bit correspondiente es 0
        else:
            nueva_cadena += cadena[j].lower()   # Convierte el carácter actual a minúscula si el bit correspondiente es 1
    print(nueva_cadena) 