def main():
    val1 = int(input("Introdueix un valor per val1:"))#Input de val1
    val2 = int(input("Introdueix un valor per val2:"))#Input de val2

    print("val1=%d  val2=%d" %(val1,val2)) #Mostra els valors introduits.
    op = val1
    val1 = val2
    val2 = op

    print("val1=%d  val2=%d" %(val1,val2)) #Mostra els valors ja intercambiats

if __name__ == "__main__":
    main()