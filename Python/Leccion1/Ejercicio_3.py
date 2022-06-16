#Ejercicio 3: Calcular estacion del año

mesDelAño = int(input("Digite un mes del año"))
if (mesDelAño >= 1 and mesDelAño <= 3) :
    print(f"La estacion del año es verano")
elif (mesDelAño >= 4 and mesDelAño <= 6) :
    print(f"La estacion del año es otoño")
elif (mesDelAño >= 7 and mesDelAño <= 9) :
    print(f"La estacion del año es invierno")
elif( mesDelAño >= 10 and mesDelAño <= 12) :
    print(f"La estacion del año es primavera")
else:
    print ("No es un numero valido, digite un numero entre el 1 y el 12")
