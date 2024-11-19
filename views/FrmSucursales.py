# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmSucursales.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_FrmSucursales(object):
    def setupUi(self, FrmSucursales):
        if not FrmSucursales.objectName():
            FrmSucursales.setObjectName(u"FrmSucursales")
        FrmSucursales.resize(762, 340)
        self.fmFrame = QFrame(FrmSucursales)
        self.fmFrame.setObjectName(u"fmFrame")
        self.fmFrame.setGeometry(QRect(10, 10, 740, 80))
        self.fmFrame.setFrameShape(QFrame.StyledPanel)
        self.fmFrame.setFrameShadow(QFrame.Raised)
        self.btnNuevo = QPushButton(self.fmFrame)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setGeometry(QRect(10, 20, 120, 40))
        self.btnEditar = QPushButton(self.fmFrame)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setGeometry(QRect(140, 20, 120, 40))
        self.btnEliminar = QPushButton(self.fmFrame)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(270, 20, 120, 40))
        self.frame = QFrame(FrmSucursales)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 100, 740, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tblSucursales = QTableWidget(self.frame)
        self.tblSucursales.setObjectName(u"tblSucursales")
        self.tblSucursales.setGeometry(QRect(20, 10, 710, 180))
        self.lblTotal = QLabel(FrmSucursales)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setGeometry(QRect(10, 310, 111, 21))
        font = QFont()
        font.setPointSize(12)
        self.lblTotal.setFont(font)
        self.lblNumeroTotal = QLabel(FrmSucursales)
        self.lblNumeroTotal.setObjectName(u"lblNumeroTotal")
        self.lblNumeroTotal.setGeometry(QRect(120, 310, 111, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblNumeroTotal.setFont(font1)

        self.retranslateUi(FrmSucursales)

        QMetaObject.connectSlotsByName(FrmSucursales)
    # setupUi

    def retranslateUi(self, FrmSucursales):
        FrmSucursales.setWindowTitle(QCoreApplication.translate("FrmSucursales", u"Gestion de Sucursales", None))
        self.btnNuevo.setText(QCoreApplication.translate("FrmSucursales", u"Nueva Sucursal", None))
        self.btnEditar.setText(QCoreApplication.translate("FrmSucursales", u"Editar Sucursal", None))
        self.btnEliminar.setText(QCoreApplication.translate("FrmSucursales", u"Eliminar Sucursal", None))
        self.lblTotal.setText(QCoreApplication.translate("FrmSucursales", u"Total Registros:", None))
        self.lblNumeroTotal.setText("")
    # retranslateUi

