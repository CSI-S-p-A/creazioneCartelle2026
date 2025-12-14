# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(971, 828)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_tests = QWidget()
        self.tab_tests.setObjectName(u"tab_tests")
        self.tableWidget = QTableWidget(self.tab_tests)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 110, 871, 611))
        self.widget = QWidget(self.tab_tests)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 871, 61))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 0, 1, 1, 1)

        self.combo_test_type = QComboBox(self.widget)
        self.combo_test_type.setObjectName(u"combo_test_type")

        self.gridLayout_5.addWidget(self.combo_test_type, 1, 0, 1, 1)

        self.combo_test_name = QComboBox(self.widget)
        self.combo_test_name.setObjectName(u"combo_test_name")

        self.gridLayout_5.addWidget(self.combo_test_name, 1, 1, 1, 1)

        self.button_add_new_test = QPushButton(self.widget)
        self.button_add_new_test.setObjectName(u"button_add_new_test")

        self.gridLayout_5.addWidget(self.button_add_new_test, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_tests, "")
        self.tab_dimensions = QWidget()
        self.tab_dimensions.setObjectName(u"tab_dimensions")
        self.label = QLabel(self.tab_dimensions)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 958, 814))
        self.label.setPixmap(QPixmap(u":/car/car2.svg"))
        self.label.setScaledContents(False)
        self.groupBox = QGroupBox(self.tab_dimensions)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(270, 570, 431, 90))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.x3Back = QLineEdit(self.groupBox)
        self.x3Back.setObjectName(u"x3Back")

        self.gridLayout_2.addWidget(self.x3Back, 0, 3, 1, 1)

        self.y5Back = QLineEdit(self.groupBox)
        self.y5Back.setObjectName(u"y5Back")

        self.gridLayout_2.addWidget(self.y5Back, 1, 5, 1, 1)

        self.y3Back = QLineEdit(self.groupBox)
        self.y3Back.setObjectName(u"y3Back")

        self.gridLayout_2.addWidget(self.y3Back, 1, 3, 1, 1)

        self.x7Back = QLineEdit(self.groupBox)
        self.x7Back.setObjectName(u"x7Back")

        self.gridLayout_2.addWidget(self.x7Back, 0, 7, 1, 1)

        self.y2Back = QLineEdit(self.groupBox)
        self.y2Back.setObjectName(u"y2Back")

        self.gridLayout_2.addWidget(self.y2Back, 1, 2, 1, 1)

        self.y6Back = QLineEdit(self.groupBox)
        self.y6Back.setObjectName(u"y6Back")

        self.gridLayout_2.addWidget(self.y6Back, 1, 6, 1, 1)

        self.x5Back = QLineEdit(self.groupBox)
        self.x5Back.setObjectName(u"x5Back")

        self.gridLayout_2.addWidget(self.x5Back, 0, 5, 1, 1)

        self.x6Back = QLineEdit(self.groupBox)
        self.x6Back.setObjectName(u"x6Back")

        self.gridLayout_2.addWidget(self.x6Back, 0, 6, 1, 1)

        self.y4Back = QLineEdit(self.groupBox)
        self.y4Back.setObjectName(u"y4Back")

        self.gridLayout_2.addWidget(self.y4Back, 1, 4, 1, 1)

        self.y1Back = QLineEdit(self.groupBox)
        self.y1Back.setObjectName(u"y1Back")

        self.gridLayout_2.addWidget(self.y1Back, 1, 1, 1, 1)

        self.x4Back = QLineEdit(self.groupBox)
        self.x4Back.setObjectName(u"x4Back")

        self.gridLayout_2.addWidget(self.x4Back, 0, 4, 1, 1)

        self.x2Back = QLineEdit(self.groupBox)
        self.x2Back.setObjectName(u"x2Back")

        self.gridLayout_2.addWidget(self.x2Back, 0, 2, 1, 1)

        self.x1Back = QLineEdit(self.groupBox)
        self.x1Back.setObjectName(u"x1Back")

        self.gridLayout_2.addWidget(self.x1Back, 0, 1, 1, 1)

        self.y7Back = QLineEdit(self.groupBox)
        self.y7Back.setObjectName(u"y7Back")

        self.gridLayout_2.addWidget(self.y7Back, 1, 7, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.groupBox_2 = QGroupBox(self.tab_dimensions)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(260, 50, 441, 90))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.x3Front = QLineEdit(self.groupBox_2)
        self.x3Front.setObjectName(u"x3Front")

        self.gridLayout.addWidget(self.x3Front, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.y3Front = QLineEdit(self.groupBox_2)
        self.y3Front.setObjectName(u"y3Front")

        self.gridLayout.addWidget(self.y3Front, 1, 3, 1, 1)

        self.y2Front = QLineEdit(self.groupBox_2)
        self.y2Front.setObjectName(u"y2Front")

        self.gridLayout.addWidget(self.y2Front, 1, 2, 1, 1)

        self.y6Front = QLineEdit(self.groupBox_2)
        self.y6Front.setObjectName(u"y6Front")

        self.gridLayout.addWidget(self.y6Front, 1, 6, 1, 1)

        self.x4Front = QLineEdit(self.groupBox_2)
        self.x4Front.setObjectName(u"x4Front")

        self.gridLayout.addWidget(self.x4Front, 0, 4, 1, 1)

        self.y7Front = QLineEdit(self.groupBox_2)
        self.y7Front.setObjectName(u"y7Front")

        self.gridLayout.addWidget(self.y7Front, 1, 7, 1, 1)

        self.y4Front = QLineEdit(self.groupBox_2)
        self.y4Front.setObjectName(u"y4Front")

        self.gridLayout.addWidget(self.y4Front, 1, 4, 1, 1)

        self.y5Front = QLineEdit(self.groupBox_2)
        self.y5Front.setObjectName(u"y5Front")

        self.gridLayout.addWidget(self.y5Front, 1, 5, 1, 1)

        self.y1Front = QLineEdit(self.groupBox_2)
        self.y1Front.setObjectName(u"y1Front")

        self.gridLayout.addWidget(self.y1Front, 1, 1, 1, 1)

        self.x5Front = QLineEdit(self.groupBox_2)
        self.x5Front.setObjectName(u"x5Front")

        self.gridLayout.addWidget(self.x5Front, 0, 5, 1, 1)

        self.x6Front = QLineEdit(self.groupBox_2)
        self.x6Front.setObjectName(u"x6Front")

        self.gridLayout.addWidget(self.x6Front, 0, 6, 1, 1)

        self.x7Front = QLineEdit(self.groupBox_2)
        self.x7Front.setObjectName(u"x7Front")

        self.gridLayout.addWidget(self.x7Front, 0, 7, 1, 1)

        self.x2Front = QLineEdit(self.groupBox_2)
        self.x2Front.setObjectName(u"x2Front")

        self.gridLayout.addWidget(self.x2Front, 0, 2, 1, 1)

        self.x1Front = QLineEdit(self.groupBox_2)
        self.x1Front.setObjectName(u"x1Front")

        self.gridLayout.addWidget(self.x1Front, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.groupBox_3 = QGroupBox(self.tab_dimensions)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(620, 230, 141, 251))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 1, 1, 1)

        self.x1Side = QLineEdit(self.groupBox_3)
        self.x1Side.setObjectName(u"x1Side")

        self.gridLayout_3.addWidget(self.x1Side, 1, 0, 1, 1)

        self.y1Side = QLineEdit(self.groupBox_3)
        self.y1Side.setObjectName(u"y1Side")

        self.gridLayout_3.addWidget(self.y1Side, 1, 1, 1, 1)

        self.x2Side = QLineEdit(self.groupBox_3)
        self.x2Side.setObjectName(u"x2Side")

        self.gridLayout_3.addWidget(self.x2Side, 2, 0, 1, 1)

        self.y2Side = QLineEdit(self.groupBox_3)
        self.y2Side.setObjectName(u"y2Side")

        self.gridLayout_3.addWidget(self.y2Side, 2, 1, 1, 1)

        self.x3Side = QLineEdit(self.groupBox_3)
        self.x3Side.setObjectName(u"x3Side")

        self.gridLayout_3.addWidget(self.x3Side, 3, 0, 1, 1)

        self.y3Side = QLineEdit(self.groupBox_3)
        self.y3Side.setObjectName(u"y3Side")

        self.gridLayout_3.addWidget(self.y3Side, 3, 1, 1, 1)

        self.x4Side = QLineEdit(self.groupBox_3)
        self.x4Side.setObjectName(u"x4Side")

        self.gridLayout_3.addWidget(self.x4Side, 4, 0, 1, 1)

        self.y4Side = QLineEdit(self.groupBox_3)
        self.y4Side.setObjectName(u"y4Side")

        self.gridLayout_3.addWidget(self.y4Side, 4, 1, 1, 1)

        self.x5Side = QLineEdit(self.groupBox_3)
        self.x5Side.setObjectName(u"x5Side")

        self.gridLayout_3.addWidget(self.x5Side, 5, 0, 1, 1)

        self.y6Side = QLineEdit(self.groupBox_3)
        self.y6Side.setObjectName(u"y6Side")

        self.gridLayout_3.addWidget(self.y6Side, 5, 1, 1, 1)

        self.x6Side = QLineEdit(self.groupBox_3)
        self.x6Side.setObjectName(u"x6Side")

        self.gridLayout_3.addWidget(self.x6Side, 6, 0, 1, 1)

        self.y6Side_2 = QLineEdit(self.groupBox_3)
        self.y6Side_2.setObjectName(u"y6Side_2")

        self.gridLayout_3.addWidget(self.y6Side_2, 6, 1, 1, 1)

        self.x7Side = QLineEdit(self.groupBox_3)
        self.x7Side.setObjectName(u"x7Side")

        self.gridLayout_3.addWidget(self.x7Side, 7, 0, 1, 1)

        self.y7Side = QLineEdit(self.groupBox_3)
        self.y7Side.setObjectName(u"y7Side")

        self.gridLayout_3.addWidget(self.y7Side, 7, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_3)

        self.layoutWidget = QWidget(self.tab_dimensions)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 330, 81, 46))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.textLenght = QLineEdit(self.layoutWidget)
        self.textLenght.setObjectName(u"textLenght")

        self.verticalLayout.addWidget(self.textLenght)

        self.layoutWidget1 = QWidget(self.tab_dimensions)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(440, 720, 121, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.textWidth = QLineEdit(self.layoutWidget1)
        self.textWidth.setObjectName(u"textWidth")

        self.horizontalLayout_5.addWidget(self.textWidth)

        self.tabWidget.addTab(self.tab_dimensions, "")
        self.tab_specifications = QWidget()
        self.tab_specifications.setObjectName(u"tab_specifications")
        self.layoutWidget2 = QWidget(self.tab_specifications)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(190, 110, 561, 481))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.textbox_year = QLineEdit(self.layoutWidget2)
        self.textbox_year.setObjectName(u"textbox_year")

        self.verticalLayout_4.addWidget(self.textbox_year)

        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)

        self.textbox_number = QLineEdit(self.layoutWidget2)
        self.textbox_number.setObjectName(u"textbox_number")

        self.verticalLayout_4.addWidget(self.textbox_number)

        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_4.addWidget(self.label_12)

        self.textbox_model = QLineEdit(self.layoutWidget2)
        self.textbox_model.setObjectName(u"textbox_model")

        self.verticalLayout_4.addWidget(self.textbox_model)

        self.label_17 = QLabel(self.layoutWidget2)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_4.addWidget(self.label_17)

        self.textbox_oem = QLineEdit(self.layoutWidget2)
        self.textbox_oem.setObjectName(u"textbox_oem")

        self.verticalLayout_4.addWidget(self.textbox_oem)

        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_4.addWidget(self.label_13)

        self.textbox_vin = QLineEdit(self.layoutWidget2)
        self.textbox_vin.setObjectName(u"textbox_vin")

        self.verticalLayout_4.addWidget(self.textbox_vin)

        self.label_14 = QLabel(self.layoutWidget2)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_4.addWidget(self.label_14)

        self.textbox_software = QLineEdit(self.layoutWidget2)
        self.textbox_software.setObjectName(u"textbox_software")

        self.verticalLayout_4.addWidget(self.textbox_software)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.layoutWidget2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radio_car = QRadioButton(self.groupBox_4)
        self.radio_car.setObjectName(u"radio_car")
        self.radio_car.setChecked(True)

        self.verticalLayout_2.addWidget(self.radio_car)

        self.radio_van = QRadioButton(self.groupBox_4)
        self.radio_van.setObjectName(u"radio_van")

        self.verticalLayout_2.addWidget(self.radio_van)

        self.radio_truck = QRadioButton(self.groupBox_4)
        self.radio_truck.setObjectName(u"radio_truck")

        self.verticalLayout_2.addWidget(self.radio_truck)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 3, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 2, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 4, 1, 1)

        self.tabWidget.addTab(self.tab_specifications, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Test Type", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Test Name", None))
        self.button_add_new_test.setText(QCoreApplication.translate("MainWindow", u"Add New Test", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tests), QCoreApplication.translate("MainWindow", u"Add Tests", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Back Profile", None))
        self.x3Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y5Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y3Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x7Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y2Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y6Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x5Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x6Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y4Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y1Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x4Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x2Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x1Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y7Back.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y :", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Front Profile", None))
        self.x3Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"y :", None))
        self.y3Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y2Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y6Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x4Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y7Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y4Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y5Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y1Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x5Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x6Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x7Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x2Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x1Front.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x :", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Side Profile", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"x :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"y :", None))
        self.x1Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y1Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x2Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y2Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x3Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y3Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x4Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y4Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x5Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y6Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x6Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y6Side_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x7Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y7Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Lenght:", None))
        self.textLenght.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.textWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dimensions), QCoreApplication.translate("MainWindow", u"Dimensions", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ENCAP Number", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Model Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"OEM", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"VIN", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Software Version", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Veichle Type", None))
        self.radio_car.setText(QCoreApplication.translate("MainWindow", u"Car", None))
        self.radio_van.setText(QCoreApplication.translate("MainWindow", u"Van", None))
        self.radio_truck.setText(QCoreApplication.translate("MainWindow", u"Truck", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Folders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_specifications), QCoreApplication.translate("MainWindow", u"Specifications", None))
    # retranslateUi

