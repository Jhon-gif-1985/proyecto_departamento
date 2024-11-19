from models.connexion import Connexion
from sqlite3 import Error

from models.dtos.viewsucursal import SucursalDto
from models.entity.sucursal import Sucursal

class SucursalRepository():
    
    def get_all(self)-> list[Sucursal]:        
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        list_datos = []
        sql = '''SELECT ID, ID_DPTO, ID_CIUDAD, SUCURSAL, DIRECCION, TELEFONO, OBSERVACIONES, ESTADO FROM Sucursales ORDER BY SUCURSAL'''
        try:                 
            cursor.execute(sql)
            objects = cursor.fetchall()
            for sucursal in objects:
                list_datos.append(Sucursal(sucursal[0], sucursal[1], sucursal[2], sucursal[3], sucursal[4], sucursal[5], sucursal[6], sucursal[7]))
            return list_datos
        except Error as e:
            print(f"Error=>{e}") 
        except Exception as ex:
            print(f"ok un error del tipo:{ex}")                              
        finally:            
            if cnx:
                cursor.close()
                cnx.close()

    def save(self, objeto: Sucursal):
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        try:
            sql = """INSERT INTO Sucursales (ID_DPTO, ID_CIUDAD, SUCURSAL, DIRECCION, TELEFONO, OBSERVACIONES, ESTADO) VALUES (?,?,?,?,?,?,?)"""
            data = (objeto.get_dpto(), objeto.get_ciudad(), objeto.get_sucursal(), objeto.get_direccion(), objeto.get_telefono(), objeto.get_observaciones(), 1)            
            cursor.execute(sql, data)
            cnx.commit()
            return True, cursor.lastrowid
        except Error as e:
            print(f"Error=>{e}")    
            return False, -1
        finally:
            if cnx:
                cursor.close()
                cnx.close()


    def get_data_all(self)-> list[SucursalDto]:
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        list_datos = []
        sql = '''SELECT ID, ID_DPTO, DEPARTAMENTO, ID_CIUDAD, CIUDAD, SUCURSAL, DIRECCION, TELEFONO, OBSERVACIONES, ESTADO FROM VW_SUCURSALES ORDER BY SUCURSAL'''
        try:
            cursor.execute(sql)
            objects = cursor.fetchall()
            for sucursal in objects:
                list_datos.append(SucursalDto(sucursal[0], sucursal[1], sucursal[2], sucursal[3], sucursal[4], sucursal[5], sucursal[6], sucursal[7], sucursal[8], sucursal[9]))
            return list_datos
        except Error as e:
            print(f"Error=>{e}")
        except Exception as ex:
            print(f"ok un error del tipo:{ex}")
        finally:
            if cnx:
                cursor.close()
                cnx.close()