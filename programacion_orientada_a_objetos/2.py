# Escriba una clase Empleado que tenga como propiedades
# nombre, cargo, salario
# escriba metodos contructores, setters y getters
# escriba un método que permita calcular cuanto gana el empleado en una hora
# un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
# Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide
#crear una variable de clase y que aumente 
class empleado:
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
    
    def getnombre(self):
        return self.__nombre

    def getcargo(self):
        return self.__cargo
    
    def getsalario(self):
        return self.__salario
    
    

    def setnombre(self,nombre):
       self.__nombre=nombre 

    def setcargo(self,cargo):
        self.__cargo=cargo
    
    def setsalario(self,salario):
        self.__salario=salario

    def sal(self):
        x=self.__salario /240
        return round(x,2)
# un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
    def IPC (self):

        if self.__salario <1200000:
            return"debe ser mayor"
        if self.__salario ==1200000:
            self.__salario*=1.163
            return self.__salario
        else:
            self.__salario*=1.33
            return self.__salario

# Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide
    def extra(self,horas):
        if horas > 10:
        
        
    

        
        
        



emp1=empleado("miguel","gerente",3500000)

print(emp1.getcargo())
print(emp1.getnombre())
print(emp1.getsalario())
emp1.setcargo("presidente")
print(emp1.getcargo())
print(emp1.sal())
print(emp1.IPC())