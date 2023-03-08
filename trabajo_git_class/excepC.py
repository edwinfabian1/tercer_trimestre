def try_syntax(numerator, denominator):
    try:
        print(f'In the try block: {numerator}/{denominator}')# imprime la cadena de texto con el valor de las variables 11/0
        result = numerator / denominator
    except ZeroDivisionError as zde:        #si no sucede este error 
        print(zde)                      
    else:                                   #hace este else
        print('The result is:', result) 
        return result                   #hace el retorno en result
    finally:                #este llamada es opcional
        print('Exiting')
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 0))    #imprime que no hay nada 