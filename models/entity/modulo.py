class Modulo():
    def __init__(self, departamento: int, municipio: int, sucursal: int, nombre: str, codigo: str):
        self.__dpto = departamento
        self.__municipio = municipio
        self.__sucursal = sucursal
        self.__nombre = nombre
        self.__codigo = codigo
        
    def get_departamento(self):
        return self.__dpto
    
    def get_municipio(self):
        return self.__municipio
    
    def get_sucursal(self):
        return self.__sucursal
    
    def get_nombre(self):
        return self.__nombre
    
    def get_codigo(self):
        return self.__codigo 
    
    def set_departamento(self, departamento):
        self.__dpto = departamento
    
    def set_municipio(self, municipio):
        self.__municipio = municipio
    
    def set_sucursal(self, sucursal):
        self.__sucursal = sucursal
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_codigo(self, codigo):
        self.__codigo = codigo      