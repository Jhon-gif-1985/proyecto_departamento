import os

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

from models.repository.sucursalesrepository import SucursalRepository
from views.FrmSucursales import Ui_FrmSucursales


class Sucursales(QWidget, Ui_FrmSucursales):
    def __init__(self):
        super().__init__()
        self.repository = SucursalRepository()
        self.setupUi(self)
        self.config_table()
        self.data_sucursales = self.repository.get_data_all()
        self.poblar_tabla(self.data_sucursales)


    def config_table(self):
        columnas = ("ID", "DEPARTAMENTO", "CIUDAD", "SUCURSAL",  "DIRECCION", "TELEFONO", "OBSERVACIONES")
        self.tblSucursales.setColumnCount(len(columnas))
        self.tblSucursales.setHorizontalHeaderLabels(columnas)


    def poblar_tabla(self, data):
        if data is None:
            data = []
        self.tblSucursales.setRowCount(len(data))
        fila = 0
        for row in data:
            print(row.get_id())
            self.tblSucursales.setItem(fila, 0, QTableWidgetItem(str(row.get_id())))
            self.tblSucursales.setItem(fila, 1, QTableWidgetItem(str(row.get_departamento())))
            self.tblSucursales.setItem(fila, 2, QTableWidgetItem(str(row.get_ciudad())))
            self.tblSucursales.setItem(fila, 3, QTableWidgetItem(str(row.get_sucursal())))
            self.tblSucursales.setItem(fila, 4, QTableWidgetItem(str(row.get_direccion())))
            self.tblSucursales.setItem(fila, 5, QTableWidgetItem(str(row.get_telefono())))
            self.tblSucursales.setItem(fila, 6, QTableWidgetItem(str(row.get_observaciones())))
            fila = fila + 1

        self.tblSucursales.resizeColumnsToContents()
        
        