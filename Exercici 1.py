def main():
   num1 = int(input("Introdueix el valor numeric d'inici:"))
   num2 = int(input("Introdueix el valor numeric final:"))

    if num1 < num2:
        print(list(range(num1,num2 + 1)))
    else:
        print(list(range(num1,num2 - 1, -1)))


if __name__ == "__main__":
    main()