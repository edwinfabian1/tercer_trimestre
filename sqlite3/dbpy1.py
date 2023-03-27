import sqlite3
with sqlite3.connect('sqlitepython/conpython.db')as con:#se hace la coneccion con la base de datos
    micursor=con.cursor()#
    sentencia="SELECT nombre,apellido FROM alumno;"#indica los valores que va a traer desde la tabla alumno
    print(micursor.execute(sentencia).fetchmany(10))# trae cada valor de la lista del cursor 

#print() 

def modificar(conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE{tabla} SET {campo}='{dato}'WHERE id='{id}' "
    micursor.execute(sentencia)
    con.commit()
    print('Modificacion exitosa !!!')

#DELETE FROM table_name WHERE 
def eliminar(conexion,tabla,campo,dato):
    micursor=conexion.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE{campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print('Eliminacion exitosa !!!')