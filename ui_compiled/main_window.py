# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import ui_compiled.source

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 618)
        MainWindow.setIconSize(QSize(50, 50))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.settings_btn = QPushButton(self.centralwidget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setGeometry(QRect(960, 530, 81, 81))
        self.settings_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_btn.setStyleSheet(u"background-color: linear-gradient(130deg, rgba(59,58,72,0.6646557548800771) 0%, rgba(67,61,57,0.9279610770089286) 42%, rgba(141,129,113,1) 71%);")
        icon = QIcon()
        icon.addFile(u":/images/images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon)
        self.settings_btn.setIconSize(QSize(50, 50))
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 10, 371, 40))
        self.title.setStyleSheet(u"font-size: 30px;\n"
"font-weight: 600;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 550, 571, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(35)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_data_btn = QPushButton(self.layoutWidget)
        self.add_data_btn.setObjectName(u"add_data_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_data_btn.sizePolicy().hasHeightForWidth())
        self.add_data_btn.setSizePolicy(sizePolicy)
        self.add_data_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_data_btn.setStyleSheet(u"QPushButton#add_data_btn{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#add_data_btn{\n"
"	background-color: rgb(230, 250, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.add_data_btn)

        self.predict_btn = QPushButton(self.layoutWidget)
        self.predict_btn.setObjectName(u"predict_btn")
        sizePolicy.setHeightForWidth(self.predict_btn.sizePolicy().hasHeightForWidth())
        self.predict_btn.setSizePolicy(sizePolicy)
        self.predict_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.predict_btn.setStyleSheet(u"QPushButton#predict_btn{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#predict_btn{\n"
"	background-color: rgb(230, 250, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.predict_btn)

        self.features_btn = QPushButton(self.layoutWidget)
        self.features_btn.setObjectName(u"features_btn")
        sizePolicy.setHeightForWidth(self.features_btn.sizePolicy().hasHeightForWidth())
        self.features_btn.setSizePolicy(sizePolicy)
        self.features_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.features_btn.setStyleSheet(u"QPushButton#features_btn{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#features_btn{\n"
"	background-color: rgb(230, 250, 255);\n"
"}")

        self.horizontalLayout.addWidget(self.features_btn)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(900, 20, 131, 74))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 25px;\n"
"font-weight: 550;")

        self.verticalLayout.addWidget(self.label)

        self.result_tbx = QLineEdit(self.layoutWidget1)
        self.result_tbx.setObjectName(u"result_tbx")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.result_tbx.sizePolicy().hasHeightForWidth())
        self.result_tbx.setSizePolicy(sizePolicy1)
        self.result_tbx.setStyleSheet(u"font-weight: 400;\n"
"font-size: 20px;")

        self.verticalLayout.addWidget(self.result_tbx)

        self.plot_lbl = QLabel(self.centralwidget)
        self.plot_lbl.setObjectName(u"plot_lbl")
        self.plot_lbl.setEnabled(True)
        self.plot_lbl.setGeometry(QRect(180, 60, 641, 481))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.settings_btn.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.add_data_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.predict_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u043f\u0440\u043e\u0433\u043d\u043e\u0437", None))
        self.features_btn.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.plot_lbl.setText("")
    # retranslateUi

