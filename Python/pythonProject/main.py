#Clase: Listas
"""
nombres=["Gise","Facu","Lucas"]
#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #Le pasamos un parametro, la lista

#Agregamos un elemento
nombres.append("Fernando")
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(1,"Cecilia") #Es una funcion
print(nombres)
nombres.insert(3,"Debora")
print(nombres)

#Eliminamos un elemento
nombres.remove("Debora")
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico
del nombres[2] #del significa delete
print(nombres)

#Eliminar borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
print(nombres) #Aca muestra error
"""
#Ejercicio 1

for i in range (11):
    if i % 3 == 0:
        print(i)

print("")
#Ejercicio 2

for i in range(2,7):
    print(i)
print("")
#Ejercicio 3

for i in range(3,11,2):
    print(i)

#Definicion de tupla
cocina = ('cuchara','cuchillo','tenedor')
print(len(cocina))

#Acceder a un elemento, para esto utilizamos corchetes
print(cocina[0]) #Primer indice
#Mostrar de manera inversa
print(cocina[-1]) #Muestra de atras a adelante

#Acceder a un rango
print(cocina[0:2])

#Ejemplo
verduras = ('papa',) #Una tupla necesita aunque sea un elemento la coma
#De lo contrario solo seria un tipo str cadena

#Recorremos los elementos de la tupla con ciclo for
for cocinar in cocina:
    print(cocinar, end=' ') #Print esta usando \n para saltos de lineas
    #Usamos el end para eliminar los saltos de linea

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina
print(cocina) #Eliminamos la tupla





