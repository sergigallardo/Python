#Implementa un programa que llegeixi les dades del document “projects_board.csv” (carpeta Python - Ex.5)
# i mostri per pantalla quants projectes conté el document i quin és el total que facturarà l’empresa.

import pandas as pd
import csv
def read_pandas():
    csvreader = pd.read_csv("files/projects_board.csv")
    print(csvreader)

def read_csv():
    with open('files/projects_board.csv') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        for row in read_csv:
            print(row)

def main():
    read_pandas()
    read_csv()
if __name__ == '__main__':
    main()