#PROGRAMACION ORIENTADA A OBJETOS
class Persona: #Creamos una clase
    def __init__(self,nombre, apellido, edad, *args, **kwargs): #Referencia al objeto que se va a crear, metodo especial
        self.nombre = nombre
        self.apellido = apellido #Atributos de metodo, no de clase
        #self._dni = dni#ENCAPSULADO
        self.edad = edad #Valores de default
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}, Direccion: {self.args}, Datos importantes: {self.kwargs}')

persona1 = Persona('Gisela', 'Vizcaino', 22) #CONSTRUCTOR, enviamos argumentos
print(persona1.nombre)  #Esto es para ver el tipo
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Facundo','Pereyra', 24)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} {persona2.edad}')

#Modificamos valores del objeto 1
persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 20
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} {persona1.edad}')

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() #La referencia se pasa de manera automatica
persona2.mostrar_detalle() #LLAMAMOS AL METODO

Persona.mostrar_detalle(persona1) #Le pasamos una referencia, si no da error
#Esto igual no se usa, no es eficaz, se usa lo de arriba

persona1.telefono = '4444555533'
print(persona1.telefono) #Hemos creado un atributo de un objeto

#print(persona2.telefono) el objeto persona2 no tiene atributo, da error
persona3 = Persona('Rogelio', 'Romero',44563256, 22, 'Telefono', '2554545525', 'Calle Lopez', 681,'Manzana',77, 'Casa', 18, Altura = 1.55, Peso=55, CFavorito= 'Rosa' )
persona3.mostrar_detalle()
#print(persona3._dni) ESTO NO SE DEBE HACER, ESTA ENCAPSULADO
#persona3.__nombre ESTA TOTALMENTE ENCAPSULADO __