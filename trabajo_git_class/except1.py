#def divisores(num):
#     for i in range(num):
#         if num%i==0:
#             print(i,' es divisor')

# try:
#     divisores(19)
# except:

def divisores(num):             #se crea una funcion 

    if type(num)!=int:                    #el if nos dice si el operador no es igual imprima (que solo trabaja con numeros)
        print('Solo trabaja con numeros')   
    else:                                
        try:
            for i in range(1,num):       #le dice que recorra i en num empezando desde 1  
                if num%i==0:        # si num reciduo de i es igual a 0 imprime que es divisor
                    print(i,' es divisor')
        except ZeroDivisionError:
            print('Indeterminacion')
        except TypeError:                  #con el try podemos identificar en caso que se cumplan algunos de estos errores se imprimiran
            print('No ingreso un numero')
        except:
            print('Error no determinado')

divisores([])                               #aqui se llama la funcion 
print('El programa continua desde aqui')

