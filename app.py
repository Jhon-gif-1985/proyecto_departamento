import sys
from PySide6.QtWidgets import  QApplication
from controllers.addmodulowindow import AddModuloWindow
from controllers.listmoduloswindow import ListModulosWindows
from controllers.addsucursalwindow import AddSucursalWindow
from controllers.addsucursal import FrmAddSucursal

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrmAddSucursal()
    window.show()
    
    sys.exit(app.exec())