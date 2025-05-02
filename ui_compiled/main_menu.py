# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        if not MenuWindow.objectName():
            MenuWindow.setObjectName(u"MenuWindow")
        MenuWindow.resize(715, 458)
        self.centralwidget = QWidget(MenuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.clusterWindowButton = QPushButton(self.centralwidget)
        self.clusterWindowButton.setObjectName(u"clusterWindowButton")
        self.clusterWindowButton.setGeometry(QRect(20, 290, 221, 61))
        self.clusterWindowButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clusterWindowButton.setStyleSheet(u"QPushButton#clusterWindowButton{\n"
"	font-size: 25px;\n"
"	color: white;	\n"
"	border-radius: 12px;\n"
"	background-color:  rgb(0, 204, 255);\n"
"}\n"
"\n"
"QPushButton:hover#clusterWindowButton{\n"
"	background-color: rgb(179, 240, 255);\n"
"	color: rgb(0, 204, 255);\n"
"}\n"
"")
        self.clusterWindowButton.setAutoDefault(True)
        self.predictWindowButton = QPushButton(self.centralwidget)
        self.predictWindowButton.setObjectName(u"predictWindowButton")
        self.predictWindowButton.setGeometry(QRect(20, 180, 221, 61))
        self.predictWindowButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.predictWindowButton.setStyleSheet(u"QPushButton#predictWindowButton{\n"
"	font-size: 25px;\n"
"	color: white;	\n"
"	border-radius: 12px;\n"
"	background-color:  rgb(0, 204, 255);\n"
"}\n"
"\n"
"QPushButton:hover#predictWindowButton{\n"
"	background-color: rgb(179, 240, 255);\n"
"	color: rgb(0, 204, 255);\n"
"}\n"
"")
        self.predictWindowButton.setAutoDefault(True)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 40, 331, 61))
        self.title.setStyleSheet(u"font-size: 33px;\n"
"font-weight: 600;")
        self.title_2 = QLabel(self.centralwidget)
        self.title_2.setObjectName(u"title_2")
        self.title_2.setGeometry(QRect(20, 100, 91, 61))
        self.title_2.setStyleSheet(u"font-size: 28px;\n"
"font-weight: 400;")
        self.title_3 = QLabel(self.centralwidget)
        self.title_3.setObjectName(u"title_3")
        self.title_3.setGeometry(QRect(260, 180, 361, 61))
        self.title_3.setStyleSheet(u"font-size: 20px;\n"
"font-weight: 400;")
        self.title_4 = QLabel(self.centralwidget)
        self.title_4.setObjectName(u"title_4")
        self.title_4.setGeometry(QRect(260, 290, 311, 61))
        self.title_4.setStyleSheet(u"font-size: 20px;\n"
"font-weight: 400;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(20, 90, 611, 20))
        self.frame.setStyleSheet(u"color: rgb(0, 204, 255);")
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)
        MenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuWindow)

        QMetaObject.connectSlotsByName(MenuWindow)
    # setupUi

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(QCoreApplication.translate("MenuWindow", u"MainWindow", None))
        self.clusterWindowButton.setText(QCoreApplication.translate("MenuWindow", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.predictWindowButton.setText(QCoreApplication.translate("MenuWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.title.setText(QCoreApplication.translate("MenuWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0434\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0438", None))
        self.title_2.setText(QCoreApplication.translate("MenuWindow", u"\u041c\u0435\u043d\u044e", None))
        self.title_3.setText(QCoreApplication.translate("MenuWindow", u"\u043f\u0440\u043e\u0433\u043d\u043e\u0437 \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0431\u0430\u043b\u043b\u0430 \u0443\u0441\u043f\u0435\u0432\u0430\u0435\u043c\u043e\u0441\u0442\u0438", None))
        self.title_4.setText(QCoreApplication.translate("MenuWindow", u"\u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f K-Means, DBSCAN", None))
    # retranslateUi

