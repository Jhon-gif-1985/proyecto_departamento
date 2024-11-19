class SucursalDto():

    def __init__(self, id: int, id_dpto: int, departamento: str, id_ciudad: int, ciudad: str, sucursal: str, direccion: str, telefono: str,
                 observaciones: str, estado: int):
        self.__id = id
        self.__iddpto = id_dpto
        self.__departamento = departamento
        self.__idciudad = id_ciudad
        self.__ciudad = ciudad
        self.__sucursal = sucursal
        self.__direccion = direccion
        self.__telefono = telefono
        self.__observaciones = observaciones
        self.__estado = estado

    def get_id(self):
        return self.__id

    def get_dpto(self):
        return self.__iddpto

    def get_departamento(self):
        return self.__departamento
    def get_ciudad(self):
        return self.__idciudad

    def get_ciudad(self):
        return self.__ciudad
    def get_sucursal(self):
        return self.__sucursal

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_observaciones(self):
        return self.__observaciones

    def get_estado(self):
        return self.__estado