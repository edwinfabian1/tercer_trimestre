class A1:#se define una clase llamada A1
    def __init__(self):#se inicializa el constructor con el metodo init 
        pass#no pide ninguna operacion espesifica
    def saludo(self):#
        print('Hola desde A1')#en esta linea imprime un mensaje

class A2:#se define una segunda clase llamada A2
    def __init__(self):#se inicializa un segundo costructor 
        pass#
    def saludo(self):#
        print('Hola desde A2')#


class B(A2,A1):
    def __init__(self):
        pass
    def saludo(self):
        print('Hola desde B')
    def __str__(self):
        return 'Soy un objeto de la clase B'
obj=B()
print(obj.__str__())
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())