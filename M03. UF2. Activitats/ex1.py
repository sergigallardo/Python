def valors(num):
    x = 0
    SUMA=0
    list = []
    while x != num:
        # Input valors per llistar i sumar.
        val = int(input("Introdueix un valor:"))
        list.append(val)
        # Variable per anar suman al mateix temps que s'introdueixen.
        SUMA = SUMA + val
        #Variable x va suman 1 per anar avançant per la llista.
        x = x + 1
    return SUMA

def main():
    # Input número de valors que vol introduir.
    num = int(input("Introdueix el numero de valors que vols introduir:"))
    print(valors(num))#print final.
if __name__ == '__main__':
    main()
