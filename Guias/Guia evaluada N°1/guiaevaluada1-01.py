#Angel Damian Stefan Punoñanco Soto
#Matias Esteban Villacura Figueroa

parrafo= input("Ingrese el texto: \n")
parrafo= parrafo.replace(",", "")
parrafo= parrafo.replace(".", "")
parrafo= parrafo.replace(":", "")
parrafo= parrafo.replace(";", "")
lista_palabras= parrafo.split()

palabra= input("\ningrese una palabra a buscar en el texto: \n")
print(f"Hay {lista_palabras.count(palabra)} *{palabra}* en el texto")

