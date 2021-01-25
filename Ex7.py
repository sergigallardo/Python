def main():
   n1 = int(input("Introdueix un numero:"))
   n2 = int(input("Introdueix un numero:"))
   n3 = int(input("Introdueix un numero:"))
   if n1==n2==n3:
       r= ((n1+n2+n3)*3)
       print(r)
   else:
       r=(n1+n2+n3)
       print(r)

if __name__ == "__main__":
    main()