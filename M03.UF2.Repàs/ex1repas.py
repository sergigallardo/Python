
def registre(num):
    id = []  # Llista per emmagatzemar ID alumnes.
    names = []  # Llista per emmagatzemar els noms dels alumnes.
    lasts = []  # Llista per emmagatzemar els cognoms dels alumnes.
    subjects = []  # Llista per emmagatzemar assignatures.
    grades = []  # Llista per emmagatzemar les notes.

    for x in range(num):
        y = int(input("Introdueix el ID del alumne:"))
        id.append(y)
        y = input("Introdueix el nom del alumne:")
        names.append(y)
        y = input("Introdueix els cognoms del alumne:")
        lasts.append(y)
        y = input("Introdueix el nom o el identificador de la assignatura:")
        subjects.append(y)
        y = float(input("Introdueix la nota de la assignatura:"))
        grades.append(y)
    print("ID Nom Cognoms Assig Nota")

    for x in range(num):
        print(id[x], names[x], lasts[x], subjects[x], grades[x])

def main():

    num = int(input("Quants alumnes vols registrar:")) #Numero de registres que vol introduir l'usuari.
    print(registre(num))

if __name__ == '__main__':
    main()