def llista():
    num = []
    x = 1

    while x < 146:
        if x % 2 == 0:
            y = x // 5
            num.append(y)
        else:
            y = x * 2
            num.append(y)
        x = x + 1
    return num

def main():

    print(llista())

if __name__ == '__main__':
   main()
