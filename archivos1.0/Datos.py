class Datos:
    def __init__(self,indice,organizacion,sitioweb,pais):
        self.__indice=indice
        self.__organizacion=organizacion
        self.__sitioweb=sitioweb
        self.__pais=pais

    def getdatos(self):
        return self.__indice+' '+self.__organizacion+' '+self.__sitioweb+' '+self.__pais