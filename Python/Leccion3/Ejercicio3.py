#Ejercicio 3: Leer 10 numeros e imprimir cuantos son positivos,
#cuantos negativos y cuantos neutros.

conteo_positivos = 0
conteo_negativos = 0
conteo_neutros = 0

for i in range(10):
    num = int(input("Digite un numero: "))
    if num == 0:
        conteo_neutros += 1
    else:
        if num > 0 :
            conteo_positivos += 1
        else:
            conteo_negativos += 1
    print(f"La cantidad de positivos es : {conteo_positivos}")
    print(f"La cantidad de negativos es: {conteo_negativos}")
    print(f"La cantidad de neutros es: {conteo_neutros}")
