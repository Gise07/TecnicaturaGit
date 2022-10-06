#Ejercicio 5: Convertidor de temperaturas
#Realizar dos funciones para convertir de grados celcius a fahrenheit
#y viceversa. Investigar las formulas

#FUNCION QUE CONVIERNE DE CELSIUS A FAHRENHEIT
def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32 #la presedencia: multiplicacion, division y suma

#FUNCION QUE CONVIERNE DE FAHRENHEIT A CELSIUS
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C : {resultado:.2f}')

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F : {resultado:.2f}')


