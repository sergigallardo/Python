#Implementa un programa per a mostrar els múltiples d'un número.
        # El programa haurà de fer el següent:
            #A.demanar a l'usuari que introdueixi un número sencer de 1 a 20 i validar-ho.
            #B.mostrar els múltiples entre 0 i 100 del nombre introduït.
import mult as mult


def validacio():
    # Validació del numero introduit.
    num = int(input('Introdueix un numero sencer del 1 al 20:'))

    while num < 1 or num > 20:
        num = int(input('Introdueix un numero sencer del 1 al 20:'))

    return num


def main():

    num = validacio()

    print(num)
    # Multiples del numero introduit per el usuari entre 0 i 100.
    print([ x * num for x in range(100) if (x*num) < 100])


if __name__ == '__main__':
    main()