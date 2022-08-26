#EJERCICIO 4: Suponga que se tiene un conjunto de calificaciones de un
#grupo de 10 alumnos. Realizar un algoritmo para calcular la calificacion
#promedio y la calificacion mas baja de todo el grupo.

calificacion_promedio = 0
calificacion_baja = 0
suma_calificaciones = 0

for i in range(10):
    calificacion = int(input("Digite una calificacion: "))
    suma_calificaciones += calificacion
    calificacion_promedio = (suma_calificaciones/10)
    if calificacion < 5:
        calificacion_baja = calificacion

print("El promedio de las calificaciones es : ",calificacion_promedio)
print("La calificacion mas baja es: ", calificacion_baja)