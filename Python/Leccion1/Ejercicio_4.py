#Ejercicio: Etapas de la vida

edad = int(input("Digite su edad"))
if (edad >= 0 and edad <= 10) :
    print(f"La infancia es increible y bella ")
elif (edad >= 10 and edad <= 19) :
    print(f"Tienes muchos cambios, mucho que estudiar")
elif (edad >= 20 and edad <= 29) :
    print(f"Amor y comienza el trabajo")
elif( edad >= 30 and edad <= 39) :
    print(f"Estabilidad economica ojala")
elif( edad >=40 and edad <= 49) :
    print(f"No se, pero ya te estas poniendo viejo")
elif (edad >=50 and edad <=59) :
    print(f"Mas viejo, asique aprovecha a hacer lo que quieras")
elif(edad >=60 and edad <=69) :
    print(f"Jubilado")
elif(edad >=70 and edad <=90) :
    print(f"Tus hijos ya te pusieron en un geriatrico ndea")
elif(edad >=91 and edad <=110) :
    print(f"Fin del juego")
else:
    print ("Sos un fosil")