def llista():
    a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    b = list(dict.fromkeys(a))
    return b
def main():
    print(llista())

if __name__ == '__main__':
    main()