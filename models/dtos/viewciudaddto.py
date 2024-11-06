

class ViewCityDto():
    def __init__(self, cod_dpto: str, id_ciudad: int, cod_ciudad: str, nombre_ciudad: str):
        self.__coddpto = cod_dpto
        self.__idciudad = id_ciudad
        self.__codciudad = cod_ciudad
        self.__nombre = nombre_ciudad
        
    
    def get_coddpto(self):
        return self.__coddpto
    
    def get_idciudad(self):
        return self.__idciudad
    
    def get_codciudad(self):
        return self.__codciudad
    
    def get_nombreciudad(self):
        return self.__nombre    