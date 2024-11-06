import os

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView

from views.FrmModulos_view import Ui_FrmListModulos

class ListModulosWindows(QWidget, Ui_FrmListModulos):
    
    def __init__(self):
        super().__init__()
        
        # Utilizamos el setupUI para definir todos los objetos
        self.setupUi(self)
        self.config_table()
        self.poblate_table()
        
        
        
    def config_table(self):
        columns_headers=("ID", "Departamento", "Municipio", "Sucursal", "Nombre", "Código")  
        self.tblModulos.setColumnCount(len(columns_headers)) 
        self.tblModulos.setHorizontalHeaderLabels(columns_headers)
        self.tblModulos.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    def poblate_table(self, data=None):
        if data is None:
            data = []
            
        self.tblModulos.setRowCount(len(data))     
        for(index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.tblModulos.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))    
    
    def ver_total(self):
        total_rows = str(self.tblModulos.rowCount())
        self.lblNumeroTotal.setText(total_rows)