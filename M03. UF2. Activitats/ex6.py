def gran():
    print(max([5, 10, 15, 2, 25, 30, 35, 40]))
    return
def petit():
    print(min([5, 10, 15, 2, 25, 30, 35, 40]))
    return
def main():
    llista = [5, 10, 15, 2, 25, 30, 35, 40]
    print(llista)
    print("El valor mes gran de la llista es:")
    print(gran())
    print("El valor mes petit de la llista es:")
    print(petit())
if __name__ == '__main__':
    main()