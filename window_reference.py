# -*- coding: utf-8 -*-

################################################################################
#  Form generated from reading UI file 'window_referenceedoGxf.ui'
##
#  Created by: Qt User Interface Compiler version 5.15.2
##
#  WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 440)
        MainWindow.setStyleSheet(u"background-color: rgb(248, 248, 248)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.roadmap_view_image = QLabel(self.centralwidget)
        self.roadmap_view_image.setObjectName(u"roadmap_view_image")
        self.roadmap_view_image.setGeometry(QRect(0, 0, 400, 100))
        self.roadmap_view_image.setStyleSheet(u"QLabel { border-color: rgb(0, 0, 0); \n"
                                              "               border-width: 1px;\n"
                                              "               border-style:solid }")
        self.roadmap_view_image.setPixmap(QPixmap(u"images/roadmap_view.png"))
        self.search = QPushButton(self.centralwidget)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(150, 385, 100, 40))
        font = QFont()
        font.setFamily(u"Bahnschrift Light SemiCondensed")
        font.setPointSize(16)
        self.search.setFont(font)
        self.search.setStyleSheet(u"QPushButton { background-color: rgba(65, 255, 51, 210);\n"
                                  "                         border-color: rgb(0, 0, 0);\n"
                                  "                         border-width: 1px;\n"
                                  "                         border-style:solid;\n"
                                  "                         border-radius: 4; }\n"
                                  "QPushButton:hover { background-color: rgb(170, 255, 127) }")
        self.frame_informations = QFrame(self.centralwidget)
        self.frame_informations.setObjectName(u"frame_informations")
        self.frame_informations.setGeometry(QRect(5, 130, 390, 245))
        self.frame_informations.setStyleSheet(u"QFrame { background-color: rgb(255, 255, 255);\n"
                                              "                 border-color: rgb(0, 0, 0);\n"
                                              "                 border-width: 1px;\n"
                                              "                 border-style:solid;\n"
                                              "                 border-radius: 4; }\n"
                                              "")
        self.frame_informations.setFrameShape(QFrame.StyledPanel)
        self.frame_informations.setFrameShadow(QFrame.Raised)
        self.street = QLabel(self.frame_informations)
        self.street.setObjectName(u"street")
        self.street.setGeometry(QRect(5, 5, 380, 55))
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans Condensed")
        font1.setPointSize(14)
        self.street.setFont(font1)
        self.street.setStyleSheet(u"QLabel { background-color: rgb(255, 255, 255);\n"
                                  "               border-color: rgb(0, 0, 0);\n"
                                  "               border-width: 0px;\n"
                                  "               border-style:solid;\n"
                                  "               border-radius: 0; }")
        self.street.setMargin(5)
        self.district = QLabel(self.frame_informations)
        self.district.setObjectName(u"district")
        self.district.setGeometry(QRect(5, 125, 380, 55))
        self.district.setFont(font1)
        self.district.setStyleSheet(u"QLabel { background-color: rgb(255, 255, 255);\n"
                                    "               border-color: rgb(0, 0, 0);\n"
                                    "               border-width: 0px;\n"
                                    "               border-style:solid;\n"
                                    "               border-radius: 0; }")
        self.district.setMargin(5)
        self.city = QLabel(self.frame_informations)
        self.city.setObjectName(u"city")
        self.city.setGeometry(QRect(5, 65, 380, 55))
        self.city.setFont(font1)
        self.city.setStyleSheet(u"QLabel { background-color: rgb(255, 255, 255);\n"
                                "               border-color: rgb(0, 0, 0);\n"
                                "               border-width: 0px;\n"
                                "               border-style:solid;\n"
                                "               border-radius: 0; }")
        self.city.setMargin(5)
        self.state = QLabel(self.frame_informations)
        self.state.setObjectName(u"state")
        self.state.setGeometry(QRect(5, 185, 380, 55))
        self.state.setFont(font1)
        self.state.setStyleSheet(u"QLabel { background-color: rgb(255, 255, 255);\n"
                                 "               border-color: rgb(0, 0, 0);\n"
                                 "               border-width: 0px;\n"
                                 "               border-style:solid;\n"
                                 "               border-radius: 0; }")
        self.state.setMargin(5)
        self.cep_number = QLineEdit(self.centralwidget)
        self.cep_number.setObjectName(u"cep_number")
        self.cep_number.setGeometry(QRect(100, 80, 200, 40))
        font2 = QFont()
        font2.setFamily(u"Arial Rounded MT Bold")
        font2.setPointSize(16)
        self.cep_number.setFont(font2)
        self.cep_number.setStyleSheet(u"QLineEdit { background-color: rgb(255, 255, 255);\n"
                                      "               color: rgb(29, 29, 29);\n"
                                      "               border-color: rgb(0, 0, 0);\n"
                                      "               border-width: 1px;\n"
                                      "               border-style: solid;\n"
                                      "               border-radius: 4; }")
        self.cep_number.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.roadmap_view_image.setText("")
        self.search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.street.setText(QCoreApplication.translate("MainWindow", u"Rua: ", None))
        self.district.setText(QCoreApplication.translate("MainWindow", u"Bairro: ", None))
        self.city.setText(QCoreApplication.translate("MainWindow", u"Cidade: ", None))
        self.state.setText(QCoreApplication.translate("MainWindow", u"Estado", None))
    # retranslateUi
