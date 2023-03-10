class Registro:
    def __init__(self):
        self.documento=str(input('Ingrese documento: '))
        self.nombre=str(input('Ingrese nombre: '))
        self.edad=str(input('Ingrese edad: '))
        self.num_contacto=str(input('Ingrese numero de contacto: '))
        self.rol=str(input('Ingrese rol: '))

    def getdatos(self):
        return self.documento,self.nombre,self.edad,self.num_contacto,self.rol

    def actualizarUsuario(self):
        x=int(input('\n Ingrese 1 para actualizar nombre \n Ingrese 2 para actualizar edad \n'\
                    ' Ingrese 3 para actualizar contacto \n Ingrese 4 para cambiar rol '))
        if x == 1:
            upNombre=str(input('Ingrese nombre: '))
            self.nombre=upNombre
        elif x== 2:
            upEdad=str(input('Ingrese edad: '))
            self.edad=upEdad
        elif x ==3:
            upContacto=str(input('Ingrese numero de contacto: '))
            self.num_contacto=upContacto
        elif x ==4:
            upRol=str(input('Ingrese rol: '))
            self.rol=upRol

class Instructor(Registro):
    pass




class Estudiante(Registro):
    def extras(self,jornada,horario):
        self.jornada=jornada
        self.horario=horario
    def getdatos(self):
        return self.documento,self.nombre,self.edad,self.num_contacto,self.rol,self.jornada,self.horario

class  Materia:
    def __init__(self):
        self.nom_materia=str(input('Digite la materia: '))
        self.num_materia=int(input('Digite numero de las materias: '))
          
    def getagregarmaterias(self):
            return self.nom_materia,self.num_materia
        

class Curso:
    def __init__(self):
        self.datos=str(input('Digite los datos del curso: '))
        self.num_estudiantes=(input('Digite el numero de estudiantes: '))
        
    def getagregarcurso(self):
        return self.datos,self.num_estudiantes


class Inscripcion:
    

    def __init__(self):
        self.descripcion=str(input('Digite los datos de la inscripcion: '))
        self.detalles=str(input('Digite el numero de estudiantes: '))
    
    def getagregarinscripcion(self):
        
        return self.descripcion,self.detalles

class Matricula:
    def __init__(self):
        self.dato=str(input('Digite los datos de matricula: '))
        
    def getagregarmat(self):
        return self.dato


        
estudiante1=Estudiante()
#estudiante1.actualizarUsuario()
estudiante1.extras('jornada tarde', 1012)
print(estudiante1.getdatos())

instructor1=Instructor()
print(instructor1.getdatos())

materia1=Materia()
print(materia1.getagregarmaterias())

curso1=Curso()
print(curso1.getagregarcurso())

inscrip=Inscripcion()
print(inscrip.getagregarinscripcion())


matricula1=Matricula()
print(matricula1.getagregarmat())
