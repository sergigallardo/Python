def main():
    u = 0
    num = []
    x = 10
    while (u < x):
        z = int(input('Introdueix un numero:'))
        num.append(z)
        u += 1

    def calc(num, x):
        w = sum(num)
        v = w / x
        return (v)

    print('Mitjana = ', calc(num, x))
    
if __name__ == "__main__":
    main()