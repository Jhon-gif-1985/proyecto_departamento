# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmModulos.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_FrmListModulos(object):
    def setupUi(self, FrmListModulos):
        if not FrmListModulos.objectName():
            FrmListModulos.setObjectName(u"FrmListModulos")
        FrmListModulos.resize(857, 417)
        self.grpBtn = QGroupBox(FrmListModulos)
        self.grpBtn.setObjectName(u"grpBtn")
        self.grpBtn.setGeometry(QRect(10, 0, 841, 81))
        self.btnNuevo = QPushButton(self.grpBtn)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setGeometry(QRect(10, 20, 111, 51))
        self.btnNuevo_2 = QPushButton(self.grpBtn)
        self.btnNuevo_2.setObjectName(u"btnNuevo_2")
        self.btnNuevo_2.setGeometry(QRect(130, 20, 111, 51))
        self.btnNuevo_3 = QPushButton(self.grpBtn)
        self.btnNuevo_3.setObjectName(u"btnNuevo_3")
        self.btnNuevo_3.setGeometry(QRect(250, 20, 111, 51))
        self.tblModulos = QTableWidget(FrmListModulos)
        self.tblModulos.setObjectName(u"tblModulos")
        self.tblModulos.setGeometry(QRect(20, 110, 820, 250))
        self.lblTotal = QLabel(FrmListModulos)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setGeometry(QRect(20, 383, 121, 21))
        font = QFont()
        font.setPointSize(12)
        self.lblTotal.setFont(font)
        self.lblNumeroTotal = QLabel(FrmListModulos)
        self.lblNumeroTotal.setObjectName(u"lblNumeroTotal")
        self.lblNumeroTotal.setGeometry(QRect(140, 383, 121, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblNumeroTotal.setFont(font1)

        self.retranslateUi(FrmListModulos)

        QMetaObject.connectSlotsByName(FrmListModulos)
    # setupUi

    def retranslateUi(self, FrmListModulos):
        FrmListModulos.setWindowTitle(QCoreApplication.translate("FrmListModulos", u"Form", None))
        self.grpBtn.setTitle(QCoreApplication.translate("FrmListModulos", u"Acciones", None))
        self.btnNuevo.setText(QCoreApplication.translate("FrmListModulos", u"Nuevo M\u00f3dulo", None))
        self.btnNuevo_2.setText(QCoreApplication.translate("FrmListModulos", u"Editar M\u00f3dulo", None))
        self.btnNuevo_3.setText(QCoreApplication.translate("FrmListModulos", u"Eliminar M\u00f3dulo", None))
        self.lblTotal.setText(QCoreApplication.translate("FrmListModulos", u"Total Registros:", None))
        self.lblNumeroTotal.setText("")
    # retranslateUi

