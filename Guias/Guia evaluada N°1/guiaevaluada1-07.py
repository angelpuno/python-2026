#Angel Damian Stefan Punoñanco Soto
#Matias Esteban Villacura Figueroa

n= int(input("ingrese el numero n: "))
multiplicaciones= ""
numeros= n
resultado= 0
if n== 0:

    print(f"{n}! = 1")
elif n>= 1:

    multiplicaciones+= str(numeros)
    resultado= numeros
    for i in range(1,n):

        multiplicaciones+= "*"
        numeros-= 1
        multiplicaciones+= str(numeros)
        resultado= resultado*numeros
    
    print(f"{n}! = {multiplicaciones}")
    print(f"Resultado: {resultado}")