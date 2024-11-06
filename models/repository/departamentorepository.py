from models.connexion import Connexion
from models.dtos.viewciudaddto import ViewCityDto
from models.entity.departamento import Departamento
from sqlite3 import Error

class DepartamentoRepository():
    
    def get_all(self)-> list[Departamento]:        
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        list_dpto = []
        sql = '''SELECT ID, CODIGO, NOMBRE, ESTADO FROM Departamento ORDER BY NOMBRE'''
        try:                 
            cursor.execute(sql)
            objects = cursor.fetchall()
            for departamento in objects:
                list_dpto.append(Departamento(departamento[0], departamento[1], departamento[2], departamento[3]))
            return list_dpto
        except Error as e:
            print(f"Error=>{e}") 
        except Exception as ex:
            print(f"ok un error del tipo:{ex}")                              
        finally:            
            if cnx:
                cursor.close()
                cnx.close()
                
    def get_by_id(self, id)->Departamento: # 1 AND DELETE
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        sql = '''SELECT ID, CODIGO, NOMBRE, ESTADO FROM Departamento WHERE ID = ?'''
        try:            
            cursor.execute(sql,(id,))
            objects = cursor.fetchone()
            
            return Departamento(objects[0], objects[1], objects[2], objects[3])
        except Error as e:
            print(f"Error=>{e}")                
        finally:
            if cnx:
                cursor.close()
                cnx.close()   
                
    def get_by_codigo(self, codigo):
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        sql = '''SELECT ID, CODIGO, NOMBRE, ESTADO FROM Departamento WHERE CODIGO = ?'''
        try:            
            cursor.execute(sql, (codigo,))
            objects = cursor.fetchone()
            return objects
        except Error as e:
            print(f"Error=>{e}")     
        finally:
            if cnx:
                cursor.close()
                cnx.close() 
                
    def get_by_nombre(self, nombre)-> Departamento:
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        sql = '''SELECT ID, CODIGO, NOMBRE, ESTADO FROM Departamento WHERE NOMBRE = ?'''
        try:            
            cursor.execute(sql, (nombre,))
            objects = cursor.fetchone()
            dpartamento = Departamento(objects[0], objects[1], objects[2], objects[3])
            return dpartamento
        except Error as e:
            print(f"Error=>{e}")     
        finally:
            if cnx:
                cursor.close()
                cnx.close()                                      
    
    def get_all_city_by_dpto(self, departamento:str)->list[ViewCityDto]:
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        listciudad = []
        sql = '''SELECT COD_DPTO, ID_CIUDAD, COD_CIUDAD, CIUDAD FROM Location WHERE DEPARTAMENTO = ? AND ESTADO_DPTO=1 AND ESTADO_CIUDAD=1'''
        try:            
            cursor.execute(sql, (departamento,))
            objects = cursor.fetchall()
            for ciudad in objects:
                listciudad.append(ViewCityDto(ciudad[0], ciudad[1], ciudad[2], ciudad[3]))
            return listciudad
        except Error as e:
            print(f"Error=>{e}")     
        finally:
            if cnx:
                cursor.close()
                cnx.close() 
                
    def get_city_by_dpto_bynombre_ciudad(self, departamento:str, ciudad: str)->ViewCityDto:
        cnx = Connexion().getconexion()
        cursor = cnx.cursor()
        
        sql = '''SELECT COD_DPTO, ID_CIUDAD, COD_CIUDAD, CIUDAD FROM Location WHERE DEPARTAMENTO = ? AND CIUDAD=? AND ESTADO_DPTO=1 AND ESTADO_CIUDAD=1'''
        try:            
            cursor.execute(sql, (departamento, ciudad,))
            objects = cursor.fetchone()
            resultado = ViewCityDto(objects[0], objects[1], objects[2], objects[3])
            return resultado
        except Error as e:
            print(f"Error=>{e}")     
        finally:
            if cnx:
                cursor.close()
                cnx.close()                                