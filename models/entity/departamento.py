class Departamento():
    
    def __init__(self, id: int, codigo: str, nombre: str, estado: int):
        self.__id = id
        self.__codigo = codigo
        self.__nombre = nombre
        self.__estado = estado
        
    def get_id(self):
        return self.__id;    
    
    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_estado(self):
        return self.__estado
    
    def set_id(self, id):
        self.__id = id;    
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_nombre(self, nombre):
         self.__nombre = nombre
    
    def set_estado(self, estado):
        self.__estado = estado
        
    def __str__(self):
        return f"{self.__id}, {self.__codigo}, {self.__nombre}, {self.__estado}"  
            