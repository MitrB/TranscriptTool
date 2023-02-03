# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(534, 539)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 511, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.openFileButton = QPushButton(self.verticalLayoutWidget)
        self.openFileButton.setObjectName(u"openFileButton")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.openFileButton.setFont(font)

        self.verticalLayout_2.addWidget(self.openFileButton)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.path_label = QLabel(self.verticalLayoutWidget)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setAlignment(Qt.AlignCenter)
        self.path_label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.path_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setUnderline(False)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.option_language = QComboBox(self.verticalLayoutWidget)
        self.option_language.addItem("")
        self.option_language.addItem("")
        self.option_language.addItem("")
        self.option_language.setObjectName(u"option_language")

        self.verticalLayout_4.addWidget(self.option_language)

        self.option_precision = QComboBox(self.verticalLayoutWidget)
        self.option_precision.addItem("")
        self.option_precision.addItem("")
        self.option_precision.addItem("")
        self.option_precision.addItem("")
        self.option_precision.addItem("")
        self.option_precision.setObjectName(u"option_precision")

        self.verticalLayout_4.addWidget(self.option_precision)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.transcribeButton = QPushButton(self.verticalLayoutWidget)
        self.transcribeButton.setObjectName(u"transcribeButton")
        self.transcribeButton.setBaseSize(QSize(100, 0))
        self.transcribeButton.setFont(font)

        self.horizontalLayout_6.addWidget(self.transcribeButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font4 = QFont()
        font4.setItalic(True)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.status_label = QLabel(self.verticalLayoutWidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font)
        self.status_label.setTextFormat(Qt.AutoText)
        self.status_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status_label)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 534, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.openFileButton.clicked.connect(MainWindow.open_file)
        self.transcribeButton.clicked.connect(MainWindow.transcribe_file)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File Path:", None))
        self.path_label.setText(QCoreApplication.translate("MainWindow", u"<Path>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Language:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Model Precision:", None))
        self.option_language.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.option_language.setItemText(1, QCoreApplication.translate("MainWindow", u"Nederlands", None))
        self.option_language.setItemText(2, QCoreApplication.translate("MainWindow", u"Francais", None))

        self.option_precision.setItemText(0, QCoreApplication.translate("MainWindow", u"very low", None))
        self.option_precision.setItemText(1, QCoreApplication.translate("MainWindow", u"low", None))
        self.option_precision.setItemText(2, QCoreApplication.translate("MainWindow", u"medium", None))
        self.option_precision.setItemText(3, QCoreApplication.translate("MainWindow", u"high", None))
        self.option_precision.setItemText(4, QCoreApplication.translate("MainWindow", u"very high", None))

        self.transcribeButton.setText(QCoreApplication.translate("MainWindow", u"Transcribe", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Choose audio file", None))
    # retranslateUi

