numero= int(input("Numero : "))
f=1
if numero != 0:
    for i in range(1, numero+1):
        f *= i
print("Factorial: ",f)