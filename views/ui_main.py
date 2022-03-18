# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mix_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 487)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget #centralwidget{\n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"QFrame{\n"
"	border: 1px solid gray;\n"
"	border-radius: 8px;\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 15px;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QDial{\n"
"	background-color: rgb(175, 0, 0);\n"
"}\n"
"QFrame{\n"
"	border: 1px solid gray;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(175, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 1px solid blue;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(5)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 15)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 10, -1, 15)
        self.lb_a = QLabel(self.frame)
        self.lb_a.setObjectName(u"lb_a")
        self.lb_a.setMinimumSize(QSize(0, 35))
        self.lb_a.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.lb_a.setFont(font)

        self.verticalLayout_7.addWidget(self.lb_a, 0, Qt.AlignHCenter)

        self.dial_a = QDial(self.frame)
        self.dial_a.setObjectName(u"dial_a")
        self.dial_a.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_a.setSingleStep(10)
        self.dial_a.setNotchesVisible(True)

        self.verticalLayout_7.addWidget(self.dial_a)

        self.lcd = QLCDNumber(self.frame)
        self.lcd.setObjectName(u"lcd")
        self.lcd.setMaximumSize(QSize(16777215, 30))
        self.lcd.setLineWidth(1)
        self.lcd.setMidLineWidth(0)
        self.lcd.setSmallDecimalPoint(False)
        self.lcd.setDigitCount(5)
        self.lcd.setSegmentStyle(QLCDNumber.Outline)
        self.lcd.setProperty("intValue", 0)

        self.verticalLayout_7.addWidget(self.lcd, 0, Qt.AlignHCenter)

        self.dlz_01 = QSlider(self.frame)
        self.dlz_01.setObjectName(u"dlz_01")
        self.dlz_01.setMaximumSize(QSize(16777215, 185))
        self.dlz_01.setCursor(QCursor(Qt.PointingHandCursor))
        self.dlz_01.setStyleSheet(u"QSlider{\n"
"background-color: rgb(57, 57, 57);\n"
"}\n"
"\n"
"QSlider::TicksAbove{\n"
"	1;\n"
"}\n"
"")
        self.dlz_01.setMinimum(0)
        self.dlz_01.setMaximum(49)
        self.dlz_01.setTracking(False)
        self.dlz_01.setOrientation(Qt.Vertical)
        self.dlz_01.setTickPosition(QSlider.TicksBothSides)
        self.dlz_01.setTickInterval(2)

        self.verticalLayout_7.addWidget(self.dlz_01, 0, Qt.AlignHCenter)

        self.btnPlay_a = QPushButton(self.frame)
        self.btnPlay_a.setObjectName(u"btnPlay_a")
        self.btnPlay_a.setMinimumSize(QSize(85, 30))
        self.btnPlay_a.setMaximumSize(QSize(16777215, 16777215))
        self.btnPlay_a.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPlay_a.setCheckable(True)
        self.btnPlay_a.setChecked(False)

        self.verticalLayout_7.addWidget(self.btnPlay_a, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QDial{\n"
"	background-color: rgb(66, 121, 121);\n"
"	border: 5px solid blue;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(66, 121, 121);\n"
"	border-radius: 10px;\n"
"	border: 1px solid blue;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.frame_2.setLineWidth(5)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 0, 15)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.lb_b = QLabel(self.frame_2)
        self.lb_b.setObjectName(u"lb_b")
        self.lb_b.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setBold(True)
        self.lb_b.setFont(font1)

        self.verticalLayout_2.addWidget(self.lb_b, 0, Qt.AlignHCenter)

        self.dial_b = QDial(self.frame_2)
        self.dial_b.setObjectName(u"dial_b")
        self.dial_b.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_b.setSingleStep(10)
        self.dial_b.setNotchesVisible(True)

        self.verticalLayout_2.addWidget(self.dial_b)

        self.dlz_02 = QSlider(self.frame_2)
        self.dlz_02.setObjectName(u"dlz_02")
        self.dlz_02.setMaximumSize(QSize(16777215, 200))
        self.dlz_02.setCursor(QCursor(Qt.PointingHandCursor))
        self.dlz_02.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.dlz_02.setMaximum(49)
        self.dlz_02.setOrientation(Qt.Vertical)
        self.dlz_02.setTickPosition(QSlider.TicksBothSides)
        self.dlz_02.setTickInterval(2)

        self.verticalLayout_2.addWidget(self.dlz_02, 0, Qt.AlignHCenter)

        self.liga_Btn_02 = QPushButton(self.frame_2)
        self.liga_Btn_02.setObjectName(u"liga_Btn_02")
        self.liga_Btn_02.setMinimumSize(QSize(85, 30))
        self.liga_Btn_02.setMaximumSize(QSize(85, 16777215))
        self.liga_Btn_02.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.liga_Btn_02, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QDial{\n"
"	background-color: rgb(175, 0, 0);\n"
"}\n"
"QFrame{\n"
"	border: 1px solid gray;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(175, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 1px solid blue;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.frame_3.setLineWidth(5)
        self.verticalLayout_14 = QVBoxLayout(self.frame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, 0, 15)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.lb_c = QLabel(self.frame_3)
        self.lb_c.setObjectName(u"lb_c")
        self.lb_c.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_3.addWidget(self.lb_c, 0, Qt.AlignHCenter)

        self.dial_c = QDial(self.frame_3)
        self.dial_c.setObjectName(u"dial_c")
        self.dial_c.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_c.setSingleStep(10)
        self.dial_c.setNotchesVisible(True)

        self.verticalLayout_3.addWidget(self.dial_c)

        self.dlz_03 = QSlider(self.frame_3)
        self.dlz_03.setObjectName(u"dlz_03")
        self.dlz_03.setMaximumSize(QSize(16777215, 200))
        self.dlz_03.setCursor(QCursor(Qt.PointingHandCursor))
        self.dlz_03.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.dlz_03.setMaximum(49)
        self.dlz_03.setOrientation(Qt.Vertical)
        self.dlz_03.setTickPosition(QSlider.TicksBothSides)
        self.dlz_03.setTickInterval(2)

        self.verticalLayout_3.addWidget(self.dlz_03, 0, Qt.AlignHCenter)

        self.liga_Btn_03 = QPushButton(self.frame_3)
        self.liga_Btn_03.setObjectName(u"liga_Btn_03")
        self.liga_Btn_03.setMinimumSize(QSize(85, 30))
        self.liga_Btn_03.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.liga_Btn_03, 0, Qt.AlignHCenter)


        self.verticalLayout_14.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QDial{\n"
"	background-color: rgb(66, 121, 121);\n"
"	border: 5px solid blue;\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(66, 121, 121);\n"
"	border-radius: 10px;\n"
"	border: 1px solid blue;\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.frame_4.setLineWidth(5)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 10, 0, 15)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.label_d = QLabel(self.frame_4)
        self.label_d.setObjectName(u"label_d")
        self.label_d.setMaximumSize(QSize(16777215, 35))

        self.verticalLayout_4.addWidget(self.label_d, 0, Qt.AlignHCenter)

        self.dial_d = QDial(self.frame_4)
        self.dial_d.setObjectName(u"dial_d")
        self.dial_d.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial_d.setSingleStep(10)
        self.dial_d.setNotchesVisible(True)

        self.verticalLayout_4.addWidget(self.dial_d)

        self.dlz_04 = QSlider(self.frame_4)
        self.dlz_04.setObjectName(u"dlz_04")
        self.dlz_04.setMaximumSize(QSize(16777215, 200))
        self.dlz_04.setCursor(QCursor(Qt.PointingHandCursor))
        self.dlz_04.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.dlz_04.setMaximum(49)
        self.dlz_04.setOrientation(Qt.Vertical)
        self.dlz_04.setTickPosition(QSlider.TicksBothSides)
        self.dlz_04.setTickInterval(2)

        self.verticalLayout_4.addWidget(self.dlz_04, 0, Qt.AlignHCenter)

        self.liga_Btn_04 = QPushButton(self.frame_4)
        self.liga_Btn_04.setObjectName(u"liga_Btn_04")
        self.liga_Btn_04.setMinimumSize(QSize(85, 30))
        self.liga_Btn_04.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.liga_Btn_04, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.frame_4)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_a.setText(QCoreApplication.translate("MainWindow", u"ENTRADA A", None))
        self.btnPlay_a.setText(QCoreApplication.translate("MainWindow", u"LIgar", None))
        self.lb_b.setText(QCoreApplication.translate("MainWindow", u"ENTRADA B", None))
        self.liga_Btn_02.setText(QCoreApplication.translate("MainWindow", u"LIgar", None))
        self.lb_c.setText(QCoreApplication.translate("MainWindow", u"ENTRADA A", None))
        self.liga_Btn_03.setText(QCoreApplication.translate("MainWindow", u"LIgar", None))
        self.label_d.setText(QCoreApplication.translate("MainWindow", u"ENTRADA B", None))
        self.liga_Btn_04.setText(QCoreApplication.translate("MainWindow", u"LIgar", None))
    # retranslateUi

