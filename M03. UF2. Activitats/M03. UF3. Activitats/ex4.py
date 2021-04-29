#Una empresa de publicitat ens ha demanat un programa per a analitzar les seves campanyes de màrketing. En concret, per a la primera campanya,
#ens demanen treballar amb una sèrie de dades dels vídeos publicats.
#Així, cal implementar un programa que demani per teclat:
#1.Quants vídeos vol introduir i per a cada vídeo, emmagatzemar:
        #a.Identificador (numèric)
        #b.Grup/cantant (text)
        #c.Nom de la cançó (text)
        #d.Data de publicació (text en format dd/mm/yyyy)
        #e.Nombre de visualitzacions (numèric)
#2.Validar que les dades introduïdes tenen el format correcte
#3.Mostri les dades tabulades i permeti mostra-les segons l’índex introduït per teclat


def formulari():
    capçalera = ["id", "grup", "nom_canço", "data", "num_visualitzacions"]
    a = []
    b = []
    c = []
    d = []
    e = []
    n_videos = int(input("Introdueix el numeros que vols introduir:"))
    for i in range(n_videos):
        a.append(int(input("Introdueix el ID numeric:\n")))
        b.append(input("Introdueix el grup/cantant:\n"))
        c.append(input("Nom de la canço:\n"))
        d.append(input("Introdueix una data:\n"))
        e.append(int(input("Numero de visualitzacions\n")))

    print("id\tgrup\tnom_canço\tdata\tnum_visualitzacions")
    for i in range (n_videos):
        print(a[i],b[i],c[i],d[i],e[i])

def main():
    formulari()
if __name__ == '__main__':
        main()