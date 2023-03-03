class Curso:# se define una clase llamada curso
    def __init__(self,titulo):#aqui se inicializa el constructor con los atributos 
        self.__titulo=titulo# se crea la variable titulo

    def getTitulo(self):#en esta linea se define el parametro llamdo titulo 
        return self.__titulo#en esta linea retorna el parametro titulo

class Aprendiz:#se define una segunda clase con el nombre Aprendiz
    def __init__(self,nombre):#se inicializa el constructor con el atributo nombre
        self.__nombre=nombre#en esta linea se crea un objeto llamado cursit de la clase curso 
        self.__cursos=[]#se crea una lista como atributo 

    def agregarCurso(self,nombreCursito):#se define un metodo 
        cursito=Curso(nombreCursito)#
        self.__cursos.append(cursito)#

    def getCursos(self):#
        return self.__cursos#
    
ap=Aprendiz('Sofia')#
ap.agregarCurso('Python Basico')#
ap.agregarCurso('Python Intermedio')#

for c in ap.getCursos():#
    print(c.getTitulo())#