# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ClusterResults.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_ClusterResultsWindow(object):
    def setupUi(self, ClusterResultsWindow):
        if not ClusterResultsWindow.objectName():
            ClusterResultsWindow.setObjectName(u"ClusterResultsWindow")
        ClusterResultsWindow.resize(1001, 709)
        self.layoutWidget = QWidget(ClusterResultsWindow)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 451, 62))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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

        self.elbow_title_lbl = QLabel(ClusterResultsWindow)
        self.elbow_title_lbl.setObjectName(u"elbow_title_lbl")
        self.elbow_title_lbl.setGeometry(QRect(340, 90, 181, 44))
        self.elbow_title_lbl.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 400;")
        self.fileButton = QPushButton(ClusterResultsWindow)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setGeometry(QRect(20, 620, 171, 41))
        self.fileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fileButton.setStyleSheet(u"QPushButton#fileButton{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#fileButton{\n"
"	background-color: rgb(230, 250, 255);\n"
"}\n"
"")
        self.fileButton.setAutoDefault(True)
        self.clusterScatterButton = QPushButton(ClusterResultsWindow)
        self.clusterScatterButton.setObjectName(u"clusterScatterButton")
        self.clusterScatterButton.setGeometry(QRect(220, 620, 141, 41))
        self.clusterScatterButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.clusterScatterButton.setStyleSheet(u"QPushButton#clusterScatterButton{\n"
"	font-size: 18px;\n"
"	color: rgb(0, 204, 255);	\n"
"	border-radius: 12px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover#clusterScatterButton{\n"
"	background-color: rgb(230, 250, 255);\n"
"}\n"
"")
        self.clusterScatterButton.setAutoDefault(True)
        self.elbow_lbl = QLabel(ClusterResultsWindow)
        self.elbow_lbl.setObjectName(u"elbow_lbl")
        self.elbow_lbl.setEnabled(True)
        self.elbow_lbl.setGeometry(QRect(350, 130, 601, 451))
        self.elbow_lbl.setMidLineWidth(2)
        self.layoutWidget1 = QWidget(ClusterResultsWindow)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(21, 101, 293, 228))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.centers_lbl = QLabel(self.layoutWidget1)
        self.centers_lbl.setObjectName(u"centers_lbl")
        self.centers_lbl.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 400;")

        self.verticalLayout_2.addWidget(self.centers_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.centersView = QTableView(self.layoutWidget1)
        self.centersView.setObjectName(u"centersView")

        self.horizontalLayout.addWidget(self.centersView)

        self.frame_2 = QFrame(self.layoutWidget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"color: rgb(0, 204, 255);")
        self.frame_2.setFrameShape(QFrame.Shape.VLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)

        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.layoutWidget2 = QWidget(ClusterResultsWindow)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(21, 351, 293, 228))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stats_lbl = QLabel(self.layoutWidget2)
        self.stats_lbl.setObjectName(u"stats_lbl")
        self.stats_lbl.setStyleSheet(u"font-size: 19px;\n"
"font-weight: 400;")

        self.verticalLayout_3.addWidget(self.stats_lbl)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.clusterStatsView = QTableView(self.layoutWidget2)
        self.clusterStatsView.setObjectName(u"clusterStatsView")

        self.horizontalLayout_2.addWidget(self.clusterStatsView)

        self.frame_3 = QFrame(self.layoutWidget2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"color: rgb(0, 204, 255);")
        self.frame_3.setFrameShape(QFrame.Shape.VLine)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(0)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ClusterResultsWindow)

        QMetaObject.connectSlotsByName(ClusterResultsWindow)
    # setupUi

    def retranslateUi(self, ClusterResultsWindow):
        ClusterResultsWindow.setWindowTitle(QCoreApplication.translate("ClusterResultsWindow", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ClusterResultsWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.elbow_title_lbl.setText(QCoreApplication.translate("ClusterResultsWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u043e \u041b\u043e\u043a\u0442\u044f", None))
        self.fileButton.setText(QCoreApplication.translate("ClusterResultsWindow", u"Download Results", None))
        self.clusterScatterButton.setText(QCoreApplication.translate("ClusterResultsWindow", u"Scatter Plot", None))
        self.elbow_lbl.setText("")
        self.centers_lbl.setText(QCoreApplication.translate("ClusterResultsWindow", u"\u0426\u0435\u043d\u0442\u0440\u044b \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u043e\u0432", None))
        self.stats_lbl.setText(QCoreApplication.translate("ClusterResultsWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
    # retranslateUi

