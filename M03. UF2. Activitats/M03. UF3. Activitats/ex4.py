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


import pandas as pd

def formulari():
    capçalera = ("id\tgrup\tnom_canço\tdata\tnum_visualitzacions")
    n_videos = int(input("Introdueix el numeros que vols introduir:"))
    pd.a = []
    pd.b = []
    pd.c = []
    pd.d = []
    pd.e = []

    for i in range(n_videos):
        pd.a.append(int(input("Introdueix el ID numeric:\n")))
        pd.b.append(input("Introdueix el grup/cantant:\n"))
        pd.c.append(input("Nom de la canço:\n"))
        pd.d.append(input("Introdueix una data:\n"))
        pd.e.append(int(input("Numero de visualitzacions:\n")))
    print("---------------------------------------------------")
    print(capçalera)
    print("---------------------------------------------------")
    for i in range(n_videos):
        print(pd.a[i], pd.b[i], pd.c[i], pd.d[i], pd.e[i])
        print("---------------------------------------------------")

def main():
    formulari()

if __name__ == '__main__':
    main()
