# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmAddSucursal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_FrmAddSucursal(object):
    def setupUi(self, FrmAddSucursal):
        if not FrmAddSucursal.objectName():
            FrmAddSucursal.setObjectName(u"FrmAddSucursal")
        FrmAddSucursal.resize(400, 500)
        FrmAddSucursal.setMinimumSize(QSize(400, 500))
        FrmAddSucursal.setMaximumSize(QSize(400, 500))
        self.grBox = QGroupBox(FrmAddSucursal)
        self.grBox.setObjectName(u"grBox")
        self.grBox.setGeometry(QRect(10, 10, 380, 431))
        self.lblDpto = QLabel(self.grBox)
        self.lblDpto.setObjectName(u"lblDpto")
        self.lblDpto.setGeometry(QRect(10, 24, 361, 21))
        font = QFont()
        font.setPointSize(12)
        self.lblDpto.setFont(font)
        self.cboDepartamento = QComboBox(self.grBox)
        self.cboDepartamento.setObjectName(u"cboDepartamento")
        self.cboDepartamento.setGeometry(QRect(10, 54, 360, 25))
        self.cboDepartamento.setFont(font)
        self.lblCiudad = QLabel(self.grBox)
        self.lblCiudad.setObjectName(u"lblCiudad")
        self.lblCiudad.setGeometry(QRect(10, 84, 361, 21))
        self.lblCiudad.setFont(font)
        self.cboCiudad = QComboBox(self.grBox)
        self.cboCiudad.setObjectName(u"cboCiudad")
        self.cboCiudad.setGeometry(QRect(10, 114, 360, 25))
        self.cboCiudad.setFont(font)
        self.lblSucursal = QLabel(self.grBox)
        self.lblSucursal.setObjectName(u"lblSucursal")
        self.lblSucursal.setGeometry(QRect(10, 144, 361, 21))
        self.lblSucursal.setFont(font)
        self.txtSucursal = QLineEdit(self.grBox)
        self.txtSucursal.setObjectName(u"txtSucursal")
        self.txtSucursal.setGeometry(QRect(10, 174, 360, 25))
        self.txtSucursal.setFont(font)
        self.txtSucursal.setMaxLength(100)
        self.lblDireccion = QLabel(self.grBox)
        self.lblDireccion.setObjectName(u"lblDireccion")
        self.lblDireccion.setGeometry(QRect(10, 204, 361, 21))
        self.lblDireccion.setFont(font)
        self.txtDireccion = QLineEdit(self.grBox)
        self.txtDireccion.setObjectName(u"txtDireccion")
        self.txtDireccion.setGeometry(QRect(10, 234, 360, 25))
        self.txtDireccion.setFont(font)
        self.txtDireccion.setMaxLength(200)
        self.txtTelefono = QLineEdit(self.grBox)
        self.txtTelefono.setObjectName(u"txtTelefono")
        self.txtTelefono.setGeometry(QRect(10, 294, 360, 25))
        self.txtTelefono.setFont(font)
        self.txtTelefono.setMaxLength(10)
        self.lblTelefono = QLabel(self.grBox)
        self.lblTelefono.setObjectName(u"lblTelefono")
        self.lblTelefono.setGeometry(QRect(10, 264, 361, 21))
        self.lblTelefono.setFont(font)
        self.lblObservaciones = QLabel(self.grBox)
        self.lblObservaciones.setObjectName(u"lblObservaciones")
        self.lblObservaciones.setGeometry(QRect(10, 324, 361, 21))
        self.lblObservaciones.setFont(font)
        self.txtObservaciones = QTextEdit(self.grBox)
        self.txtObservaciones.setObjectName(u"txtObservaciones")
        self.txtObservaciones.setGeometry(QRect(10, 350, 360, 70))
        font1 = QFont()
        font1.setPointSize(11)
        self.txtObservaciones.setFont(font1)
        self.btnGuardar = QPushButton(FrmAddSucursal)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(120, 450, 120, 41))
        self.btnGuardar.setFont(font1)
        self.btnCancelar = QPushButton(FrmAddSucursal)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(270, 450, 120, 41))
        self.btnCancelar.setFont(font1)

        self.retranslateUi(FrmAddSucursal)

        QMetaObject.connectSlotsByName(FrmAddSucursal)
    # setupUi

    def retranslateUi(self, FrmAddSucursal):
        FrmAddSucursal.setWindowTitle(QCoreApplication.translate("FrmAddSucursal", u"Sucursal", None))
        self.grBox.setTitle(QCoreApplication.translate("FrmAddSucursal", u"Informaci\u00f3n de Sucursal", None))
        self.lblDpto.setText(QCoreApplication.translate("FrmAddSucursal", u"Departamento", None))
        self.lblCiudad.setText(QCoreApplication.translate("FrmAddSucursal", u"Ciudad", None))
        self.lblSucursal.setText(QCoreApplication.translate("FrmAddSucursal", u"Nombre Sucursal", None))
        self.lblDireccion.setText(QCoreApplication.translate("FrmAddSucursal", u"Direcci\u00f3n Sucursal", None))
        self.txtTelefono.setInputMask(QCoreApplication.translate("FrmAddSucursal", u"9999999999", None))
        self.lblTelefono.setText(QCoreApplication.translate("FrmAddSucursal", u"Tel\u00e9fono Sucursal", None))
        self.lblObservaciones.setText(QCoreApplication.translate("FrmAddSucursal", u"Observaciones", None))
        self.btnGuardar.setText(QCoreApplication.translate("FrmAddSucursal", u"Guardar", None))
        self.btnCancelar.setText(QCoreApplication.translate("FrmAddSucursal", u"Cancelar", None))
    # retranslateUi

