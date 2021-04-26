#Implementa un programa que mostri un menú amb les següents opcions:
#a.Crear un fitxer (demanant el nom del fitxer a l’usuari per teclat)
#b.Mostrar el contingut d’un fitxer per pantalla (demanant el nom del fitxer a l’usuari per teclat)
#c.Modificar el contingut d’un fitxer demanant el nom del fitxer a l’usuari per teclat)
#d.Sortir

def benvinguda():
    print("_____________________________________________________________________")
    print("|\t\t                                                     \t\t|")
    print("|\t\t______                 _                   _     _ _ \t\t|")
    print("|\t\t| ___ \               (_)                 | |   | | |\t\t|")
    print("|\t\t| |_/ / ___ _ ____   ___ _ __   __ _ _   _| |_  | | |\t\t|")
    print("|\t\t| ___ \/ _ \ '_ \ \ / / | '_ \ / _` | | | | __| | | |\t\t|")
    print("|\t\t| |_/ /  __/ | | \ V /| | | | | (_| | |_| | |_  |_|_|\t\t|")
    print("|\t\t\____/ \___|_| |_|\_/ |_|_| |_|\__, |\__,_|\__| (_|_)\t\t|")
    print("|\t\t                                __/ |                \t\t|")
    print("|\t\t                               |___/                 \t\t|")
    print("|\t\t_____________________________________________________\t\t|")
def menu():
    print("|\t\tSelecciona una opcio: \t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t1.-CREAR \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t2.-MOSTRAR \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t3.-ESCRIURE \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t4.-SORTIR \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t_____________________________________________________\t\t|")
def crear():
    route = input("Introdueix la ruta i nom del fitxer que vols crear [ruta/nomfitxer.extensió]:")
    f = open(route, "a")
def mostrar():
    route = input("Introdueix la ruta i nom del fitxer que vols escriure[ruta/nomfitxer.extensió]:")
    f = open(route, "r")
    print(f.read())
    f.close()
def escriure():
    route = input("Introdueix la ruta i nom del fitxer que vols escriure[ruta/nomfitxer.extensió]:")
    f = open(route, "w")
    str = input("Introdueix un text: ")[:100]
    f.write(str)
    f.close()
def seleccio():
    sel = int(input("|\t\tSeleccio: \t\t\t\t\t\t\t\t\t\t\t\t\t|"))
    if sel == 1:
        crear()
    else:
        if sel == 2:
            mostrar()
        else:
            if sel == 3:
                escriure()
            else:
                if sel == 4:
                    print("Exit...")
def main():
    print(benvinguda())
    print(menu())
    print(seleccio())
if __name__ == '__main__':
    main()