from colorama import init, Fore
init()

#Angel Damian Stefan Punoñanco Soto
#Matias Esteban Villacura Figueroa

tablero= {
    "a8":"r",
    "b8":"n",
    "c8":"b",
    "d8":"q",
    "e8":"k",
    "f8":"b",
    "g8":"n",
    "h8":"r",
    "a7":"p",
    "b7":"p",
    "c7":"p",
    "d7":"p",
    "e7":"p",
    "f7":"p",
    "g7":"p",
    "h7":"p",
    "a6":".",
    "b6":".",
    "c6":".",
    "d6":".",
    "e6":".",
    "f6":".",
    "g6":".",
    "h6":".",
    "a5":".",
    "b5":".",
    "c5":".",
    "d5":".",
    "e5":".",
    "f5":".",
    "g5":".",
    "h5":".",
    "a4":".",
    "b4":".",
    "c4":".",
    "d4":".",
    "e4":".",
    "f4":".",
    "g4":".",
    "h4":".",
    "a3":".",
    "b3":".",
    "c3":".",
    "d3":".",
    "e3":".",
    "f3":".",
    "g3":".",
    "h3":".",
    "a2":"P",
    "b2":"P",
    "c2":"P",
    "d2":"P",
    "e2":"P",
    "f2":"P",
    "g2":"P",
    "h2":"P",
    "a1":"R",
    "b1":"N",
    "c1":"B",
    "d1":"Q",
    "e1":"K",
    "f1":"B",
    "g1":"N",
    "h1":"R"
}
contador= 1
piezas_capturadas= []
piezas= []
for fila in range(8,0,-1):
    fila = str(fila)
    for columna in "abcdefgh":
        piezas+= tablero[f"{columna}{fila}"]
        
    print(Fore.MAGENTA + fila+" "+ Fore.WHITE + tablero[f"a{fila}"]+" "+tablero[f"b{fila}"]+" "+tablero[f"c{fila}"]+" "+tablero[f"d{fila}"]+" "+tablero[f"e{fila}"]+" "+tablero[f"f{fila}"]+" "+tablero[f"g{fila}"]+" "+tablero[f"h{fila}"])
print(Fore.MAGENTA + "  a b c d e f g h\n")
print(piezas)
while True:
    posicion= str(input(Fore.WHITE + f"ingrese la casilla inicial: "))
    posicion2= tablero[f"{posicion}"]
    if posicion2 == ".":
        while True:
            print("no hay pieza en esa casilla\n")
            posicion= str(input(f"ingrese la casilla inicial: "))
            if posicion2 != ".":
                break
    #esta parte es para las reglas del peon
    posicion2= tablero[f"{posicion}"]
    destino= str(input(f"ingrese la pocision final: "))
    posicion_D= tablero[f"destino"]
    while posicion2== "P":
        
        contador_del_peonB= list(posicion)
        numero_del_peonB= int(contador_del_peonB[1]) + 2
        numero2_del_peonB= numero_del_peonB -1
        if posicion_D == piezas:
            print("El movimiento es invalido por obstruccion")
            destino= str(input(f"ingrese la pocision final: "))
        if (posicion2 == "P" and numero2_del_peonB==3):
            if destino == f"{str(contador_del_peonB[0] + str(numero_del_peonB))}":
                break
            elif destino == f"{str(contador_del_peonB[0] + str(numero2_del_peonB))}":
                break
            if destino != f"{str(contador_del_peonB[0] + str(numero_del_peonB))}":
                print(f"El movimiento que se ejecuto no es correcto\n")
                destino= str(input(f"ingrese la pocision final: "))
        numero_del_peonB= int(contador_del_peonB[1]) + 1
        if (posicion2 == "P" and numero2_del_peonB!= 3):
            contador_del_peonB= list(posicion)
            numero_del_peonB= int(contador_del_peonB[1]) + 1
            if destino == f"{str(contador_del_peonB[0] + str(numero_del_peonB))}":
                break
            if destino != f"{str(contador_del_peonB[0] + str(numero_del_peonB))}":
                print(f"El movimiento que se ejecuto no es correcto\n")
                destino= str(input(f"ingrese la pocision final: "))
        
        #aqui termina el movimiento del peon blanco
    
    #Movimiento del peon negro
    while posicion2== "p":
        contador_del_peonN= list(posicion)
        numero_del_peonN= int(contador_del_peonN[1]) - 2
        numero2_del_peonN= numero_del_peonN + 1
        if (posicion2 == "p" and numero2_del_peonN==6):
            if destino == f"{str(contador_del_peonN[0] + str(numero_del_peonN))}":
                break
            elif destino == f"{str(contador_del_peonN[0] + str(numero2_del_peonN))}":
                break
            if destino != f"{str(contador_del_peonN[0] + str(numero_del_peonN))}":
                print(f"El movimiento que se ejecuto no es correcto\n")
                destino= str(input(f"ingrese la pocision final: "))
        numero_del_peonN= int(contador_del_peonN[1]) - 1
        if (posicion2 == "p" and numero2_del_peonN!= 6):
            contador_del_peonN= list(posicion)
            numero_del_peonN= int(contador_del_peonN[1]) - 1
            if destino == f"{str(contador_del_peonN[0] + str(numero_del_peonN))}":
                break
            if destino != f"{str(contador_del_peonN[0] + str(numero_del_peonN))}":
                print(f"El movimiento que se ejecuto no es correcto\n")
                destino= str(input(f"ingrese la pocision final: "))
    #aqui termina el movimiento del peon negro


    if tablero[f"{destino}"]!= ".":
        print(f"Capturó a {tablero[f"{destino}"]}")
        piezas_capturadas.append(tablero[f"{destino}"])

    tablero[f"{destino}"]= f"{posicion2}"
    tablero[f"{posicion}"]= "."


    for fila in range(8,0,-1):
        fila = str(fila)
        print(Fore.MAGENTA + fila+" "+ Fore.WHITE + tablero[f"a{fila}"]+" "+tablero[f"b{fila}"]+" "+tablero[f"c{fila}"]+" "+tablero[f"d{fila}"]+" "+tablero[f"e{fila}"]+" "+tablero[f"f{fila}"]+" "+tablero[f"g{fila}"]+" "+tablero[f"h{fila}"])
    print(Fore.MAGENTA + "  a b c d e f g h\n")
    print(Fore.GREEN + f"piezas captiradas: {piezas_capturadas}" + Fore.WHITE)

