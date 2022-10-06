#Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
#Hacer un programa donde el usuario ingrese una frase, se le devolvera la
#misma frase pero sin espacios en blanco, y ademas un contador de cuantos
#caracteres tiene la frase (sin contar los espacios en blanco)
#Ejemplo: frase = vivir por siempre en paz
# frase final = vivirporsiempreenpaz
# nº de caracteres = 20

frase = input("Digite una frase: ")
frase2 = " "
for i in frase:
    if i != " ":
        frase2 += i
frase = frase2
print(f'\nLa frase final es: {frase}')
print(f'Nº de caracteres: {len(frase)}') #Muestra la longitud
