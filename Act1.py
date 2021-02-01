#Implementa una aplicació que demani (i validi)
#les següents dades per teclat (registre):
#   - aula:numeric(entre 1 i 50)
#   - nom aula:text
#   - ip:text
#   - nombre pcs: numeric(entre 1 i 20)
#Demanar quants registres vol introduir  i mostran els resultat en format taula.

def main():
    register = int(input("Introdueix el numero de registres que vols entrar:"))
    c = 0
    while (c < register):
        c1= int(input("Introdueix el numero d'aula:"))
        c2= input("Introdueix el nom d'aula:")
        c3= input("Introdueix l'IP de l'aula")
        c4= int(input("Introdueix el nombre de PC's:"))
        c += 1
    print("nºAula\t\tnom\t\tIP\t\tnºPC")
    print("%d\t\t\t%s\t\t%s\t%d" %(c1,c2,c3,c4))

if __name__ == "__main__":
    main()