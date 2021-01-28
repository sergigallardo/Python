def main():
    seg=int(input("Introdueix el numero de segons:"))

    d= int(seg/86400)

    h = int(seg / 3600)
    seg -= h * 3600
    min = int(seg / 60)
    seg -= min * 60

    print("%sd:%sh:%smin:%sseg" % (d,h, min, seg))
if __name__ == "__main__":
    main()