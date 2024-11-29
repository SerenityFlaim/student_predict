# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Student_data(object):
    def setupUi(self, Student_data):
        if not Student_data.objectName():
            Student_data.setObjectName(u"Student_data")
        Student_data.resize(510, 391)
        self.buttonBox = QDialogButtonBox(Student_data)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(170, 360, 161, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.data_title_lbl = QLabel(Student_data)
        self.data_title_lbl.setObjectName(u"data_title_lbl")
        self.data_title_lbl.setGeometry(QRect(10, 10, 221, 31))
        self.data_title_lbl.setStyleSheet(u"font-size: 25px;\n"
"font-weight: 500;")
        self.layoutWidget = QWidget(Student_data)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 51, 121, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout.addWidget(self.label)

        self.gender_cbx = QComboBox(self.layoutWidget)
        self.gender_cbx.addItem("")
        self.gender_cbx.addItem("")
        self.gender_cbx.setObjectName(u"gender_cbx")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gender_cbx.sizePolicy().hasHeightForWidth())
        self.gender_cbx.setSizePolicy(sizePolicy)
        self.gender_cbx.setStyleSheet(u"text-align: center;\n"
"font-size: 15px;")

        self.horizontalLayout.addWidget(self.gender_cbx)

        self.layoutWidget1 = QWidget(Student_data)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 190, 201, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.job_lbl = QLabel(self.layoutWidget1)
        self.job_lbl.setObjectName(u"job_lbl")
        self.job_lbl.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_2.addWidget(self.job_lbl)

        self.job_cbx = QComboBox(self.layoutWidget1)
        self.job_cbx.addItem("")
        self.job_cbx.addItem("")
        self.job_cbx.setObjectName(u"job_cbx")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.job_cbx.sizePolicy().hasHeightForWidth())
        self.job_cbx.setSizePolicy(sizePolicy1)
        self.job_cbx.setStyleSheet(u"font-size: 15px;")

        self.horizontalLayout_2.addWidget(self.job_cbx)

        self.widget = QWidget(Student_data)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 240, 331, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.activity_lbl = QLabel(self.widget)
        self.activity_lbl.setObjectName(u"activity_lbl")
        self.activity_lbl.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_5.addWidget(self.activity_lbl)

        self.activity_cbx = QComboBox(self.widget)
        self.activity_cbx.addItem("")
        self.activity_cbx.addItem("")
        self.activity_cbx.setObjectName(u"activity_cbx")
        sizePolicy1.setHeightForWidth(self.activity_cbx.sizePolicy().hasHeightForWidth())
        self.activity_cbx.setSizePolicy(sizePolicy1)
        self.activity_cbx.setStyleSheet(u"font-size: 15px;")

        self.horizontalLayout_5.addWidget(self.activity_cbx)

        self.widget1 = QWidget(Student_data)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 100, 489, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hours_lbl = QLabel(self.widget1)
        self.hours_lbl.setObjectName(u"hours_lbl")
        self.hours_lbl.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_3.addWidget(self.hours_lbl)

        self.hours_tbx = QLineEdit(self.widget1)
        self.hours_tbx.setObjectName(u"hours_tbx")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.hours_tbx.sizePolicy().hasHeightForWidth())
        self.hours_tbx.setSizePolicy(sizePolicy2)
        self.hours_tbx.setStyleSheet(u"font-weight: 400;\n"
"font-size: 16px;")

        self.horizontalLayout_3.addWidget(self.hours_tbx)

        self.widget2 = QWidget(Student_data)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 290, 221, 29))
        self.horizontalLayout_6 = QHBoxLayout(self.widget2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.skips_lbl = QLabel(self.widget2)
        self.skips_lbl.setObjectName(u"skips_lbl")
        self.skips_lbl.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_6.addWidget(self.skips_lbl)

        self.skips_tbx = QLineEdit(self.widget2)
        self.skips_tbx.setObjectName(u"skips_tbx")
        sizePolicy2.setHeightForWidth(self.skips_tbx.sizePolicy().hasHeightForWidth())
        self.skips_tbx.setSizePolicy(sizePolicy2)
        self.skips_tbx.setStyleSheet(u"font-weight: 400;\n"
"font-size: 16px;")

        self.horizontalLayout_6.addWidget(self.skips_tbx)

        self.widget3 = QWidget(Student_data)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(10, 140, 381, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.prof_lbl = QLabel(self.widget3)
        self.prof_lbl.setObjectName(u"prof_lbl")
        self.prof_lbl.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_4.addWidget(self.prof_lbl)

        self.prof_cbx = QComboBox(self.widget3)
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.addItem("")
        self.prof_cbx.setObjectName(u"prof_cbx")
        sizePolicy1.setHeightForWidth(self.prof_cbx.sizePolicy().hasHeightForWidth())
        self.prof_cbx.setSizePolicy(sizePolicy1)
        self.prof_cbx.setStyleSheet(u"font-size: 15px;")

        self.horizontalLayout_4.addWidget(self.prof_cbx)


        self.retranslateUi(Student_data)
        self.buttonBox.accepted.connect(Student_data.accept)
        self.buttonBox.rejected.connect(Student_data.reject)

        QMetaObject.connectSlotsByName(Student_data)
    # setupUi

    def retranslateUi(self, Student_data):
        Student_data.setWindowTitle(QCoreApplication.translate("Student_data", u"Dialog", None))
        self.data_title_lbl.setText(QCoreApplication.translate("Student_data", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0435", None))
        self.label.setText(QCoreApplication.translate("Student_data", u"\u041f\u043e\u043b:", None))
        self.gender_cbx.setItemText(0, QCoreApplication.translate("Student_data", u"\u041c", None))
        self.gender_cbx.setItemText(1, QCoreApplication.translate("Student_data", u"\u0416", None))

        self.job_lbl.setText(QCoreApplication.translate("Student_data", u"\u041f\u043e\u0434\u0440\u0430\u0431\u043e\u0442\u043a\u0430:", None))
        self.job_cbx.setItemText(0, QCoreApplication.translate("Student_data", u"\u041d\u0435\u0442", None))
        self.job_cbx.setItemText(1, QCoreApplication.translate("Student_data", u"\u0415\u0441\u0442\u044c", None))

        self.activity_lbl.setText(QCoreApplication.translate("Student_data", u"\u0412\u043d\u0435\u0443\u0440\u043e\u0447\u043d\u0430\u044f \u0434\u0435\u044f\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c: ", None))
        self.activity_cbx.setItemText(0, QCoreApplication.translate("Student_data", u"\u041d\u0435\u0442", None))
        self.activity_cbx.setItemText(1, QCoreApplication.translate("Student_data", u"\u0415\u0441\u0442\u044c", None))

        self.hours_lbl.setText(QCoreApplication.translate("Student_data", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0447\u0438\u0441\u043b\u043e \u0441\u0430\u043c\u043e\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f \u0432 \u043d\u0435\u0434\u0435\u043b\u044e: ", None))
        self.skips_lbl.setText(QCoreApplication.translate("Student_data", u"\u041f\u0440\u043e\u043f\u0443\u0441\u043a\u0438:        ", None))
        self.prof_lbl.setText(QCoreApplication.translate("Student_data", u"\u041a\u0430\u0440\u044c\u0435\u0440\u043d\u043e\u0435 \u0441\u0442\u0440\u0435\u043c\u043b\u0435\u043d\u0438\u0435:", None))
        self.prof_cbx.setItemText(0, QCoreApplication.translate("Student_data", u"\u0418\u043d\u0436\u0435\u043d\u0435\u0440 \u041f\u041e", None))
        self.prof_cbx.setItemText(1, QCoreApplication.translate("Student_data", u"\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446 \u0431\u0438\u0437\u043d\u0435\u0441\u0430", None))
        self.prof_cbx.setItemText(2, QCoreApplication.translate("Student_data", u"\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e", None))
        self.prof_cbx.setItemText(3, QCoreApplication.translate("Student_data", u"\u0411\u0430\u043d\u043a\u0438\u0440", None))
        self.prof_cbx.setItemText(4, QCoreApplication.translate("Student_data", u"\u042e\u0440\u0438\u0441\u0442", None))
        self.prof_cbx.setItemText(5, QCoreApplication.translate("Student_data", u"\u0411\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440", None))
        self.prof_cbx.setItemText(6, QCoreApplication.translate("Student_data", u"\u0414\u043e\u043a\u0442\u043e\u0440", None))
        self.prof_cbx.setItemText(7, QCoreApplication.translate("Student_data", u"\u0417\u0430\u0441\u0442\u0440\u043e\u0439\u0449\u0438\u043a", None))
        self.prof_cbx.setItemText(8, QCoreApplication.translate("Student_data", u"\u0425\u0443\u0434\u043e\u0436\u043d\u0438\u043a", None))
        self.prof_cbx.setItemText(9, QCoreApplication.translate("Student_data", u"\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a \u0438\u0433\u0440", None))
        self.prof_cbx.setItemText(10, QCoreApplication.translate("Student_data", u"\u0413\u043e\u0441 \u0441\u043b\u0443\u0436\u0430\u0449\u0438\u0439", None))
        self.prof_cbx.setItemText(11, QCoreApplication.translate("Student_data", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.prof_cbx.setItemText(12, QCoreApplication.translate("Student_data", u"\u0414\u0438\u0437\u0430\u0439\u043d\u0435\u0440", None))
        self.prof_cbx.setItemText(13, QCoreApplication.translate("Student_data", u"\u0423\u0447\u0451\u043d\u044b\u0439", None))
        self.prof_cbx.setItemText(14, QCoreApplication.translate("Student_data", u"\u041f\u0438\u0441\u0430\u0442\u0435\u043b\u044c", None))

    # retranslateUi

