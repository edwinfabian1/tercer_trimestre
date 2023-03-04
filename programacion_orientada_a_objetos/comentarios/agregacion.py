class Curso:# se define una clase llamada curso
    def __init__(self,titulo):#aqui se inicializa el constructor con los atributos "el objeto"
        self.__titulo=titulo# se crea la variable titulo "seria otro objeto"

    def getTitulo(self):#en esta linea se define el parametro llamdo titulo 
        return self.__titulo#en esta linea retorna el parametro titulo

class Aprendiz:#se define una segunda clase con el nombre Aprendiz
    def __init__(self,nombre):#se inicializa el constructor con el atributo nombre
        self.__nombre=nombre#en esta linea se crea un objeto 
        self.__cursos=[]#se crea una lista como atributo 

    def agregarCurso(self,nombreCursito):#se define el metodo llamado agregar cursito con su parametro nombre cursito
        cursito=Curso(nombreCursito)#se crea una instancia de la clase llamada cursito
        self.__cursos.append(cursito)#se agrega la instancia cursos a cursitos 

    def getCursos(self):#aqui se define la funcion con el metodo getcurso
        return self.__cursos# self hacer referencia a la clase y la retorna 
    
ap=Aprendiz('Sofia')#esta instanciando el objeto en la clase aprendiz
ap.agregarCurso('Python Basico')#se llama el metodo 
ap.agregarCurso('Python Intermedio')#se llama el metodo una segunda vez

for c in ap.getCursos():#en esta linea el for esta recorriendo cada elemento de la lista cursos de la instanciacion ap de la clase aprendiz y se guarda cada elemento en la variable c
    print(c.getTitulo())# aqui se llama el metodo gettitulo con la instancia c de la clase curso y se imprime