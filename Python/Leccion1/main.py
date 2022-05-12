"""
# Procesar la entrada del usiario
# funcion input
resultado = input ("Digite un numero: ")   #Regresa un dato tipo string
print(resultado)

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado se la suma es: ", resultado)

"""
edadAdulto = 18
edadPersona = int(input("Digite su edad"))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print (f"Su edad es: {edadPersona} años, usted es menor de edad")



#Ejercicio: Rango entre 20 y 30 años
edad = int(input('Digite su edad: '))
veinte = edad >=20 and edad < 30
print(veinte)
treinta = edad >=30 and edad < 40
print(treinta)

if veinte or treinta:
    print('Estas dentro del rango de los (20s) a (30s) años')
else:
    print('No estas en el rango de los (20s) a (30s) años')
