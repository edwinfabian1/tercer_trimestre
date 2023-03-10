class Registro:
    def __init__(self,documento,nombre,edad,num_contacto,correo):
        self.__documento=documento
        self.nombre=nombre
        self.edad=edad
        self.num_contacto=num_contacto
        self.correo=correo
#getter
    def getdocumento(self):
        return self.__documento
    
    def getnombre(self):
        return self.nombre
    
    def getedad(self):
        return self.edad
    
    def getnum_contacto(self):
        return self.num_contacto
    
    def getcorreo(self):
        return self.correo
#setter
    
    def setdocumento(self,documento):
        self.__documento=documento
    
    def setnombre(self,nombre):
        self.nombre=nombre

    def setedad(self,edad):
        self.edad=edad
    
    def setnum_contacto(self,num_contacto):
        self.num_contacto=num_contacto

    def setcorreo(self,correo):
        self.correo=correo

regis=Registro('21653215','andres','15','3155546415','adrew@gmail.com\n')

print(regis.getdocumento())
print(regis.getnombre())
print(regis.getedad())
print(regis.getnum_contacto())
print(regis.getcorreo())
regis.setdocumento("fgdh")
regis.getdocumento


class Instructor:
    def __init__(self,documento,nombre,correo,num_contacto):
        self.__documento=documento
        self.nombre=nombre
        self.correo=correo
        self.num_contacto=num_contacto
#       
    def getducumento(self):
        return self.__documento
    
    def getnombre(self):
        return self.nombre
    
    def getcorreo(self):
        return self.correo
    
    def getnum_contacto(self):
        return self.num_contacto
#

    def setdocumento(self,documento):
        self.__documento=documento
    
    def setnombre(self,nombre):
        self.nombre=nombre

    def setcorreo(self,correo):
        self.correo=correo
    
    def setnum_contacto(self,num_contacto):
        self.num_contacto=num_contacto 
                   
inst=Instructor('151564','carlos','charls@gmail.com','3125898747\n')
print(inst.getducumento())
print(inst.getnombre())
print(inst.getcorreo())
print(inst.getnum_contacto())


class Materia(Instructor):
    def __init__(self,id,nom_materias,num_materias,cronograma):
        self.__id=id
        self.nom_materias=nom_materias
        self.num_materias=num_materias
        self.cronograma=cronograma
#
    def getid (self):
        return self.__id
    
    def getnom_materias(self):
        return self.nom_materias
    
    def getnum_materias(self):
        return self.num_materias
    
    def getcronograma(self):
        return self.cronograma
#

    def setid(self,id):
        self.__id=id
    
    def setnom_materias(self,nom_materias):
        self.nom_materias=nom_materias

    def setnum_num_materias(self,num_materias):
        self.num_materias=num_materias
    
    def setcronograma(self,cronograma):
        self.cronograma=cronograma

mat=Materia('1102','ingles,español,matematicas','3','2023\n')
print(mat.getid())
print(mat.getnom_materias())
print(mat.getnum_materias())
print(mat.getcronograma())


class Estudiante:
    def __init__(self,id,curso,jornada,horario):
        self.__id=id
        self.curso=curso
        self.jornada=jornada
        self.horario=horario
#
    def getid(self):
        return self.__id
    
    def getcurso(self):
        return self.curso
    
    def getjornada(self):
        return self.jornada
    
    def gethorario(self):
        return self.horario
#

    def setid(self,id):
        self.__id=id
        
    def setcurso(self,curso):
        self.curso=curso
        
    def setjornada(self,jornada):
        self.jornada=jornada
    
    def sethorario(self,horario):
        self.horario=horario

estud=Estudiante('1000792656','1102','mañana','6am a 12pm\n')
      
print(estud.getid())
print(estud.getcurso())
print(estud.getjornada())
print(estud.gethorario())     

class Inscripciones(Estudiante):
    def __init__(self,id,descripcion,detalles):
        self.__id=id
        self.descripcion=descripcion
        self.detalles=detalles
    
    def getid(self):
        return self.__id
    
    def getdescripcion(self):
        return self.descripcion
    
    def getdetalles(self):
        return self.detalles
    
#  
    def setid(self,id):
        self.__id=id
        
    def setdescripcion(self,descripcion):
        self.descripcion=descripcion
    
    def setdetalles(self,detalles):
        self.detalles=detalles    

inscrip=Inscripciones('201','ingenieria','10\n')     
print(inscrip.getid())        
print(inscrip.getdescripcion())
print(inscrip.getdetalles()) 

 
class Matricula:
    def __init__(self,id,datos):
        self.__id=id
        self.datos=datos
#        
    def getid(self):
        return self.__id
    
    def getdatos(self):
        return self.datos    
        
#         
    def setid(self,id):
        self.__id=id
        
    def setdatos(self,datos):
        self.datos=datos
        
matri=Matricula('1','seleccionado')
print(matri.getid())        
print(matri.getdatos())  
        
        
class Curso(Materia,Inscripciones,Matricula):
    def __init__(self,id,datos,num_estudiantes):
        self.__id=id
        self.datos=datos
        self.num_estudiantes=num_estudiantes
#    
    def getid(self):
        return self.__id
    
    def getdatos(self):
        return self.datos
    
    def getnum_estudiantes(self):
        return self.num_estudiantes
    
#
    def setid(self,id):
        self.__id=id
        
    def setdatos(self,datos):
        self.datos=datos
    
    def setnum_estudiantes(self,num_estudiantes):
        self.num_estudiantes=num_estudiantes  
cur=Curso('100','tecnico','35')
        
print(cur.getid()) 
print(cur.getdatos())
print(cur.getnum_estudiantes())            
