def main():
    num=int(0)
    while  num < 11:
        for i in range(0,11):
            result=i*num
            print(("%d x %d = %d")%(num,i,result))
        num+= 1
if __name__ == "__main__":
    main()