#Clase: Listas
"""
#Colecciones en Python,arreglos o vectores

nombres=["Gise","Facu","Lucas"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1]) #del ultimo hacia el primero
print(nombres[-2])
print(nombres[0:2]) #solo muestra el indice 0,1 pero no el indice 2
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3]) #Indices a mostrar 0,1,2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#Modificamos un valor
nombres[3] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

#Preguntamos cuantos elementos tiene una lista
print(len(nombres)) #Le pasamos un parametro, la lista

#Agregamos un elemento
nombres.append("Fernando")
nombres.append([1,2,3]) #Agregamos una lista
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
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

#Ejercicio 1

#for i in range (11):
 #   if i % 3 == 0:
  #      print(i)

#print("")

#Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimelos

for i in range(2,7):
    print(i)
"""


#Uso de rangos
#GISELA VIZCAINO

#Ejercicio 3 : Crear un rango de 3 a 10 pero con incremento de 2 en 2, 
#en lugar de 1 en 1

for i in range(3,11,2):
    print(i)

"""
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

#Dada la siguiente tupla
tupla = (13,1,8,3,2,5,8)
#Crear una lista que solo incluya los numeros menores a 5
#e imprima por consola [1,3,2]

lista = [] #Definimos la lista
#Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#Tipo set
planetas = {'Marte','Jupiter','Venus'}
print(planetas) #No los imprime en orden
print(len(planetas)) #Muestra la cantidad de elementos
print('Marte' in planetas) #Para ver si esta el elemento en el set

#Agregar un elemento
planetas.add('Tierra') #Add es una funcion, no se agregan duplicados
print(planetas)

#Eliminar elementos, puede arrojar error si el elemento no existe
planetas.remove('Jupiter')
print(planetas)
planetas.discard('Tierra') #Elimina tambien sin presentar ningun tipo de error
print(planetas)

#Limpiar tipo set o conjunto
planetas.clear()
print(planetas)

#Eliminar set o conjunto
del planetas
print(planetas)

#Diccionario: compuesto por dos elementos
#una llave y un valor
#dict(key,value)
diccionario = {
    'IDE' : 'Integrated development enviroment',
    'POO' : 'Programacion orientada a objetos',
    'SABD' : 'Sistema de administracion de base de datos',
}
print(len(diccionario))#vemos cuantos elementos hay

#Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento
print(diccionario.get('POO'))

#Modificamos elementos
diccionario['IDE'] = 'Entorno de desarrollo integrado'
print(diccionario)

#Como recorrer los elementos
for termino in diccionario: #Recorremos mostrando solo las llaves
    print(termino)

#Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys():
    print(termino) #Muestra solo las llaves

for valor in diccionario.values():
    print(valor) #Muestra los valores

#Comprobar la existencia de algun elemento
print('IDE' in diccionario)

#Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario

#Concatenar listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7,8,9]) #Funcion para agregar varios elementos a una lista
print(lista3)

print(lista.index(5)) #Ver en que indice esta un elemento
#print(lista3.index(0)) esto da error por no ser un elemento de la lista

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #Cuenta cuantos valores iguales hay dentro de una lista

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
lista = [1,2,3] * 2
print(lista)

#Metodos de ordenamiento
lista3.sort() #Ordena los elementos de menor a mayor
print(lista3)
lista3.sort(reverse=True)
print(lista3) #Los ordena de mayor a menor

#Repaso de tuplas
tupla = (4,'Hola',6.78,[1,2,3],4,'Hola')#Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla) #Accion booleana, su respuesta es de tipo boolean
#Lo que podemos usar dentro de tuplas son : index,count,len
#En tuplas se puede convertir de tupla a lista y de lista a tupla

#Repaso de set o conjunto
#Para definir un conjunto
conjunto = set()
conjunto1 = {} #Hay que inicializarlo con un elemento para que ande despues
conjunto.add(7)
conjunto.add(6)
conjunto.add('Hola')
print(conjunto)
conjunto1.add(7,8,9) #Esto da error porque el conjunto esta vacio con las llaves
print(conjunto1)
print(3 not in conjunto1) #Preguntamos si el n 3 no esta en el conjunto1

#Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto) #Nos devuelve una respuesta booleana

#Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto #La linea une los dos conjuntos, union
print(conjunto3)

conjunto3 = conjunto1 & conjunto #Que elemento tienen en comun, interseccion
print(conjunto3)

conjunto3 = conjunto1 - conjunto #Asigna el valor que esta en el conjunto1 y no en el conjunto0
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto #Muestra elemento que NO comparten
print(conjunto3)

conjunto3 = conjunto1 | conjunto
print(conjunto1.issubset(conjunto3)) #Pregunta si es subconjunto de un conjunto

print(conjunto3.issuperset(conjunto1)) #Preguntamos si los elementos del conjunto1
print(conjunto3.issuperset(conjunto)) #estan dentro del 3
#Si es verdadero quiere decir que el conjunto3 es un super conjunto

#Como saber si ambos conjuntos son disconexos, esto es si no comparten elems en comun
print(conjunto1.isdisjoint(conjunto)) #No hay cosas en comun

#Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #Esto hace que el conjunto sea totalmente inmutable
#No se puede agregar, modoficar ni eliminar elementos del conjunto
"""










