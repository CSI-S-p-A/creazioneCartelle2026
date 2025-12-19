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
        self.layoutWidget = QWidget(self.tab_tests)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 30, 871, 61))
        self.gridLayout_5 = QGridLayout(self.layoutWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 0, 1, 1, 1)

        self.combo_test_type = QComboBox(self.layoutWidget)
        self.combo_test_type.setObjectName(u"combo_test_type")

        self.gridLayout_5.addWidget(self.combo_test_type, 1, 0, 1, 1)

        self.combo_test_name = QComboBox(self.layoutWidget)
        self.combo_test_name.setObjectName(u"combo_test_name")

        self.gridLayout_5.addWidget(self.combo_test_name, 1, 1, 1, 1)

        self.button_add_new_test = QPushButton(self.layoutWidget)
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

        self.y5Side = QLineEdit(self.groupBox_3)
        self.y5Side.setObjectName(u"y5Side")

        self.gridLayout_3.addWidget(self.y5Side, 5, 1, 1, 1)

        self.x6Side = QLineEdit(self.groupBox_3)
        self.x6Side.setObjectName(u"x6Side")

        self.gridLayout_3.addWidget(self.x6Side, 6, 0, 1, 1)

        self.y6Side = QLineEdit(self.groupBox_3)
        self.y6Side.setObjectName(u"y6Side")

        self.gridLayout_3.addWidget(self.y6Side, 6, 1, 1, 1)

        self.x7Side = QLineEdit(self.groupBox_3)
        self.x7Side.setObjectName(u"x7Side")

        self.gridLayout_3.addWidget(self.x7Side, 7, 0, 1, 1)

        self.y7Side = QLineEdit(self.groupBox_3)
        self.y7Side.setObjectName(u"y7Side")

        self.gridLayout_3.addWidget(self.y7Side, 7, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_3)

        self.layoutWidget1 = QWidget(self.tab_dimensions)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 330, 81, 46))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.textLenght = QLineEdit(self.layoutWidget1)
        self.textLenght.setObjectName(u"textLenght")

        self.verticalLayout.addWidget(self.textLenght)

        self.layoutWidget2 = QWidget(self.tab_dimensions)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(440, 720, 121, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.textWidth = QLineEdit(self.layoutWidget2)
        self.textWidth.setObjectName(u"textWidth")

        self.horizontalLayout_5.addWidget(self.textWidth)

        self.tabWidget.addTab(self.tab_dimensions, "")
        self.tab_specifications = QWidget()
        self.tab_specifications.setObjectName(u"tab_specifications")
        self.verticalLayout_3 = QVBoxLayout(self.tab_specifications)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 72, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_10 = QLabel(self.tab_specifications)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)

        self.verticalLayout_4.addWidget(self.label_10)

        self.textbox_year = QLineEdit(self.tab_specifications)
        self.textbox_year.setObjectName(u"textbox_year")
        self.textbox_year.setMinimumSize(QSize(250, 0))
        self.textbox_year.setFont(font)

        self.verticalLayout_4.addWidget(self.textbox_year)

        self.label_11 = QLabel(self.tab_specifications)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_4.addWidget(self.label_11)

        self.textbox_number = QLineEdit(self.tab_specifications)
        self.textbox_number.setObjectName(u"textbox_number")
        self.textbox_number.setMinimumSize(QSize(250, 0))
        self.textbox_number.setFont(font)

        self.verticalLayout_4.addWidget(self.textbox_number)

        self.label_12 = QLabel(self.tab_specifications)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout_4.addWidget(self.label_12)

        self.textbox_model = QLineEdit(self.tab_specifications)
        self.textbox_model.setObjectName(u"textbox_model")
        self.textbox_model.setMinimumSize(QSize(250, 0))
        self.textbox_model.setFont(font)

        self.verticalLayout_4.addWidget(self.textbox_model)

        self.label_17 = QLabel(self.tab_specifications)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.verticalLayout_4.addWidget(self.label_17)

        self.textbox_oem = QLineEdit(self.tab_specifications)
        self.textbox_oem.setObjectName(u"textbox_oem")
        self.textbox_oem.setMinimumSize(QSize(250, 0))
        self.textbox_oem.setFont(font)

        self.verticalLayout_4.addWidget(self.textbox_oem)

        self.label_13 = QLabel(self.tab_specifications)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout_4.addWidget(self.label_13)

        self.textbox_vin = QLineEdit(self.tab_specifications)
        self.textbox_vin.setObjectName(u"textbox_vin")
        self.textbox_vin.setMinimumSize(QSize(250, 0))
        self.textbox_vin.setFont(font)

        self.verticalLayout_4.addWidget(self.textbox_vin)

        self.label_14 = QLabel(self.tab_specifications)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_4.addWidget(self.label_14)

        self.textbox_software = QLineEdit(self.tab_specifications)
        self.textbox_software.setObjectName(u"textbox_software")
        self.textbox_software.setMinimumSize(QSize(250, 0))
        self.textbox_software.setFont(font)

        self.verticalLayout_4.addWidget(self.textbox_software, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.groupBox_4 = QGroupBox(self.tab_specifications)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(300, 250))
        self.groupBox_4.setMaximumSize(QSize(300, 250))
        self.groupBox_4.setFont(font)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(89, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radio_car = QRadioButton(self.groupBox_4)
        self.radio_car.setObjectName(u"radio_car")
        self.radio_car.setFont(font)
        self.radio_car.setChecked(True)

        self.verticalLayout_2.addWidget(self.radio_car)

        self.radio_van = QRadioButton(self.groupBox_4)
        self.radio_van.setObjectName(u"radio_van")
        self.radio_van.setFont(font)

        self.verticalLayout_2.addWidget(self.radio_van)

        self.radio_truck = QRadioButton(self.groupBox_4)
        self.radio_truck.setObjectName(u"radio_truck")
        self.radio_truck.setFont(font)

        self.verticalLayout_2.addWidget(self.radio_truck)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_7.addWidget(self.groupBox_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_2 = QSpacerItem(20, 73, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.button_create_folders = QPushButton(self.tab_specifications)
        self.button_create_folders.setObjectName(u"button_create_folders")
        self.button_create_folders.setMinimumSize(QSize(250, 50))
        self.button_create_folders.setMaximumSize(QSize(250, 50))
        font1 = QFont()
        font1.setPointSize(19)
        self.button_create_folders.setFont(font1)

        self.verticalLayout_3.addWidget(self.button_create_folders, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 72, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.tabWidget.addTab(self.tab_specifications, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.x1Front, self.x2Front)
        QWidget.setTabOrder(self.x2Front, self.x3Front)
        QWidget.setTabOrder(self.x3Front, self.x4Front)
        QWidget.setTabOrder(self.x4Front, self.x5Front)
        QWidget.setTabOrder(self.x5Front, self.x6Front)
        QWidget.setTabOrder(self.x6Front, self.x7Front)
        QWidget.setTabOrder(self.x7Front, self.y1Front)
        QWidget.setTabOrder(self.y1Front, self.y2Front)
        QWidget.setTabOrder(self.y2Front, self.y3Front)
        QWidget.setTabOrder(self.y3Front, self.y4Front)
        QWidget.setTabOrder(self.y4Front, self.y5Front)
        QWidget.setTabOrder(self.y5Front, self.y6Front)
        QWidget.setTabOrder(self.y6Front, self.y7Front)
        QWidget.setTabOrder(self.y7Front, self.x1Side)
        QWidget.setTabOrder(self.x1Side, self.y1Side)
        QWidget.setTabOrder(self.y1Side, self.x2Side)
        QWidget.setTabOrder(self.x2Side, self.y2Side)
        QWidget.setTabOrder(self.y2Side, self.x3Side)
        QWidget.setTabOrder(self.x3Side, self.y3Side)
        QWidget.setTabOrder(self.y3Side, self.x4Side)
        QWidget.setTabOrder(self.x4Side, self.y4Side)
        QWidget.setTabOrder(self.y4Side, self.x5Side)
        QWidget.setTabOrder(self.x5Side, self.y5Side)
        QWidget.setTabOrder(self.y5Side, self.x6Side)
        QWidget.setTabOrder(self.x6Side, self.y6Side)
        QWidget.setTabOrder(self.y6Side, self.x7Side)
        QWidget.setTabOrder(self.x7Side, self.y7Side)
        QWidget.setTabOrder(self.y7Side, self.x1Back)
        QWidget.setTabOrder(self.x1Back, self.x2Back)
        QWidget.setTabOrder(self.x2Back, self.x3Back)
        QWidget.setTabOrder(self.x3Back, self.x4Back)
        QWidget.setTabOrder(self.x4Back, self.x5Back)
        QWidget.setTabOrder(self.x5Back, self.x6Back)
        QWidget.setTabOrder(self.x6Back, self.x7Back)
        QWidget.setTabOrder(self.x7Back, self.y1Back)
        QWidget.setTabOrder(self.y1Back, self.y2Back)
        QWidget.setTabOrder(self.y2Back, self.y3Back)
        QWidget.setTabOrder(self.y3Back, self.y4Back)
        QWidget.setTabOrder(self.y4Back, self.y5Back)
        QWidget.setTabOrder(self.y5Back, self.y6Back)
        QWidget.setTabOrder(self.y6Back, self.y7Back)
        QWidget.setTabOrder(self.y7Back, self.textLenght)
        QWidget.setTabOrder(self.textLenght, self.textWidth)
        QWidget.setTabOrder(self.textWidth, self.combo_test_name)
        QWidget.setTabOrder(self.combo_test_name, self.textbox_year)
        QWidget.setTabOrder(self.textbox_year, self.textbox_number)
        QWidget.setTabOrder(self.textbox_number, self.textbox_model)
        QWidget.setTabOrder(self.textbox_model, self.textbox_oem)
        QWidget.setTabOrder(self.textbox_oem, self.textbox_vin)
        QWidget.setTabOrder(self.textbox_vin, self.textbox_software)
        QWidget.setTabOrder(self.textbox_software, self.radio_car)
        QWidget.setTabOrder(self.radio_car, self.radio_van)
        QWidget.setTabOrder(self.radio_van, self.radio_truck)
        QWidget.setTabOrder(self.radio_truck, self.button_create_folders)
        QWidget.setTabOrder(self.button_create_folders, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.combo_test_type)
        QWidget.setTabOrder(self.combo_test_type, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.button_add_new_test)

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
        self.y5Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x6Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y6Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.x7Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.y7Side.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Lenght:", None))
        self.textLenght.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.textWidth.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_dimensions), QCoreApplication.translate("MainWindow", u"Dimensions", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.textbox_year.setPlaceholderText(QCoreApplication.translate("MainWindow", u"202X", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ENCAP Number", None))
        self.textbox_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"11XX", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Model Name", None))
        self.textbox_model.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Toyota Yaris", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"OEM", None))
        self.textbox_oem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TOY", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"VIN", None))
        self.textbox_vin.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1G1BW4EF1K50768801", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Software Version", None))
        self.textbox_software.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.9.12", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Veichle Type", None))
        self.radio_car.setText(QCoreApplication.translate("MainWindow", u"Car", None))
        self.radio_van.setText(QCoreApplication.translate("MainWindow", u"Van", None))
        self.radio_truck.setText(QCoreApplication.translate("MainWindow", u"Truck", None))
        self.button_create_folders.setText(QCoreApplication.translate("MainWindow", u"Create Folders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_specifications), QCoreApplication.translate("MainWindow", u"Specifications", None))
    # retranslateUi

