class Registro:
    def __init__(self,documento,nombre,edad,num_contacto):
        self.__documento=documento
        self.nombre=nombre
        self.edad=edad
        self.num_contacto=num_contacto
#getter
    def getducumento(self):
        return self.__documento
    
    def getnombre(self):
        return self.nombre
    
    def getedad(self):
        return self.edad
    
    def getnum_contacto(self):
        return self.num_contacto
#setter
    
    def setdocumento(self,documento):
        self.__documento=documento
    
    def setnombre(self,nombre):
        self.nombre=nombre

    def setedad(self,edad):
        self.edad=edad
    
    def setnum_contacto(self,num_contacto):
        self.num_contacto=num_contacto

regis=Registro('10004464','andres','15','3155546415')

print(regis.documento())
print(regis.nombre())
print(regis.edad())
print(regis.num_contacto())



class Instructor:
    def __init__(self,documento,nombre,correo,num_contacto):
        self.__documento=documento
        self.nombre=nombre
        self.correo=correo
        self.num_contacto=num_contacto

class Sujeto(Instructor):
    def __init__(self,documento, correo,nombre,cronograma):
        self.__documento=documento
        self.correo=correo
        self.nombre=nombre
        self.cronograma=cronograma

class Estudiante:
    def __init__(self,curso):
        self.curso=curso



        

        
