import pandas as pd
import mysql.connector
from mysql.connector import errorcode

connection_args = {
    'host': 'mysql-sergi.alwaysdata.net',
    'user': 'sergi_asix',
    'password': '@MVM2016'
}


def create_db():
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = "Create database if not exists sergi_ex6"
        # creem el cursor, executem la sentència i fem commit
        crs = cnx.cursor()
        crs.execute(sql)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        # s'executarà només si try no genera excepció
        cnx.close()


def create_table():
    # afegim al dictionary a quina bbdd volem accedir
    connection_args.update({'database': 'sergi_ex6'})
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        table = (
            "CREATE TABLE IF NOT EXISTS `grades` ("
            "  `ID` int(11) NOT NULL AUTO_INCREMENT,"
            "  `group_name` varchar(40) NOT NULL,"
            "  `song_name` varchar(60) NOT NULL,"
            "  `date` varchar(20) NOT NULL,"
            "  `grade` int(2) NOT NULL,"
            "  PRIMARY KEY (`ID`)"
            ") ENGINE=InnoDB")
        '''creem el cursor,
        executem la sentència i fem commit
        '''
        crs = cnx.cursor()
        crs.execute(table)
        cnx.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrasenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()


def insert_data():
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("INSERT INTO grades "
               "(ID,group_name,song_name,date,views) "
               "VALUES (%s, %s, %s, %s, %s)")
        # indiquem els valors (tupla) que han de substituir els placeholders (%s)
        pd.a = []
        pd.b = []
        pd.c = []
        pd.d = []
        pd.e = []
        n_videos = int(input("Introdueix el numero de videos  que vols introduir:"))

        for i in range(n_videos):
            pd.a.append(int(input("Introdueix el ID numeric:\n")))
            pd.b.append(input("Introdueix el grup/cantant:\n"))
            pd.c.append(input("Nom de la canço:\n"))
            pd.d.append(input("Introdueix una data:\n"))
            pd.e.append(int(input("Numero de visualitzacions:\n")))

        data = (pd.a[i], pd.b[i], pd.c[i], pd.d[i], pd.e[i])
        # creem el cursor, executem la sentència (passant la tupla també) i fem commit
        crs = cnx.cursor()
        crs.execute(sql, data)
        cnx.commit()
        # mostra per pantalla quants registres s'han inserit
        print(crs.rowcount, "registres inserits.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()


def select_data():
    try:
        # obrim connexió a la bbdd amb els paràmetres de connection_args
        cnx = mysql.connector.connect(**connection_args)
        # definim la sentència sql per a crear la bbdd
        sql = ("SELECT * FROM grades")
        # creem el cursor, executem la sentència i fem fetchall (per obtenir tots els registres)
        crs = cnx.cursor()
        crs.execute(sql)
        result = crs.fetchall()
        # mostra tots els resultats
        for x in result:
            print(x)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuari o contrassenya incorrectes")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de dades indicada no existeix")
        else:
            print(err)
    else:
        cnx.close()