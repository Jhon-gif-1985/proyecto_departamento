import os

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView

from models.repository.departamentorepository import DepartamentoRepository
from views.FrmAddModulo_view import Ui_FrmAddModulo

class AddModuloWindow(QWidget, Ui_FrmAddModulo):
    def __init__(self):
        super().__init__()
        
        # Utilizamos el setupUI para definir todos los objetos
        self.setupUi(self)
        self.poblar_departamento()
        
        self.cboDepartamento.currentIndexChanged.connect(self.select_dpto)
        
        
            
            
    def poblar_departamento(self):
        repo_departamento = DepartamentoRepository()
        list_dptos = repo_departamento.get_all()
        ## poblar un combobox
        self.cboDepartamento.addItem('Seleccione una opción') 
        for dpto in list_dptos:
            self.cboDepartamento.addItem(dpto.get_nombre())  
            
    def poblar_ciudades(self, dpto:str):
        self.cboMunicipio.clear()
        repo_dpto = DepartamentoRepository()
        list_ciudades = repo_dpto.get_all_city_by_dpto(dpto) 
        self.cboMunicipio.addItem('Seleccione una opción')
        for city in list_ciudades:
            self.cboMunicipio.addItem(city.get_nombreciudad())              
            
    def select_dpto(self):
        dpto_seleccionado = self.cboDepartamento.currentText()
        self.poblar_ciudades(dpto_seleccionado)
        print(dpto_seleccionado)
                