# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cluster.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)

class Ui_ClusterWindow(object):
    def setupUi(self, ClusterWindow):
        if not ClusterWindow.objectName():
            ClusterWindow.setObjectName(u"ClusterWindow")
        ClusterWindow.resize(1135, 699)
        self.importDataButton = QPushButton(ClusterWindow)
        self.importDataButton.setObjectName(u"importDataButton")
        self.importDataButton.setGeometry(QRect(20, 510, 121, 41))
        self.importDataButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.importDataButton.setStyleSheet(u"QPushButton#importDataButton{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#importDataButton{\n"
"	background-color: rgb(179, 236, 255);\n"
"}\n"
"")
        self.importDataButton.setAutoDefault(True)
        self.enterDataButton = QPushButton(ClusterWindow)
        self.enterDataButton.setObjectName(u"enterDataButton")
        self.enterDataButton.setGeometry(QRect(170, 510, 131, 41))
        self.enterDataButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.enterDataButton.setStyleSheet(u"QPushButton#enterDataButton{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#enterDataButton{\n"
"	background-color: rgb(179, 236, 255);\n"
"}\n"
"")
        self.enterDataButton.setAutoDefault(True)
        self.layoutWidget = QWidget(ClusterWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 921, 481))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 33px;\n"
"font-weight: 600;")

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setStyleSheet(u"color: rgb(0, 204, 255);")
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(2)

        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.dataView = QTableView(self.layoutWidget)
        self.dataView.setObjectName(u"dataView")

        self.verticalLayout_2.addWidget(self.dataView)

        self.metricFeatures_scrollArea = QScrollArea(ClusterWindow)
        self.metricFeatures_scrollArea.setObjectName(u"metricFeatures_scrollArea")
        self.metricFeatures_scrollArea.setGeometry(QRect(950, 70, 161, 421))
        self.metricFeatures_scrollArea.setWidgetResizable(True)
        self.checkBoxContainer = QWidget()
        self.checkBoxContainer.setObjectName(u"checkBoxContainer")
        self.checkBoxContainer.setGeometry(QRect(0, 0, 159, 419))
        self.metricFeatures_scrollArea.setWidget(self.checkBoxContainer)
        self.analyzeButton = QPushButton(ClusterWindow)
        self.analyzeButton.setObjectName(u"analyzeButton")
        self.analyzeButton.setGeometry(QRect(960, 510, 131, 41))
        self.analyzeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.analyzeButton.setStyleSheet(u"QPushButton#analyzeButton{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#analyzeButton{\n"
"	background-color: rgb(179, 236, 255);\n"
"}\n"
"")
        self.analyzeButton.setAutoDefault(True)
        self.layoutWidget1 = QWidget(ClusterWindow)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 560, 316, 81))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 400;")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioKMeans = QRadioButton(self.layoutWidget1)
        self.radioKMeans.setObjectName(u"radioKMeans")
        self.radioKMeans.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioKMeans.setStyleSheet(u"font-size: 18px;\n"
"color: rgb(0, 204, 255);")

        self.horizontalLayout.addWidget(self.radioKMeans)

        self.radioDBSCAN = QRadioButton(self.layoutWidget1)
        self.radioDBSCAN.setObjectName(u"radioDBSCAN")
        self.radioDBSCAN.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioDBSCAN.setStyleSheet(u"font-size: 18px;\n"
"color: rgb(0, 204, 255);")

        self.horizontalLayout.addWidget(self.radioDBSCAN)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.layoutWidget2 = QWidget(ClusterWindow)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(360, 560, 161, 81))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 400;")

        self.verticalLayout_4.addWidget(self.label_3)

        self.numClusters_tbx = QLineEdit(self.layoutWidget2)
        self.numClusters_tbx.setObjectName(u"numClusters_tbx")
        self.numClusters_tbx.setStyleSheet(u"font-size: 18px;")

        self.verticalLayout_4.addWidget(self.numClusters_tbx)


        self.retranslateUi(ClusterWindow)

        QMetaObject.connectSlotsByName(ClusterWindow)
    # setupUi

    def retranslateUi(self, ClusterWindow):
        ClusterWindow.setWindowTitle(QCoreApplication.translate("ClusterWindow", u"Dialog", None))
        self.importDataButton.setText(QCoreApplication.translate("ClusterWindow", u"Import data", None))
        self.enterDataButton.setText(QCoreApplication.translate("ClusterWindow", u"Enter Data", None))
        self.label.setText(QCoreApplication.translate("ClusterWindow", u"\u041a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.analyzeButton.setText(QCoreApplication.translate("ClusterWindow", u"Analyze", None))
        self.label_2.setText(QCoreApplication.translate("ClusterWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.radioKMeans.setText(QCoreApplication.translate("ClusterWindow", u"K-Means Cluster", None))
        self.radioDBSCAN.setText(QCoreApplication.translate("ClusterWindow", u"DBSCAN Cluster", None))
        self.label_3.setText(QCoreApplication.translate("ClusterWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u043e\u0432", None))
    # retranslateUi

