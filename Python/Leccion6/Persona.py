#PROGRAMACION ORIENTADA A OBJETOS
class Persona: #Creamos una clase
    def __init__(self,nombre, apellido, edad): #Referencia al objeto que se va a crear, metodo especial
        self.nombre = nombre
        self.apellido = apellido #Atributos de metodo, no de clase
        self.edad = edad #Valores de default
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Gisela', 'Vizcaino', 22) #CONSTRUCTOR, envviamos argumentos
print(persona1.nombre)  #Esto es para ver el tipo
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Facundo','Pereyra', 24)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

#Modificamos valores del objeto 1
persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 20
rint(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle()
persona2.mostrar_detalle() #LLAMAMOS AL METODO
