# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(395, 289)
        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 250, 161, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.Settings_lbl = QLabel(Settings)
        self.Settings_lbl.setObjectName(u"Settings_lbl")
        self.Settings_lbl.setGeometry(QRect(10, 10, 131, 31))
        self.Settings_lbl.setStyleSheet(u"font-size: 25px;\n"
"font-weight: 500;")
        self.layoutWidget = QWidget(Settings)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 201, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.model_lbl = QLabel(self.layoutWidget)
        self.model_lbl.setObjectName(u"model_lbl")
        self.model_lbl.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_2.addWidget(self.model_lbl)

        self.model_cbx = QComboBox(self.layoutWidget)
        self.model_cbx.addItem("")
        self.model_cbx.addItem("")
        self.model_cbx.setObjectName(u"model_cbx")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_cbx.sizePolicy().hasHeightForWidth())
        self.model_cbx.setSizePolicy(sizePolicy)
        self.model_cbx.setStyleSheet(u"font-size: 15px;")

        self.horizontalLayout_2.addWidget(self.model_cbx)


        self.retranslateUi(Settings)
        self.buttonBox.accepted.connect(Settings.accepted) #accept
        self.buttonBox.rejected.connect(Settings.rect) #reject

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Dialog", None))
        self.Settings_lbl.setText(QCoreApplication.translate("Settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.model_lbl.setText(QCoreApplication.translate("Settings", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.model_cbx.setItemText(0, QCoreApplication.translate("Settings", u"Sequential", None))
        self.model_cbx.setItemText(1, QCoreApplication.translate("Settings", u"XGB", None))

    # retranslateUi

