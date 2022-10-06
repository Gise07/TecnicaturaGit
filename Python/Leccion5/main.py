#Comenzamos con funciones

#Definimos una funcion
def mi_funcion(): #Aca van los parametros de la funcion
    print("Saludos a todos los alumnos de la tecnicatura")

mi_funcion() #Estamos llamando a la funcion
#No se puede llamar antes de definir una funcion

#Desempaquetado de listas o list unpacking
def show(name, lastName): #PARAMETROS DENTRO DE PARENTESIS
    print(name+ ' '+lastName)
person = ["Facundo","Gisela"]
show(person[0],person[1]) #Le pasamos los datos a nuestra funcion, las que guardamos
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Lucas", "Facundo") #Desenpaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Vizcaino", "name": "Gisela"} #DICCIONARIO
show(**person3) #Usamos dos ** porque tiene que mostrar clave y valor del diccionario

numbers = [1,2,3,4,5] #Aun con la lista vacio se va a ejecutar el else
for n in numbers:
    print(n)
    if n == 3:
        break #Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino.")

#List comprehension, lista de comprension
names = ["Gise","Lucas","Facu","Pepe"]
alongP = [p for p in names if p[0] == 'P'] #Esto regresa una nueva lista
#Solo devuelve los nombres que tienen P
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mx"},
           {"name": "Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

#Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Gisela","Vizcaino") #Hay que pasar los parametros o tira eeror
mi_funcion2("Lucas", "Vizcaino") #Se puede llamar dos veces la funcion

#La palabra return en funciones
#Creamos una funcion para sumar
def sumar(a,b):
    return a + b
resultado = sumar(78,22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')

def sumar2(a: int = 0,b: int = 0): #Valores por default
    return a + b
resultado2 = sumar2()
print(f'Resultado de la suma: {resultado2}') #Da error si no pasamos argumentos
print(f'Resultado de la suma: {sumar2(22,66)}')

#Argumentos, variables en funciones
def listarNombres(*nombres): #Para que varien, y sean muchos, normalmente se usa *args
    for nombre in nombres: #Se convierte en una tupla, xq no pueden modificarse
        print(nombre)
listarNombres('Lucas','Gisela','Facu<3','Cecilia')
listarNombres('Pepe','Pepito','Pepillo') #Se siguen añadiendo a la lista

def listarTerminos(**kwargs): #o **terminos, es para recibir los argumentos
    for llave, valor in kwargs.items(): #Funcion para recorrer diccionarios
        print(f'{llave} : {valor}') #kwargs significa key word argument

listarTerminos(IDE='Integrated Develoment Enviroment',PK='Primaruy Key')
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre) #Adentro ponemos la variable
nombres2 = ['Tito', 'Lucas', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla') #Lo muestra como cadena, uno por uno
#desplegarNombres('10') #Sale error porque es entero, objeto no iterable
desplegarNombres((10,11)) #Se convierte en una tupla iterable
desplegarNombres([22,55]) #La convertimos en una lista

#FUNCIONES RECURSIVAS, necesita un caso base y un caso recursivo
def factorial(numero):
    if numero == 1: #CASO BASE
        return 1
    else:
        return numero * factorial(numero-1) #CASO RECURSIVO

resultado = factorial(5) #Lo hacemos en codigo duro
print(f'El factorial del numero 5 es: {resultado}')










