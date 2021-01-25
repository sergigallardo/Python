def main():
    while True:
        num = int(input("Introdueix un numero:"))

        if num>=0 and num<=10:
            print("Correcte")
            break
        else:
            num=int(input("Error! introdueix un altre numero:"))

if __name__ == "__main__":
    main()