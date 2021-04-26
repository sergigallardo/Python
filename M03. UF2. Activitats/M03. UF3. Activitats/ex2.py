#Implementa un programa que demani un text (no més de 100 caràcters)
# a l’usuari i l’afegeixi al fitxer creat en l’activitat anterior.


def writefile(filename):
    f = open(filename, "a")
    str = input("Introdueix un text: ")[:100]
    f.write(str)
    print(str)
    f.close()



def main():
    writefile('files/text.txt')

if __name__ == '__main__':
    main()