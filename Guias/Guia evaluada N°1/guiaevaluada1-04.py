#Angel Damian Stefan Punoñanco Soto
#Matias Esteban Villacura Figueroa

num = int(input(f"ingrese el numero del cubo final que desea imprimir: "))

impar=1
sumas = ""

for i in range(1, num+1):
    sumas= str(impar)
    impar+= 2
    for n in range(i):
        if n < i-1:
            sumas += "+"
            sumas += str(impar)
            impar +=2
    resultado = i**3
    print(f"{i}^3 = {sumas} = {resultado}")