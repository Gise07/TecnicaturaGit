import math #Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)
#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#Elimine los elementos repetidos, por ultimo mostrar la lista.

#Creamos una lista, es con corchetes
lista = [1,2.3, "Gisela",7,7,3,"Facundo",5,"Gisela" ]
#Convertimos la lista a un conjunto, asi se elimina lo repetido
#conjunto = set(lista) #Convertimos la lista a un conjunto de tipo set
#lista = list(conjunto) #Convertimos el conjunto a una lista
lista = list(set(lista)) #Hacemos lo mismo en una sola linea de codigo(eficiente)

#Ejercicio Matematicas
#Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo: "))
while numero < 0:
    print("Error -> Deberia ser un numero positivo.")
    numero = int(input("Digite un numero positivo: "))
print(f'\nSu raiz cuadrada es: {math.sqrt(numero):.2f}')



