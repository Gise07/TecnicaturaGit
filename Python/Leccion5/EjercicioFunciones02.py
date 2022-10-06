#Ejercicio 1: Crear una funcion para multiplicar los valores recibidos de tipo
#numerico, utilizando argumentos variables *args como parametro de la
#funcion y agregar como resultado la multiplicacion de todos los valores pasados
#como argumentos.

#DEFINIMOS UNA FUNCION
def multiplicar_valor(*args): #Recibimos una cantidad de parametros indefinidos
    resultado = 1 #El cero es el elemento nulo en la multiplicacion
    #ITERAMOS CADA ELEMENTO
    for valor in args:
        resultado *= valor
    return resultado

#LLAMAMOS LA FUNCION
print(multiplicar_valor(3,5,9))