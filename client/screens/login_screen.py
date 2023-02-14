# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/1_login_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        """
        Este é o painel de login do usuário do banco gerado pelo Qt Designer.

        ...

        Attributes
        ----------
        MainWindow : QMainWindow
                Janela principal do painel de login do usuário do banco.
        
        Methods
        -------
        setupUi(MainWindow)
                Configura a interface gráfica do painel de login do usuário do banco.
        retranslateUi(MainWindow)
                Traduz a interface gráfica do painel de login do usuário do banco.
        """
        def setupUi(self, MainWindow):
                """
                Esse método configura a interface gráfica do painel de login do usuário do banco.

                Parameters
                ----------
                MainWindow : QMainWindow
                        Janela principal do painel de login do usuário do banco.
                
                Returns
                -------
                None
                """
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1366, 768)
                MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
                MainWindow.setStyleSheet("background-color: #498f97;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
                self.gridLayout.setObjectName("gridLayout")
                self.frame_3 = QtWidgets.QFrame(self.centralwidget)
                self.frame_3.setStyleSheet("border: 0px")
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
                self.gridLayout_3.setObjectName("gridLayout_3")
                self.label_5 = QtWidgets.QLabel(self.frame_3)
                self.label_5.setMaximumSize(QtCore.QSize(16777215, 600))
                font = QtGui.QFont()
                font.setFamily("Suruma")
                font.setPointSize(44)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("border: 0px")
                self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
                self.label_5.setObjectName("label_5")
                self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
                self.label_6 = QtWidgets.QLabel(self.frame_3)
                self.label_6.setMaximumSize(QtCore.QSize(16777215, 300))
                font = QtGui.QFont()
                font.setFamily("Fira Code Light")
                font.setPointSize(14)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("color:  #fff;")
                self.label_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
                self.label_6.setObjectName("label_6")
                self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
                self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)
                self.frame_2 = QtWidgets.QFrame(self.centralwidget)
                self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
                self.frame_2.setStyleSheet("border: 0px")
                self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.frame = QtWidgets.QFrame(self.frame_2)
                self.frame.setMinimumSize(QtCore.QSize(361, 411))
                self.frame.setMaximumSize(QtCore.QSize(361, 411))
                self.frame.setStyleSheet("background-color: #156068;\n"
        "border-radius: 15px;\n"
        "")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.Titulo = QtWidgets.QLabel(self.frame)
                self.Titulo.setGeometry(QtCore.QRect(100, 80, 161, 51))
                font = QtGui.QFont()
                font.setPointSize(29)
                font.setBold(False)
                font.setWeight(50)
                self.Titulo.setFont(font)
                self.Titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.Titulo.setStyleSheet("color: #fff;\n"
        "font-size: 26;")
                self.Titulo.setAlignment(QtCore.Qt.AlignCenter)
                self.Titulo.setObjectName("Titulo")
                self.email = QtWidgets.QLineEdit(self.frame)
                self.email.setGeometry(QtCore.QRect(50, 180, 261, 35))
                self.email.setStyleSheet("QLineEdit{\n"
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
                self.email.setObjectName("email")
                self.senha = QtWidgets.QLineEdit(self.frame)
                self.senha.setGeometry(QtCore.QRect(50, 240, 261, 35))
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
                self.pushButton = QtWidgets.QPushButton(self.frame)
                self.pushButton.setGeometry(QtCore.QRect(50, 310, 261, 35))
                self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton.setStyleSheet("background-color: #498f97;\n"
        "border-radius: 17px;\n"
        "color: #fff")
                self.pushButton.setObjectName("pushButton")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(100, 350, 131, 19))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.label.setFont(font)
                self.label.setStyleSheet("color: #fff;")
                self.label.setObjectName("label")
                self.pushButton_2 = QtWidgets.QPushButton(self.frame)
                self.pushButton_2.setGeometry(QtCore.QRect(230, 348, 51, 20))
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setUnderline(True)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.pushButton_2.setStyleSheet("color: #000;")
                self.pushButton_2.setObjectName("pushButton_2")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(110, 30, 141, 31))
                font = QtGui.QFont()
                font.setFamily("Sawasdee")
                font.setPointSize(20)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color: #7cbec6;")
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setObjectName("label_2")
                self.checkBox = QtWidgets.QCheckBox(self.frame)
                self.checkBox.setGeometry(QtCore.QRect(170, 280, 131, 16))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.checkBox.setFont(font)
                self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
                self.checkBox.setAutoFillBackground(False)
                self.checkBox.setStyleSheet("color: #fff;")
                self.checkBox.setObjectName("checkBox")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(55, 160, 72, 19))
                self.label_3.setStyleSheet("color: #fff;")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(55, 220, 72, 19))
                self.label_4.setStyleSheet("color: #fff")
                self.label_4.setObjectName("label_4")
                self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
                self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
                self.frame_4 = QtWidgets.QFrame(self.centralwidget)
                self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
                self.frame_4.setStyleSheet("border: 0px;")
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.voltar = QtWidgets.QPushButton(self.frame_4)
                self.voltar.setGeometry(QtCore.QRect(40, 0, 40, 40))
                self.voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.voltar.setStyleSheet("background-color: rgba(200, 200, 200, 51);\n"
        "border-radius: 20px;\n"
        "")
                self.voltar.setText("")
                self.voltar.setObjectName("voltar")
                self.img = QtWidgets.QLabel(self.frame_4)
                self.img.setGeometry(QtCore.QRect(40, 0, 40, 40))
                self.img.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.img.setStyleSheet("background-color: rgb(243, 243, 243);\n"
        "border-radius: 20px;")
                self.img.setText("")
                self.img.setAlignment(QtCore.Qt.AlignCenter)
                self.img.setObjectName("img")
                self.img.raise_()
                self.voltar.raise_()
                self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                """
                Método para traduzir os textos da interface

                Parameters
                ----------
                MainWindow : QMainWindow
                        Janela principal da interface.
                
                Returns
                -------
                None
                """
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
                self.label_5.setText(_translate("MainWindow", "Beast Bank"))
                self.label_6.setText(_translate("MainWindow", "Gaste como uma fera."))
                self.Titulo.setText(_translate("MainWindow", "Login"))
                self.email.setPlaceholderText(_translate("MainWindow", "ex: joaodasilva@gmail.com"))
                self.senha.setPlaceholderText(_translate("MainWindow", "ex: 12345678"))
                self.pushButton.setText(_translate("MainWindow", "Entrar"))
                self.label.setText(_translate("MainWindow", "Não possui uma conta?"))
                self.pushButton_2.setText(_translate("MainWindow", "Cadastro"))
                self.label_2.setText(_translate("MainWindow", "Beast Bank"))
                self.checkBox.setText(_translate("MainWindow", "mostrar senha"))
                self.label_3.setText(_translate("MainWindow", "E-mail:"))
                self.label_4.setText(_translate("MainWindow", "Senha:"))
