# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/6_extrato.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 650)
        MainWindow.setStyleSheet("background-color: #498f97;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 55))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Suruma")
        font.setPointSize(41)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(700, 400))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 450))
        self.frame.setStyleSheet("border: 0px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setMinimumSize(QtCore.QSize(900, 300))
        self.scrollArea.setMaximumSize(QtCore.QSize(1200, 425))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1186, 416))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 450))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scrollAreaWidgetContents.setFont(font)
        self.scrollAreaWidgetContents.setStyleSheet("QWidget{\n"
"    background: #156060;\n"
"    padding: -10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel{\n"
"    background: #65ac92;\n"
"    padding: 7px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_2.setStyleSheet("padding: 0px")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(700, 60))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 1)
        self.criacao = QtWidgets.QLabel(self.widget_2)
        self.criacao.setMinimumSize(QtCore.QSize(0, 30))
        self.criacao.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.criacao.setFont(font)
        self.criacao.setStyleSheet("color: #fff;")
        self.criacao.setText("")
        self.criacao.setAlignment(QtCore.Qt.AlignCenter)
        self.criacao.setObjectName("criacao")
        self.gridLayout_6.addWidget(self.criacao, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setMaximumSize(QtCore.QSize(750, 800))
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_4.addWidget(self.widget_5, 0, 2, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMinimumSize(QtCore.QSize(120, 50))
        self.widget_4.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_4.setObjectName("widget_4")
        self.voltar = QtWidgets.QPushButton(self.widget_4)
        self.voltar.setGeometry(QtCore.QRect(40, 0, 40, 40))
        self.voltar.setMinimumSize(QtCore.QSize(40, 40))
        self.voltar.setMaximumSize(QtCore.QSize(40, 40))
        self.voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar.setStyleSheet("background-color: rgba(200, 200, 200, 51);\n"
"border-radius: 20px;\n"
"")
        self.voltar.setText("")
        self.voltar.setObjectName("voltar")
        self.img = QtWidgets.QLabel(self.widget_4)
        self.img.setGeometry(QtCore.QRect(40, 0, 40, 40))
        self.img.setMinimumSize(QtCore.QSize(40, 40))
        self.img.setMaximumSize(QtCore.QSize(40, 40))
        self.img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border-radius: 20px;")
        self.img.setText("")
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.img.raise_()
        self.voltar.raise_()
        self.gridLayout_4.addWidget(self.widget_4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Historico de Transações"))
        self.label_2.setText(_translate("MainWindow", "Beast Bank"))
        self.label.setText(_translate("MainWindow", "Extrato"))
