def main():
    num = int(input("Introdueix el numero de bytes:"))
    
    res = num / 1000*1
    
    print("Resposta:{0}MB".format(res))
    

if __name__ == "__main__":
    main()