class Aprendiz:#definimos una clase llamada aprendiz
    def __init__(self,nombre):#se inicializa el constructor con el metodo init se crea un objeto de la clase y se utilza para inicializar los atributos del objeto
        self.__nombre=nombre# en esta linea es un argumento que se utiliza para inicializar el atributo nombre
        self.__cursos=[]# aqui se inicia el atributo cursos con un lista vacia 

    def agregarCurso(self,titulo):#en esta linea se define el parametro llamdo titulo 
        self.__cursos.append(titulo)#self hace refercia al objeto que se esta agregado y creando 

    def getCursos(self):#en esta linea se define el parametro llamdo  cursos
        return self.__cursos#retorna el parametro cursos

class Curso:#se define una segunda clase llamada cursos
    def __init__(self,titulo):#en esta linea se inicializa el constructor se crea el objeto de la clase 
        self.__titulo=titulo#en esta linea se crea un objeto 

    def getTitulo(self):#aqui se define titulo
        return self.__titulo#retorna el parametro titulo
    
a=Aprendiz('Martha')
c1=Curso('Python Intermedio')#se crea un primer objeto
c2=Curso('Python Basico')#se crea un segundo objeto
c3=Curso('Introduccion a Java')#se crea un tercer objeto

a.agregarCurso(c1)#las tres lineas agregan a curso cada objeto como argumento
a.agregarCurso(c2)
a.agregarCurso(c3)

print(a.getCursos())#en esta impresion devuelve el nombre de los cursos en los que esta la aprendiz


for curso in a.getCursos():#el for esta recoriendo la lista des todos los cursos y los agrega 
    print(curso.getTitulo())#toma los objetos de cruso y los muestra en pantalla 