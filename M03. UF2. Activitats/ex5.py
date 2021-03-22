def benvinguda():#Funcio que printa el missatge de benvinguda.
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
def menu():#Funcio printar opcions menu.
    print("|\t\tSelecciona una opcio: \t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t1.-OPCIO \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t2.-OPCIO \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t3.-OPCIO \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t4.-OPCIO \t\t\t\t\t\t\t\t\t\t\t\t\t|")
    print("|\t\t_____________________________________________________\t\t|")
def seleccio():#Funcio que determina quina opcio ha escollit l'usuari.
    sel = int(input("|\t\tSeleccio: \t\t\t\t\t\t\t\t\t\t\t\t\t|"))
    if sel == 1:
        print("Opció1")
    else:
        if sel == 2:
            print("Opció2")
        else:
            if sel == 3:
                print("Opció3")
            else:
                if sel == 4:
                    print("Opció4")
def main():
    print(benvinguda())
    print(menu())
    print(seleccio())
if __name__ == '__main__':
    main()