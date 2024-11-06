import sqlite3
import os


class Connexion:
    def __init__(self):
        try:
            self.__conexion_db = sqlite3.connect(os.path.join('models', 'dsklibrary.db'))
        except Exception as ex:
            print(f"Existe un error al conectarse a la base de datos: {ex}")

    def getconexion(self):
        return self.__conexion_db
