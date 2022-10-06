#Ejercicio 11: Agenda telefonica
#Hacer un programa que simule una agenda de contactos. Crear un
#diccionario donde la clave sea el nombre del usuario y el valor
#sea el telefono, el programa tendra el siguiente menu de opciones:
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir

#Describimos variables
agenda = {}
while True:
    print("\t//MENÚ//")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menú: "))
    if opcion == 1:
        nombre = input("Digite el nombre de contacto: ")
        telefono = input("Digite el numero de telefono: ")
        #ESTRUCTURA ANIDADA
        if nombre not in agenda:
            agenda[nombre] = telefono #CREAMOS DICCIONARIO
            print("Contacto agregado exitosamente.")
        else:
            print("El contacto ya existe.")
    elif opcion == 2:
        nombre = input("Digite el nombre de contacto que desea eliminar: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Se ha eliminado el contacto.")
        else:
            print("Este contacto no existe.") #Esto dice que no existe si dice un contacto q no esta
    elif opcion == 3:
        print("Agenda de contactos: ")
        for clave,valor in agenda.items(): #Con esta funcion mostramos las dos variables
            print(f"Nombre: {clave} \nTelefono: {valor}")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos.")
        break
    else:
        print("Opción incoreccta de menú.")
    print()

