# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmAddModulo.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_FrmAddModulo(object):
    def setupUi(self, FrmAddModulo):
        if not FrmAddModulo.objectName():
            FrmAddModulo.setObjectName(u"FrmAddModulo")
        FrmAddModulo.setWindowModality(Qt.WindowModality.WindowModal)
        FrmAddModulo.resize(740, 276)
        FrmAddModulo.setMinimumSize(QSize(740, 270))
        FrmAddModulo.setMaximumSize(QSize(750, 300))
        self.grbNuevo = QGroupBox(FrmAddModulo)
        self.grbNuevo.setObjectName(u"grbNuevo")
        self.grbNuevo.setGeometry(QRect(10, 10, 711, 251))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.grbNuevo.setFont(font)
        self.grbNuevo.setAutoFillBackground(False)
        self.label = QLabel(self.grbNuevo)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 121, 21))
        self.cboDepartamento = QComboBox(self.grbNuevo)
        self.cboDepartamento.setObjectName(u"cboDepartamento")
        self.cboDepartamento.setGeometry(QRect(10, 56, 220, 22))
        self.cboMunicipio = QComboBox(self.grbNuevo)
        self.cboMunicipio.setObjectName(u"cboMunicipio")
        self.cboMunicipio.setGeometry(QRect(240, 56, 220, 22))
        self.label_2 = QLabel(self.grbNuevo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 30, 121, 21))
        self.label_3 = QLabel(self.grbNuevo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 30, 121, 21))
        self.cboSucursal = QComboBox(self.grbNuevo)
        self.cboSucursal.setObjectName(u"cboSucursal")
        self.cboSucursal.setGeometry(QRect(470, 56, 220, 22))
        self.label_4 = QLabel(self.grbNuevo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 110, 121, 21))
        self.txtNombre = QLineEdit(self.grbNuevo)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(10, 133, 220, 22))
        self.txtCodigo = QLineEdit(self.grbNuevo)
        self.txtCodigo.setObjectName(u"txtCodigo")
        self.txtCodigo.setGeometry(QRect(240, 133, 220, 22))
        self.label_5 = QLabel(self.grbNuevo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 110, 121, 21))
        self.btnGuardar = QPushButton(self.grbNuevo)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(360, 190, 150, 41))
        self.btnGuardar.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(0, 140, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.btnCancelar = QPushButton(self.grbNuevo)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(534, 190, 150, 41))
        self.btnCancelar.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(170, 0, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(FrmAddModulo)

        QMetaObject.connectSlotsByName(FrmAddModulo)
    # setupUi

    def retranslateUi(self, FrmAddModulo):
        FrmAddModulo.setWindowTitle(QCoreApplication.translate("FrmAddModulo", u"Form", None))
        self.grbNuevo.setTitle(QCoreApplication.translate("FrmAddModulo", u"Nuevo Elemento", None))
        self.label.setText(QCoreApplication.translate("FrmAddModulo", u"Departamento", None))
        self.label_2.setText(QCoreApplication.translate("FrmAddModulo", u"Municipio", None))
        self.label_3.setText(QCoreApplication.translate("FrmAddModulo", u"Sucursal", None))
        self.label_4.setText(QCoreApplication.translate("FrmAddModulo", u"Nombre", None))
        self.label_5.setText(QCoreApplication.translate("FrmAddModulo", u"C\u00f3digo", None))
        self.btnGuardar.setText(QCoreApplication.translate("FrmAddModulo", u"Guardar", None))
        self.btnCancelar.setText(QCoreApplication.translate("FrmAddModulo", u"Cancelar", None))
    # retranslateUi

