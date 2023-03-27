import sqlite3#se importa la base de datos 
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')
con=sqlite3.connect('sqlitepython/conpython.db')#se instancia la ubicacion del archivo con una ubicacion remota 
print(type(con))#imprime el tipo de dato que contiene
micursor=con.cursor()
print(type(micursor))#trae el tipo de dato de micursor
sentencia="SELECT * from alumno;"#en esta sentencia se selecciona la tabla llamada alumno y trae todos los datos 
micursor.execute(sentencia)
for fila in micursor.fetchall():#el for hace un recorrido y fetchall devuelve todas las filas de una lista con tuplas 
    print(fila[0])#cada uno trae cada una de las columnas que se le indique 
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('-'*50)