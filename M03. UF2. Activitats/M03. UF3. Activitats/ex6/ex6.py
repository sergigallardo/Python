#6. Implementa el programa que crearà la base de dades i la taula corresponent a l’estructura definida a l’exercici 6
#   i que insereixi els valors introduïts per teclat (si ja s’ha executat el programa, no cal tornar a crear la bbdd
#   i la taula). Adjunta l’esquema que defineix la bbdd. Utilitza els següents valors per a la configuració de la bbdd:
#       a. db: db_campaign
#       b. user: admin_campaign
#       c. password: 4dm1n_c4mp41gn
#       d. table: tb_video


import pandas as pd
import csv
import functions as f

def main():
    f.create_db()
    f.create_table()
    f.insert_data()
if __name__ == '__main__':
    main()
