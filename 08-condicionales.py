from colorama import init, Fore
init()

print(Fore.RED + "Texto Rojo")
print(Fore.MAGENTA + "Texto magenta")


print(Fore.MAGENTA + "\n===== UTILIZANDO IF Y ELSE =====")

licencia= False
edad= 19
automovil= True

if licencia and edad >= 18:
    print(Fore.YELLOW + "Puede conducir un automovil")
else:
    print(Fore.YELLOW + "No puede conducir un automovil")


if licencia and edad >= 18:
    print(Fore.CYAN + "Puede conducir un automovil")
elif automovil: # En otros lenguajes como C, elif = else if
    print(Fore.BLUE + "Tengo automovil, pero no tengo la edad ni la licencia necesaria")
else:
    print(Fore.RED + "no puedo conducir, ya que no tengo la edad, ni licencia, ni automovil")