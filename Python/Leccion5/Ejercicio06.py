#Ejercicio6: Tabla de multiplicar
#Hacer un programa que pida un numero por teclado y guarde
#en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
#si digita el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50

numero = int(input('Digite un numero: '))
lista = [] #Creamos una lista vacia
for i in range(1,11):
    lista.append(i*numero)
print(f'\nTabla de multiplicar del numero: {numero}: \n {lista}')

for indice,i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}')
#Este cuclo es para ver el formate de una tabla de multiplicar
