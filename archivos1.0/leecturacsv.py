from Datos import *
import csv
listadatos=[]
with open('archivos1.0\Interprise.csv') as csvDataFile:

    csvReader=csv.reader(csvDataFile)
    
    for i in csvDataFile:
        d=Datos(i[0],i[1],i[2],i[3])
        listadatos.append(d)
        
print(listadatos)
print(d.getdatos())
for apr in listadatos:
    print(apr.getdatos())