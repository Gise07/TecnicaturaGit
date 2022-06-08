#Ejercicio Sistema de calificaciones

num = int(input("Digite una calificacion"))
texto = ""
if ( num == 9 or num == 10) :
    texto = "A"
if ( num == 8 or num <9):
    texto = "B"
if ( num == 7 or num <8):
    texto = "C"
if ( num == 6 or num < 7):
    texto = "D"
if ( num >= 0 and num <= 6):
    texto = "F"
print(f"Su calificacion es {texto}")
