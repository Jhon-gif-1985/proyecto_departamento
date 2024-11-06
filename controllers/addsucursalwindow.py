import os

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView

from models.repository.departamentorepository import DepartamentoRepository
from views.FrmAddSucursal_view import Ui_FrmAddSucursal

class AddSucursalWindow(QWidget, Ui_FrmAddSucursal):
    def __init__(self):
        super().__init__()
        
        # Utilizamos el setupUI para definir todos los objetos
        self.setupUi(self)
        self.poblar_departamento()
        
        self.cboDepartamento.currentIndexChanged.connect(self.select_dpto)
        self.cboCiudad.currentIndexChanged.connect(self.select_ciudad)
        self.btnCancelar.clicked.connect(self.close)
        self.btnGuardar.clicked.connect(self.guardar)
        
        
            
            
    def poblar_departamento(self):
        repo_departamento = DepartamentoRepository()
        list_dptos = repo_departamento.get_all()
        ## poblar un combobox
        self.cboDepartamento.addItem('Seleccione una opción') 
        for dpto in list_dptos:
            self.cboDepartamento.addItem(dpto.get_nombre())  
            
    def poblar_ciudades(self, dpto:str):
        self.cboCiudad.clear()
        repo_dpto = DepartamentoRepository()
        list_ciudades = repo_dpto.get_all_city_by_dpto(dpto) 
        self.cboCiudad.addItem('Seleccione una opción')
        for city in list_ciudades:
            self.cboCiudad.addItem(city.get_nombreciudad())              
            
    def select_dpto(self):
        dpto_seleccionado = self.cboDepartamento.currentText()
        self.poblar_ciudades(dpto_seleccionado)
        print(f"Departamento Seleccionado: {dpto_seleccionado}")
        
    def select_ciudad(self):
        ciudad_seleccionado = self.cboCiudad.currentText()  
        print(f"ciudad seleccionada: {ciudad_seleccionado}")  
        
    def guardar(self):
        dpto = self.cboDepartamento.currentText()
        ciudad = self.cboCiudad.currentText()
        nombre = self.txtSucursal.text()
        direccion = self.txtDireccion.text()
        telefono = self.txtTelefono.text()
        observaciones = self.txtObservaciones.toPlainText()  
        print(f"Datos=> {dpto}, {ciudad}, {nombre}, {direccion}, {telefono}, {observaciones}")  