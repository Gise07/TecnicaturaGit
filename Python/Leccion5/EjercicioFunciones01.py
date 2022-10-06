#Ejercicio 1: Crear una funcion para sumar los valores recibidos de tipo
#numerico, utilizando argumentos variables *args como parametro de la
#funcion y agregar como resultado la suma de todos los valores pasados
#como argumentos.

#DEFINIMOS UNA FUNCION
def sumar_valor(*args): #Recibimos una cantidad de parametros indefinidos
    resultado = 0
    #ITERAMOS CADA ELEMENTO
    for valor in args:
        resultado += valor
    return resultado

LLAMAMOS LA FUNCION
print(sumar_valor(3,5,9))

