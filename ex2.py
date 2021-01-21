def main():
    n1 = int(input("Introdueix un numero:"))
    n2 = int(input("Introdueix un altre numero:"))
    
    s = max(n1, n2)
    g = min(n1, n2)
    
    while g!=0:
        op = g
        g = s%g
        s = op
    print("EL MAXIM COMU DIVISOR ENTRE {0} i {1} es: {2}".format(n1, n2, op))
    
if __name__ == "__main__":
    main()