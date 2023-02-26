try:
    #print(1/1))
    raise SyntaxError # el raise permite que se presente el syntaxisError
except SyntaxError:
    print('Cierra el parentesis') 

#El interprete de python permite definir el error con el try