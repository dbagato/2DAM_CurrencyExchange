# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ventanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 631)
        MainWindow.setStyleSheet("QMainWindow{background-color: #AA14F0;\n"
"}\n"
"QWidget{border-color:black}\n"
"#tab{\n"
"    background-color: rgb(188, 140, 242);\n"
"}\n"
"#tab_2{\n"
"    background-color: rgb(188, 140, 242);\n"
"}\n"
"#tab_3{\n"
"    background-color: rgb(188, 140, 242);\n"
"}\n"
"#tab_4{\n"
"    background-color: rgb(188, 140, 242);\n"
"}\n"
"#costeFechFecha{font-size:24px\n"
"}\n"
"QComboBox{\n"
"font-size:24px\n"
"}\n"
"#cambioDinero{font-size:24px;\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"#conversorDinero{font-size:24px;\n"
"background-color: rgb(238, 238, 238);\n"
"}\n"
"QListWidget{background-color: rgb(238, 238, 238);\n"
"}\n"
"QPushButton{\n"
"  background-color: #AA14F0;\n"
"  border-radius: 24px;\n"
"  border-style: none;\n"
"  height: 48px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.conversor = QtWidgets.QGroupBox(self.tab)
        self.conversor.setTitle("")
        self.conversor.setObjectName("conversor")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.conversor)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter = QtWidgets.QSplitter(self.conversor)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.conversorTitle = QtWidgets.QLabel(self.layoutWidget)
        self.conversorTitle.setObjectName("conversorTitle")
        self.verticalLayout_3.addWidget(self.conversorTitle)
        self.conversorMonedas = QtWidgets.QComboBox(self.layoutWidget)
        self.conversorMonedas.setEnabled(True)
        self.conversorMonedas.setMinimumSize(QtCore.QSize(0, 30))
        self.conversorMonedas.setObjectName("conversorMonedas")
        self.verticalLayout_3.addWidget(self.conversorMonedas)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.conversorImporte = QtWidgets.QLabel(self.layoutWidget)
        self.conversorImporte.setObjectName("conversorImporte")
        self.horizontalLayout_2.addWidget(self.conversorImporte)
        spacerItem1 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.conversorDesc = QtWidgets.QLabel(self.layoutWidget)
        self.conversorDesc.setObjectName("conversorDesc")
        self.horizontalLayout_2.addWidget(self.conversorDesc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.conversorDinero = QtWidgets.QLineEdit(self.layoutWidget)
        self.conversorDinero.setMinimumSize(QtCore.QSize(0, 30))
        self.conversorDinero.setObjectName("conversorDinero")
        self.verticalLayout_3.addWidget(self.conversorDinero)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout_8.addWidget(self.splitter, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.conversor)
        self.cambio = QtWidgets.QGroupBox(self.tab)
        self.cambio.setTitle("")
        self.cambio.setObjectName("cambio")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.cambio)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.splitter_2 = QtWidgets.QSplitter(self.cambio)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cambioTitle = QtWidgets.QLabel(self.layoutWidget_3)
        self.cambioTitle.setObjectName("cambioTitle")
        self.verticalLayout_8.addWidget(self.cambioTitle)
        self.cambioMonedas = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cambioMonedas.setEnabled(True)
        self.cambioMonedas.setMinimumSize(QtCore.QSize(0, 30))
        self.cambioMonedas.setSizeIncrement(QtCore.QSize(0, 0))
        self.cambioMonedas.setObjectName("cambioMonedas")
        self.verticalLayout_8.addWidget(self.cambioMonedas)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cambioImporte = QtWidgets.QLabel(self.layoutWidget_3)
        self.cambioImporte.setObjectName("cambioImporte")
        self.horizontalLayout_3.addWidget(self.cambioImporte)
        spacerItem4 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.cambioDesc = QtWidgets.QLabel(self.layoutWidget_3)
        self.cambioDesc.setObjectName("cambioDesc")
        self.horizontalLayout_3.addWidget(self.cambioDesc)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.cambioDinero = QtWidgets.QLabel(self.layoutWidget_3)
        self.cambioDinero.setMinimumSize(QtCore.QSize(0, 30))
        self.cambioDinero.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cambioDinero.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 0, 0);")
        self.cambioDinero.setObjectName("cambioDinero")
        self.verticalLayout_8.addWidget(self.cambioDinero)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.gridLayout_9.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.cambio)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.detalles_3 = QtWidgets.QGroupBox(self.tab)
        self.detalles_3.setTitle("")
        self.detalles_3.setObjectName("detalles_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.detalles_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.convertirPrincipal = QtWidgets.QPushButton(self.detalles_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.convertirPrincipal.setFont(font)
        self.convertirPrincipal.setObjectName("convertirPrincipal")
        self.gridLayout_10.addWidget(self.convertirPrincipal, 0, 0, 1, 1)
        self.verticalLayout_16.addWidget(self.detalles_3)
        self.gridLayout.addLayout(self.verticalLayout_16, 1, 1, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.costeTitle = QtWidgets.QLabel(self.tab_2)
        self.costeTitle.setObjectName("costeTitle")
        self.verticalLayout_2.addWidget(self.costeTitle)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 25, -1, 15)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.costeDesc = QtWidgets.QLabel(self.tab_2)
        self.costeDesc.setObjectName("costeDesc")
        self.horizontalLayout_15.addWidget(self.costeDesc)
        self.costeBase = QtWidgets.QComboBox(self.tab_2)
        self.costeBase.setObjectName("costeBase")
        self.horizontalLayout_15.addWidget(self.costeBase)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.costeList = QtWidgets.QListWidget(self.tab_2)
        self.costeList.setObjectName("costeList")
        self.verticalLayout_2.addWidget(self.costeList)
        self.costeButtons = QtWidgets.QGroupBox(self.tab_2)
        self.costeButtons.setMinimumSize(QtCore.QSize(0, 100))
        self.costeButtons.setTitle("")
        self.costeButtons.setObjectName("costeButtons")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.costeButtons)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem6 = QtWidgets.QSpacerItem(590, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.costeMostrar = QtWidgets.QPushButton(self.costeButtons)
        self.costeMostrar.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.costeMostrar.setFont(font)
        self.costeMostrar.setObjectName("costeMostrar")
        self.horizontalLayout_11.addWidget(self.costeMostrar)
        self.verticalLayout_2.addWidget(self.costeButtons)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.splitter_3 = QtWidgets.QSplitter(self.tab_3)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget_7 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_7)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.costeFechFecha = QtWidgets.QDateEdit(self.layoutWidget_7)
        self.costeFechFecha.setMinimumSize(QtCore.QSize(0, 30))
        self.costeFechFecha.setMinimumDate(QtCore.QDate(1997, 1, 1))
        self.costeFechFecha.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.costeFechFecha.setObjectName("costeFechFecha")
        self.gridLayout_3.addWidget(self.costeFechFecha, 1, 1, 1, 1)
        self.costeFechMoneda = QtWidgets.QComboBox(self.layoutWidget_7)
        self.costeFechMoneda.setObjectName("costeFechMoneda")
        self.gridLayout_3.addWidget(self.costeFechMoneda, 0, 1, 1, 1)
        self.costeFechTitle = QtWidgets.QLabel(self.layoutWidget_7)
        self.costeFechTitle.setObjectName("costeFechTitle")
        self.gridLayout_3.addWidget(self.costeFechTitle, 0, 0, 1, 1)
        self.costeFech = QtWidgets.QLabel(self.layoutWidget_7)
        self.costeFech.setObjectName("costeFech")
        self.gridLayout_3.addWidget(self.costeFech, 1, 0, 1, 1)
        self.costeFechMostrar = QtWidgets.QPushButton(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.costeFechMostrar.setFont(font)
        self.costeFechMostrar.setObjectName("costeFechMostrar")
        self.gridLayout_3.addWidget(self.costeFechMostrar, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.costeFechLista = QtWidgets.QListWidget(self.tab_3)
        self.costeFechLista.setObjectName("costeFechLista")
        self.gridLayout_6.addWidget(self.costeFechLista, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("")
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.acercaDesc = QtWidgets.QLabel(self.tab_4)
        self.acercaDesc.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.acercaDesc.setObjectName("acercaDesc")
        self.verticalLayout.addWidget(self.acercaDesc)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.acercaLink1 = QtWidgets.QLabel(self.tab_4)
        self.acercaLink1.setObjectName("acercaLink1")
        self.horizontalLayout_12.addWidget(self.acercaLink1)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.acercaLink2 = QtWidgets.QLabel(self.tab_4)
        self.acercaLink2.setObjectName("acercaLink2")
        self.horizontalLayout_13.addWidget(self.acercaLink2)
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_13.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.acercaLink3 = QtWidgets.QLabel(self.tab_4)
        self.acercaLink3.setObjectName("acercaLink3")
        self.horizontalLayout_14.addWidget(self.acercaLink3)
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setObjectName("label")
        self.horizontalLayout_14.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.gridLayout_7.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem10, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 876, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.conversorTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Tengo esta divisa:</span></p></body></html>"))
        self.conversorImporte.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Importe:</span></p></body></html>"))
        self.conversorDesc.setText(_translate("MainWindow", "<html><head/><body><p>Tengo esta cantidad para cambiar</p></body></html>"))
        self.conversorDinero.setText(_translate("MainWindow", "0.00"))
        self.cambioTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Al cambio de divisa:</span></p></body></html>"))
        self.cambioImporte.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Importe:</span></p></body></html>"))
        self.cambioDesc.setText(_translate("MainWindow", "<html><head/><body><p>Cantidad al cambio</p></body></html>"))
        self.cambioDinero.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">0.00</p></body></html>"))
        self.convertirPrincipal.setText(_translate("MainWindow", "Convertir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Conversor de Divisas"))
        self.costeTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Coste de divisas actuales</span></p></body></html>"))
        self.costeDesc.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Seleccione la moneda base:</span></p></body></html>"))
        self.costeMostrar.setText(_translate("MainWindow", "Mostrar divisas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Coste divisas en este momento"))
        self.costeFechFecha.setDisplayFormat(_translate("MainWindow", "yyyy/MM/dd"))
        self.costeFechTitle.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Seleccione una moneda</span></p></body></html>"))
        self.costeFech.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Seleccione la fecha a consultar</span></p></body></html>"))
        self.costeFechMostrar.setText(_translate("MainWindow", "Consultar Valor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Coste de divisas en una fecha"))
        self.acercaDesc.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Aplicacion creada para Proyecto 2ºDAM Diseño de Interfaces Primer Trimestre</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Curso 2021/2022</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Licencias:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    -Aplicacion sujeta a licencia GNU3 de codigo abierto </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">    -Creado por aplicacion Qt Designer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Links:</span></p></body></html>"))
        self.acercaLink1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">-Link al codigo de proyecto:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/dbagato/2DAM_CurrencyExchange\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">https://github.com/dbagato/2DAM_CurrencyExchange</span></a></p></body></html>"))
        self.acercaLink2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">-Link a pagina Qt Designer:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.qt.io/\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">https://www.qt.io/</span></a></p></body></html>"))
        self.acercaLink3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\"> -Link a licencia GNU3:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.gnu.org/licenses/licenses.es.html\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">https://www.gnu.org/licenses/licenses.es.html</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Acerca de..."))
