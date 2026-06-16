from colorama import init, Fore
init()

print(Fore.YELLOW + "===== BUCLES =====")

edad= 30
num= 0

#while edad < 18:
#    print("Eres menor de edad, no puedes conducir")

#while True:
#    print(num)
#    num +=2




# Bucle while
# Impresion de numeros de 0 a 100 (incrementando de 2 en 2)

while num <= 100:
    print(num)
    num += 2
print(Fore.RED + "Primer bucle Terminado!")

#impresion del 100 al 200 + condicion else
while num <= 200:
    print(num)
    num += 2
else:
    print("Mi condicion es igual o menor a 200")

# no se puede hacer un elif

print(Fore.CYAN + "Segundo bucle Terminado!")

# Conbinar While con un if dentro
while num <= 300:
    print(num)
    num += 2
    if num == 250:
        print("Mi condicion es igual a 250")
print(Fore.GREEN + "Tercer bucle terminado")

# Utilizando el break
while num <= 400:
    print(num)
    num += 2
    if num == 350:
        print(Fore.MAGENTA + "Se detiene el bucle")
        break
print(num)
print(Fore.MAGENTA + "Cuarto bucle terminado!")

# Utilizar el continuar

num= 0
while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)

# bucle infinito + break
while True:
    parametro = input("ingrese la palabra secreta>")
    if parametro == "exit":
        break
    else:
        print(parametro)

# Bucle FOR
# For n°1

print(Fore.GREEN + "===== BUCLE FOR =====")
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

print(Fore.CYAN + "===== BUCLE FOR =====")
listita= [1,2,3,4,5,6,7,8,9,10]
for i in listita:
    print(i)

print(Fore.MAGENTA + "===== BUCLE FOR =====")
for i in range(1,101):
    print(i)