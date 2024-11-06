import os

from PySide6.QtWidgets import QWidget

from views.FrmSucursales_view import Ui_FrmSucursales

class SucursalesWindow(QWidget, Ui_FrmSucursales):
    
    def __init__(self):
        super().__init__()
        
        # Utilizamos el setupUI para definir todos los objetos
        self.setupUi(self)