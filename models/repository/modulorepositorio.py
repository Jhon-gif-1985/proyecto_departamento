from models.connexion import Connexion
from models.entity.modulo import Modulo
from sqlite3 import Error

class ModuloRepository():
    
    def save(self, modulo: Modulo):
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        try:
            sql = """"""
            data = (modulo.get_departamento, modulo.get_municipio, modulo.get_sucursal, modulo.get_nombre, modulo.get_codigo)
            cursor.execute(sql, data)
            cnx.commit()
            return True, cursor.lastrowid
        except Error as e:
            print(f"Error=>{e}")    
            return False
        finally:
            if cnx:
                cursor.close()
                cnx.close()