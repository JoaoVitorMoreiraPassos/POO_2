# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/8_transferencia.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-color: #498f97;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("border: 0px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(361, 471))
        self.frame.setMaximumSize(QtCore.QSize(361, 471))
        self.frame.setStyleSheet("background-color: #156068;\n"
"border-radius: 15px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_confirma = QtWidgets.QPushButton(self.frame)
        self.btn_confirma.setGeometry(QtCore.QRect(50, 400, 261, 35))
        self.btn_confirma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_confirma.setStyleSheet("QPushButton {\n"
"\n"
"    background-color: #498f97;\n"
"    border-radius: 17px;\n"
"    color: #fff\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(86, 159, 168);\n"
"\n"
"}")
        self.btn_confirma.setObjectName("btn_confirma")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #7cbec6;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(55, 250, 81, 19))
        self.label.setStyleSheet("color:#fff;")
        self.label.setObjectName("label")
        self.operacao = QtWidgets.QLabel(self.frame)
        self.operacao.setGeometry(QtCore.QRect(80, 60, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operacao.setFont(font)
        self.operacao.setStyleSheet("color: #fff;")
        self.operacao.setAlignment(QtCore.Qt.AlignCenter)
        self.operacao.setObjectName("operacao")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(55, 120, 151, 19))
        self.label_4.setStyleSheet("color:#fff;")
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 205, 261, 35))
        self.comboBox_2.setStyleSheet("\n"
"QComboBox{\n"
"    background-color: #fff;\n"
"    color: #000;\n"
"    padding-left: 5px;\n"
"    border-radius: 17px;\n"
"    border: 2px solid #498f97;\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"    border: 2px ridge rgb(3, 151, 136);\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(55, 185, 191, 19))
        self.label_5.setStyleSheet("color:#fff;")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(55, 315, 72, 19))
        self.label_3.setStyleSheet("color:#fff;")
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(180, 370, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet("color: #fff;")
        self.checkBox.setObjectName("checkBox")
        self.cpf = QtWidgets.QLineEdit(self.frame)
        self.cpf.setGeometry(QtCore.QRect(50, 140, 261, 35))
        self.cpf.setStyleSheet("QLineEdit{\n"
"    background-color: #fff;\n"
"    color: #111;\n"
"    padding-left: 5px;\n"
"    border-radius: 17px;\n"
"    border: 2px solid #498f97;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px ridge rgb(3, 151, 136)\n"
"}")
        self.cpf.setObjectName("cpf")
        self.valor = QtWidgets.QLineEdit(self.frame)
        self.valor.setGeometry(QtCore.QRect(50, 270, 261, 35))
        self.valor.setStyleSheet("QLineEdit{\n"
"    background-color: #fff;\n"
"    color: #111;\n"
"    padding-left: 5px;\n"
"    border-radius: 17px;\n"
"    border: 2px solid #498f97;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px ridge rgb(3, 151, 136)\n"
"}")
        self.valor.setObjectName("valor")
        self.senha = QtWidgets.QLineEdit(self.frame)
        self.senha.setGeometry(QtCore.QRect(50, 333, 261, 35))
        self.senha.setStyleSheet("QLineEdit{\n"
"    background-color: #fff;\n"
"    color: #111;\n"
"    padding-left: 5px;\n"
"    border-radius: 17px;\n"
"    border: 2px solid #498f97;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px ridge rgb(3, 151, 136)\n"
"}")
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setObjectName("senha")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setStyleSheet("border: 0px")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.voltar = QtWidgets.QPushButton(self.frame_3)
        self.voltar.setGeometry(QtCore.QRect(40, 0, 40, 40))
        self.voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.voltar.setStyleSheet("background-color: rgba(200, 200, 200, 51);\n"
"border-radius: 20px;")
        self.voltar.setText("")
        self.voltar.setObjectName("voltar")
        self.img = QtWidgets.QLabel(self.frame_3)
        self.img.setGeometry(QtCore.QRect(40, 0, 40, 40))
        self.img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img.setStyleSheet("background-color: rgb(243, 243, 243);\n"
"border-radius: 20px;")
        self.img.setText("")
        self.img.setAlignment(QtCore.Qt.AlignCenter)
        self.img.setObjectName("img")
        self.img.raise_()
        self.voltar.raise_()
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transferência"))
        self.btn_confirma.setText(_translate("MainWindow", "Confirmar"))
        self.label_2.setText(_translate("MainWindow", "Beast Bank"))
        self.label.setText(_translate("MainWindow", "Valor (R$):"))
        self.operacao.setText(_translate("MainWindow", "Transferência"))
        self.label_4.setText(_translate("MainWindow", "CPF do destinatário:"))
        self.label_5.setText(_translate("MainWindow", "Conta de destino:"))
        self.label_3.setText(_translate("MainWindow", "Senha:"))
        self.checkBox.setText(_translate("MainWindow", "mostrar senha"))
        self.cpf.setPlaceholderText(_translate("MainWindow", "Apenas números"))
        self.valor.setPlaceholderText(_translate("MainWindow", "150"))
