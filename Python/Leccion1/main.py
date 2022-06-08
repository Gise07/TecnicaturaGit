"""
# Clase dos variables
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
#Las literales se escriben x184
print(id(y))
print(id(z)) #Cada valor es una literal
#Clase 3 tipos de datos en Python int,float,string,bool
a = "Hola mundo"
print(type(a)) #Para ver el tipo de dato que es
x = 14.5
print(x)
print(type(x))
x = True
print(x)
print(type(x))

#Manejo de cadenas (String)
miGrupoFavorito = "Que se yo"
print("Mi grupo favorito es:" + miGrupoFavorito)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

#Tipos Booleanos (bool)
miBooleano = 1 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

#Procesar la entrada del usuario, funcion input
resultado = input("Digite un numero: ")#Regresa un dato tipo string
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado se la suma es: ", resultado)
"""
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("Resultado de la suma: ",suma)
print(f"El resultado de la suma es: ¨{suma}")#Interpolacion

resta =operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division es: {division}")
disivion = operandoA // operandoB
print(f"El resultado de la division (int) es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")
esponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")

#Ejercicio del rectangulo
alto = int(input("Digite el alto del rectangulo: "))
ancho = int(input("Digite el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("El area es: ", area)
print("El perimetro es:",perimetro)
"""
"""
#Operadores de asignacion
miVariable3 = 10
print(miVariable3)
#Operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1 #Lo mismo que lo de arriba
print(miVariable3)
#miVariable3 = miVariable3 -2
miVariable3 -= 2
print(miVariable3)
miVariable3 *= 3
print(miVariable3)

#Operadores de comparacion
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
print(resultado)
#Operador diferente
resultado = d != b
print(resultado)
#Operador mayor que
resultado = d > b
print(resultado)
#Operador menor que
resultado = d < b
print(resultado)
#Operador menor o igual que
resultado = d <= b
print(resultado)
#Operador mayor o igual que
resultado = d >= b
print(resultado)
"""
"""
#Operadores Logicos
a= False
b= True
resultado = a and b
print(resultado)

#Operador or
resultado= a or b
print(resultado)

#Ejercicio: Valor dentro de un rango
valor = int(input("Digite un numero: "))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} esta dentro del rango')
else:
    print(f'El valor {valor} no esta dentro del rango')

#Ejercicio con el operador or, Operador not
vacaciones = False
diaDescanso = True
if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('Tiene trabajo que hacer')

#Ejercicio: Rango entre 20 y 30 años
edad = int(input('Digite su edad: '))
#veinte = edad >=20 and edad < 30
#print(veinte)
#treinta = edad >=30 and edad < 40
#print(treinta)
if: (edad >= 20 and edad < 30) or (edad >=30 and edad < 40)
    print("Estas dentro del rango de los 20 a 30 años")
#Sintaxis simplificada del operador and
#if (20 <=edad < 30) or (30 <= edad < 40):
    #print("Estas dentro del rango de los 20s a 30s años")
#if veinte or treinta:
 #   print('Estas dentro del rango de los (20s) a (30s) años')
#else:
 #   print('No estas en el rango de los (20s) a (30s) años')

#Ejercicio: El mayor de dos numeros
numero1 = int(input("Digite el valor del numero1: "))
numero2 = int(input("Digite el valor del numero2: "))

if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")

#Ejercicio: Tienda de libros
print("Digite los siguientes datos del libro ")
nombre = input("Diite el nombre del libro: ")
id = int(input("Digite el ID del libro: "))
precio = float(input("Digite el precio del libro: "))
envioGratuito = input("Indicar si el envio es gratuito (True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"
print(f'''
    Nombre : {nombre}
    ID : {id}
    Precio : {precio}
    Envio Gratuito? : {envioGratuito}
''')


#Ejercicio: Numero par o impar clase 4
a = int(input("Digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es : {a} es un numero PAR")
else:
    print(f"El valor de a es: {a} es un numero IMPAR")

#Ejercicio: Determinar si es mayor de edad clase 4
edadAdulto = 18
edadPersona = int(input("Digite su edad"))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print (f"Su edad es: {edadPersona} años, usted es menor de edad")
"""








