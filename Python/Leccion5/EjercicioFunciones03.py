#Ejercicio 3: Funcion recursiva
#imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
#puede ser cualquier valor positivo, por ejemplo, si pasamos el valor de 5
#debe imprimir:
#5
#4
#3
#2
#1
#En caso de ser el numero 3 imprimir:
#3
#2
#1
#si se ingresan numeros negativos no imprime nada

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
numeroFactorial = int(input('Digite el numero para calcular el factorial: '))
resultado = factorial(numeroFactorial) #Lo hacemos en codigo duro
print(f'El factorial del numero {numeroFactorial} es: {resultado}')
#El usurario ingresa el valor

#EL OTRO
def imprimir_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimir_numeros_recursivos(numero-1)
    elif numero ==0:
        return #Aca esta vacio
    elif numero <= 0:
        print('El valor ingresado es incorrecto.')
imprimir_numeros_recursivos(5)