import os

from PySide6.QtWidgets import QWidget, QMessageBox

from models.entity.sucursal import Sucursal
from models.repository.departamentorepository import DepartamentoRepository
from models.repository.sucursalesrepository import SucursalRepository
from views.FrmAddSucursal_view import Ui_FrmAddSucursal

class FrmAddSucursal(QWidget, Ui_FrmAddSucursal):
    
    def __init__(self, edit_mode = False, sucursaledit: Sucursal=None):
        super().__init__()
        
        self.setupUi(self)
        self.__sucursal = sucursaledit
        self.btnCancelar.clicked.connect(self.close)
        self.btnGuardar.clicked.connect(self.guardar)
        self.cboDepartamento.currentIndexChanged.connect(self.select_dpto)
        self.inicializa_repositorios()
        self.extraer_departamentos()
        
        if edit_mode :
            self.load_data()
        
    def inicializa_repositorios(self):
        self.repositorio_departamento = DepartamentoRepository()    
        self.repositorio_sucursal = SucursalRepository()
        
    def extraer_departamentos(self):        
        listadodpto = self.repositorio_departamento.get_all()        
        self.cboDepartamento.addItem('Seleccione una opción') 
        for dpto in listadodpto:
            self.cboDepartamento.addItem(dpto.get_nombre()) 
  
        
    def select_dpto(self):
        dpto_seleccion = self.cboDepartamento.currentText()
        self.cboCiudad.clear()        
        self.listado_ciudades=self.repositorio_departamento.get_all_city_by_dpto(dpto_seleccion) 
        self.cboCiudad.addItem('Seleccione una opción')  
        for ciudad in self.listado_ciudades:
            self.cboCiudad.addItem(ciudad.get_nombreciudad())
    
    def select_ciudad(self):
        ciudad_seleccionado = self.cboCiudad.currentText()  
        print(f"ciudad seleccionada: {ciudad_seleccionado}")         
        
    def guardar(self):
        try:
            msg_error = ""
            dpto = self.cboDepartamento.currentText()
            ciudad = self.cboCiudad.currentText()
            nombre = self.txtSucursal.text()
            direccion = self.txtDireccion.text()
            telefono = self.txtTelefono.text()
            observaciones = self.txtObservaciones.toPlainText()

            if dpto == "" or dpto =="Seleccione una opción":
                msg_error = msg_error + "Debe completar el campo Departamento,"

            if ciudad =="" or ciudad == "Seleccione una opción":
                msg_error = msg_error + "Debe completar el campo Ciudad,"
                
            if(nombre==""):
                msg_error = msg_error + "Debe completar el campo Nombre Sucursal,"
            
            if(direccion==""):
                msg_error = msg_error + "Debe completar el campo Dirección,"  
                       
            if msg_error=="":
                departamento=self.repositorio_departamento.get_by_nombre(dpto)
                ciudadresul = self.repositorio_departamento.get_city_by_dpto_bynombre_ciudad(dpto, ciudad)
                sucursal = Sucursal(id=0, id_dpto=departamento.get_id(), id_ciudad=ciudadresul.get_idciudad(), sucursal=nombre, direccion=direccion, telefono=telefono, observaciones=observaciones, estado=1)
                self.repositorio_sucursal.save(sucursal)
                print(sucursal)
                self.mostrar_mensaje(titulo="Guardar", texto="Guardar", textoinformativo="Se guardó la información de manera satisfactoria", tipo=QMessageBox.Information)            
                self.limpiar_campos()
                
            else:
                self.mostrar_mensaje(titulo="Error", texto="Complete los campos", textoinformativo=msg_error, tipo=QMessageBox.Warning)
        except Exception as er:
            print(er)
            self.mostrar_mensaje(titulo="Error", texto="Error Desconocido", textoinformativo="", tipo=QMessageBox.Critical)


    def limpiar_campos(self):
        self.cboDepartamento.setCurrentIndex(0)
        self.cboCiudad.clear()
        self.txtSucursal.setText("")
        self.txtDireccion.setText("")
        self.txtTelefono.setText("")
        self.txtObservaciones.setPlainText("")
            

    def mostrar_mensaje(self, titulo: str, texto:str, textoinformativo:str, tipo: QMessageBox.Icon):
        message = QMessageBox()
        message.setWindowTitle(titulo)
        message.setText(texto) 
        message.setInformativeText(textoinformativo)           
        message.setIcon(tipo)
        message.exec()
        
    
    def load_data(self):
        self.cboDepartamento.setCurrentText(self.repositorio_departamento.get_by_id(self.__sucursal.get_dpto()).get_nombre())
        self.txtSucursal.setText(self.__sucursal.get_sucursal())
        self.txtDireccion.setText(self.__sucursal.get_direccion())
        self.txtTelefono.setText(self.__sucursal.get_telefono())    