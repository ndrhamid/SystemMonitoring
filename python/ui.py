# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainZoFdiv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 617)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(21,76,121);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.header_left_frame)
        self.menu_btn.setObjectName(u"menu_btn")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menu_btn.setFont(font)
        self.menu_btn.setStyleSheet(u"color: rgb(73, 209, 243);")
        icon = QIcon()
        icon.addFile(u":/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.menu_btn, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left_frame)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setPixmap(QPixmap(u":/systemTask.png"))

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:rgb(255,255,255);\n"
"")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/window-minimize-solid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(40, 46))

        self.horizontalLayout_2.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_right_frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/window-restore-solid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(26, 23))

        self.horizontalLayout_2.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/xmark-solid.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setStyleSheet(u"color:rgb(255,255,255);\n"
"")
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_count_frame = QFrame(self.main_body_frame)
        self.left_menu_count_frame.setObjectName(u"left_menu_count_frame")
        self.left_menu_count_frame.setMinimumSize(QSize(60, 0))
        self.left_menu_count_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_count_frame.setStyleSheet(u"background-color: rgb(21,76,121);")
        self.left_menu_count_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_count_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_count_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_count_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(250, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cpu_page_btn = QPushButton(self.menu_frame)
        self.cpu_page_btn.setObjectName(u"cpu_page_btn")
        icon4 = QIcon()
        icon4.addFile(u":/Cpu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cpu_page_btn.setIcon(icon4)
        self.cpu_page_btn.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.cpu_page_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.network_page_btn = QPushButton(self.menu_frame)
        self.network_page_btn.setObjectName(u"network_page_btn")
        icon5 = QIcon()
        icon5.addFile(u":/network.png", QSize(), QIcon.Normal, QIcon.Off)
        self.network_page_btn.setIcon(icon5)
        self.network_page_btn.setIconSize(QSize(35, 35))

        self.gridLayout.addWidget(self.network_page_btn, 6, 0, 1, 1, Qt.AlignLeft)

        self.battery_page_btn = QPushButton(self.menu_frame)
        self.battery_page_btn.setObjectName(u"battery_page_btn")
        icon6 = QIcon()
        icon6.addFile(u":/battery.png", QSize(), QIcon.Normal, QIcon.Off)
        self.battery_page_btn.setIcon(icon6)
        self.battery_page_btn.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.battery_page_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.system_info_page_btn = QPushButton(self.menu_frame)
        self.system_info_page_btn.setObjectName(u"system_info_page_btn")
        icon7 = QIcon()
        icon7.addFile(u":/monitor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.system_info_page_btn.setIcon(icon7)
        self.system_info_page_btn.setIconSize(QSize(35, 35))

        self.gridLayout.addWidget(self.system_info_page_btn, 2, 0, 1, 1, Qt.AlignLeft)

        self.sensor_page_btn = QPushButton(self.menu_frame)
        self.sensor_page_btn.setObjectName(u"sensor_page_btn")
        icon8 = QIcon()
        icon8.addFile(u":/sensor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sensor_page_btn.setIcon(icon8)
        self.sensor_page_btn.setIconSize(QSize(35, 35))

        self.gridLayout.addWidget(self.sensor_page_btn, 5, 0, 1, 1, Qt.AlignLeft)

        self.storage_page_btn = QPushButton(self.menu_frame)
        self.storage_page_btn.setObjectName(u"storage_page_btn")
        icon9 = QIcon()
        icon9.addFile(u":/storage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_page_btn.setIcon(icon9)
        self.storage_page_btn.setIconSize(QSize(35, 35))

        self.gridLayout.addWidget(self.storage_page_btn, 4, 0, 1, 1, Qt.AlignLeft)

        self.activity_page_btn = QPushButton(self.menu_frame)
        self.activity_page_btn.setObjectName(u"activity_page_btn")
        icon10 = QIcon()
        icon10.addFile(u":/systemInformation.png", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_page_btn.setIcon(icon10)
        self.activity_page_btn.setIconSize(QSize(35, 35))

        self.gridLayout.addWidget(self.activity_page_btn, 3, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1, Qt.AlignLeft)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1, Qt.AlignLeft)

        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMargin(5)

        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_count_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        self.main_body_contents.setStyleSheet(u"background-color: rgb(32, 40, 40)")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu_and_memory = QWidget()
        self.cpu_and_memory.setObjectName(u"cpu_and_memory")
        self.verticalLayout_3 = QVBoxLayout(self.cpu_and_memory)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cpu_info_frame = QFrame(self.cpu_and_memory)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cpu_info_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_12 = QLabel(self.cpu_info_frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")

        self.gridLayout_2.addWidget(self.cpu_main_core, 3, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_13 = QLabel(self.cpu_info_frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_11 = QLabel(self.cpu_info_frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")

        self.gridLayout_2.addWidget(self.cpu_count, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")

        self.gridLayout_2.addWidget(self.cpu_per, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.cpu_percentage = roundProgressBar(self.cpu_info_frame)
        self.cpu_percentage.setObjectName(u"cpu_percentage")
        self.cpu_percentage.setMinimumSize(QSize(150, 150))
        self.cpu_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_2.addWidget(self.cpu_percentage, 2, 2, 2, 1)


        self.verticalLayout_3.addWidget(self.cpu_info_frame)

        self.ram_info_frame = QFrame(self.cpu_and_memory)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        self.ram_info_frame.setMinimumSize(QSize(150, 150))
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ram_info_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_21 = QLabel(self.ram_info_frame)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.free_ram = QLabel(self.ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")

        self.gridLayout_3.addWidget(self.free_ram, 3, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_19 = QLabel(self.ram_info_frame)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")

        self.gridLayout_3.addWidget(self.total_ram, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_18 = QLabel(self.ram_info_frame)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.ram_usage_2 = QLabel(self.ram_info_frame)
        self.ram_usage_2.setObjectName(u"ram_usage_2")

        self.gridLayout_3.addWidget(self.ram_usage_2, 4, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_17 = QLabel(self.ram_info_frame)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.available_ram = QLabel(self.ram_info_frame)
        self.available_ram.setObjectName(u"available_ram")

        self.gridLayout_3.addWidget(self.available_ram, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")

        self.gridLayout_3.addWidget(self.used_ram, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_20 = QLabel(self.ram_info_frame)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.ram_percentage = spiralProgressBar(self.ram_info_frame)
        self.ram_percentage.setObjectName(u"ram_percentage")
        self.ram_percentage.setMinimumSize(QSize(150, 150))
        self.ram_percentage.setMaximumSize(QSize(150, 150))

        self.gridLayout_3.addWidget(self.ram_percentage, 1, 2, 3, 1)


        self.verticalLayout_3.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu_and_memory)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_4 = QVBoxLayout(self.battery)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.battery_info_frame = QFrame(self.battery)
        self.battery_info_frame.setObjectName(u"battery_info_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.battery_info_frame.sizePolicy().hasHeightForWidth())
        self.battery_info_frame.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(10)
        self.battery_info_frame.setFont(font3)
        self.battery_info_frame.setFrameShape(QFrame.StyledPanel)
        self.battery_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.battery_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_30 = QLabel(self.battery_info_frame)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_4.addWidget(self.label_30, 4, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.battery_status = QLabel(self.battery_info_frame)
        self.battery_status.setObjectName(u"battery_status")

        self.gridLayout_4.addWidget(self.battery_status, 1, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.battery_plugged = QLabel(self.battery_info_frame)
        self.battery_plugged.setObjectName(u"battery_plugged")

        self.gridLayout_4.addWidget(self.battery_plugged, 4, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_28 = QLabel(self.battery_info_frame)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_4.addWidget(self.label_28, 2, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.battery_charge = QLabel(self.battery_info_frame)
        self.battery_charge.setObjectName(u"battery_charge")

        self.gridLayout_4.addWidget(self.battery_charge, 2, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.battery_time_left = QLabel(self.battery_info_frame)
        self.battery_time_left.setObjectName(u"battery_time_left")

        self.gridLayout_4.addWidget(self.battery_time_left, 3, 1, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_35 = QLabel(self.battery_info_frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.gridLayout_4.addWidget(self.label_35, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.label_22 = QLabel(self.battery_info_frame)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_29 = QLabel(self.battery_info_frame)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_4.addWidget(self.label_29, 3, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.battery_usage = roundProgressBar(self.battery_info_frame)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMinimumSize(QSize(150, 150))
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_4.addWidget(self.battery_usage, 2, 2, 3, 1)


        self.verticalLayout_4.addWidget(self.battery_info_frame)

        self.stackedWidget.addWidget(self.battery)
        self.system_information = QWidget()
        self.system_information.setObjectName(u"system_information")
        self.verticalLayout_5 = QVBoxLayout(self.system_information)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.system_info_frame = QFrame(self.system_information)
        self.system_info_frame.setObjectName(u"system_info_frame")
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        self.system_info_frame.setFont(font4)
        self.system_info_frame.setFrameShape(QFrame.StyledPanel)
        self.system_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.system_info_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_39 = QLabel(self.system_info_frame)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font4)

        self.gridLayout_5.addWidget(self.label_39, 2, 0, 1, 1)

        self.label_37 = QLabel(self.system_info_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.gridLayout_5.addWidget(self.label_37, 0, 0, 1, 1)

        self.system_platform = QLabel(self.system_info_frame)
        self.system_platform.setObjectName(u"system_platform")

        self.gridLayout_5.addWidget(self.system_platform, 2, 1, 1, 1)

        self.label_46 = QLabel(self.system_info_frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font4)

        self.gridLayout_5.addWidget(self.label_46, 3, 2, 1, 1)

        self.system_version = QLabel(self.system_info_frame)
        self.system_version.setObjectName(u"system_version")

        self.gridLayout_5.addWidget(self.system_version, 3, 1, 1, 1)

        self.label_47 = QLabel(self.system_info_frame)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font4)

        self.gridLayout_5.addWidget(self.label_47, 4, 2, 1, 1)

        self.label_41 = QLabel(self.system_info_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font4)

        self.gridLayout_5.addWidget(self.label_41, 4, 0, 1, 1)

        self.system_system = QLabel(self.system_info_frame)
        self.system_system.setObjectName(u"system_system")
        self.system_system.setFont(font4)

        self.gridLayout_5.addWidget(self.system_system, 1, 0, 1, 1)

        self.label_40 = QLabel(self.system_info_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font4)

        self.gridLayout_5.addWidget(self.label_40, 3, 0, 1, 1)

        self.system_date = QLabel(self.system_info_frame)
        self.system_date.setObjectName(u"system_date")

        self.gridLayout_5.addWidget(self.system_date, 4, 1, 1, 1)

        self.label_45 = QLabel(self.system_info_frame)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font4)

        self.gridLayout_5.addWidget(self.label_45, 2, 2, 1, 1)

        self.system_processor = QLabel(self.system_info_frame)
        self.system_processor.setObjectName(u"system_processor")

        self.gridLayout_5.addWidget(self.system_processor, 2, 3, 1, 1)

        self.system_machine = QLabel(self.system_info_frame)
        self.system_machine.setObjectName(u"system_machine")

        self.gridLayout_5.addWidget(self.system_machine, 3, 3, 1, 1)

        self.system_time = QLabel(self.system_info_frame)
        self.system_time.setObjectName(u"system_time")

        self.gridLayout_5.addWidget(self.system_time, 4, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.system_info_frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.system_information)
        self.activities = QWidget()
        self.activities.setObjectName(u"activities")
        self.verticalLayout_6 = QVBoxLayout(self.activities)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.activities_header_frame = QFrame(self.activities)
        self.activities_header_frame.setObjectName(u"activities_header_frame")
        self.activities_header_frame.setFrameShape(QFrame.StyledPanel)
        self.activities_header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.activities_header_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.header_lable_frame = QFrame(self.activities_header_frame)
        self.header_lable_frame.setObjectName(u"header_lable_frame")
        self.header_lable_frame.setFrameShape(QFrame.StyledPanel)
        self.header_lable_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.header_lable_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.header_lable_frame)
        self.label_51.setObjectName(u"label_51")
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_51.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_51, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.header_lable_frame)

        self.search_frame = QFrame(self.activities_header_frame)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.activity_search = QLineEdit(self.search_frame)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setStyleSheet(u"color: rgb(5, 115, 24);")

        self.horizontalLayout_11.addWidget(self.activity_search, 0, Qt.AlignRight|Qt.AlignTop)

        self.process_search_btn = QPushButton(self.search_frame)
        self.process_search_btn.setObjectName(u"process_search_btn")
        icon11 = QIcon()
        icon11.addFile(u":/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.process_search_btn.setIcon(icon11)
        self.process_search_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.process_search_btn, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_10.addWidget(self.search_frame)


        self.verticalLayout_6.addWidget(self.activities_header_frame)

        self.activities_center_frame = QFrame(self.activities)
        self.activities_center_frame.setObjectName(u"activities_center_frame")
        self.activities_center_frame.setFrameShape(QFrame.StyledPanel)
        self.activities_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.activities_center_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.activities_table_widget = QTableWidget(self.activities_center_frame)
        if (self.activities_table_widget.columnCount() < 8):
            self.activities_table_widget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.activities_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.activities_table_widget.setObjectName(u"activities_table_widget")

        self.horizontalLayout_14.addWidget(self.activities_table_widget)


        self.verticalLayout_6.addWidget(self.activities_center_frame)

        self.activities_footer_frame = QFrame(self.activities)
        self.activities_footer_frame.setObjectName(u"activities_footer_frame")
        self.activities_footer_frame.setStyleSheet(u"color: rgb(5, 115, 24);")
        self.activities_footer_frame.setFrameShape(QFrame.StyledPanel)
        self.activities_footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.activities_footer_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_3 = QPushButton(self.activities_footer_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_13.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.activities_footer_frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_13.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.activities_footer_frame)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_13.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.activities_footer_frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_13.addWidget(self.pushButton_6)


        self.verticalLayout_6.addWidget(self.activities_footer_frame)

        self.stackedWidget.addWidget(self.activities)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.horizontalLayout_15 = QHBoxLayout(self.storage)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.storage_frame = QFrame(self.storage)
        self.storage_frame.setObjectName(u"storage_frame")
        self.storage_frame.setFrameShape(QFrame.StyledPanel)
        self.storage_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.storage_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.storage_frame)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)

        self.verticalLayout_7.addWidget(self.label_52)

        self.storage_table_widget = QTableWidget(self.storage_frame)
        if (self.storage_table_widget.columnCount() < 8):
            self.storage_table_widget.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.storage_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.storage_table_widget.setObjectName(u"storage_table_widget")

        self.verticalLayout_7.addWidget(self.storage_table_widget)


        self.horizontalLayout_15.addWidget(self.storage_frame)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.verticalLayout_8 = QVBoxLayout(self.sensors)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.sensors_frame = QFrame(self.sensors)
        self.sensors_frame.setObjectName(u"sensors_frame")
        self.sensors_frame.setFrameShape(QFrame.StyledPanel)
        self.sensors_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.sensors_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_53 = QLabel(self.sensors_frame)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.verticalLayout_9.addWidget(self.label_53, 0, Qt.AlignLeft|Qt.AlignTop)

        self.sensor_table_Widget = QTableWidget(self.sensors_frame)
        if (self.sensor_table_Widget.columnCount() < 5):
            self.sensor_table_Widget.setColumnCount(5)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.sensor_table_Widget.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.sensor_table_Widget.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sensor_table_Widget.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sensor_table_Widget.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.sensor_table_Widget.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        self.sensor_table_Widget.setObjectName(u"sensor_table_Widget")

        self.verticalLayout_9.addWidget(self.sensor_table_Widget)


        self.verticalLayout_8.addWidget(self.sensors_frame)

        self.stackedWidget.addWidget(self.sensors)
        self.network = QWidget()
        self.network.setObjectName(u"network")
        self.network.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.network)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea = QScrollArea(self.network)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 205, 474))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stats_frame = QFrame(self.scrollAreaWidgetContents)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setFrameShape(QFrame.StyledPanel)
        self.stats_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.stats_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_54 = QLabel(self.stats_frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.verticalLayout_12.addWidget(self.label_54)

        self.tableWidget = QTableWidget(self.stats_frame)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.stats_frame)

        self.network_io_counter_frame = QFrame(self.scrollAreaWidgetContents)
        self.network_io_counter_frame.setObjectName(u"network_io_counter_frame")
        self.network_io_counter_frame.setFrameShape(QFrame.StyledPanel)
        self.network_io_counter_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.network_io_counter_frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_55 = QLabel(self.network_io_counter_frame)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.verticalLayout_13.addWidget(self.label_55)

        self.network_io_counter_table_widget = QTableWidget(self.network_io_counter_frame)
        if (self.network_io_counter_table_widget.columnCount() < 9):
            self.network_io_counter_table_widget.setColumnCount(9)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.network_io_counter_table_widget.setHorizontalHeaderItem(8, __qtablewidgetitem34)
        self.network_io_counter_table_widget.setObjectName(u"network_io_counter_table_widget")
        self.network_io_counter_table_widget.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.network_io_counter_table_widget)


        self.verticalLayout_10.addWidget(self.network_io_counter_frame)

        self.network_addresses_frame = QFrame(self.scrollAreaWidgetContents)
        self.network_addresses_frame.setObjectName(u"network_addresses_frame")
        self.network_addresses_frame.setFrameShape(QFrame.StyledPanel)
        self.network_addresses_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.network_addresses_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_56 = QLabel(self.network_addresses_frame)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.verticalLayout_14.addWidget(self.label_56)

        self.network_addresses_tablewidget = QTableWidget(self.network_addresses_frame)
        if (self.network_addresses_tablewidget.columnCount() < 6):
            self.network_addresses_tablewidget.setColumnCount(6)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.network_addresses_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.network_addresses_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.network_addresses_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.network_addresses_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.network_addresses_tablewidget.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.network_addresses_tablewidget.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        self.network_addresses_tablewidget.setObjectName(u"network_addresses_tablewidget")

        self.verticalLayout_14.addWidget(self.network_addresses_tablewidget)


        self.verticalLayout_10.addWidget(self.network_addresses_frame)

        self.network_connection_frame = QFrame(self.scrollAreaWidgetContents)
        self.network_connection_frame.setObjectName(u"network_connection_frame")
        self.network_connection_frame.setFrameShape(QFrame.StyledPanel)
        self.network_connection_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.network_connection_frame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_57 = QLabel(self.network_connection_frame)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)

        self.verticalLayout_15.addWidget(self.label_57)

        self.network_connection_frame_tablewidget = QTableWidget(self.network_connection_frame)
        if (self.network_connection_frame_tablewidget.columnCount() < 6):
            self.network_connection_frame_tablewidget.setColumnCount(6)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.network_connection_frame_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.network_connection_frame_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.network_connection_frame_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.network_connection_frame_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.network_connection_frame_tablewidget.setHorizontalHeaderItem(4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.network_connection_frame_tablewidget.setHorizontalHeaderItem(5, __qtablewidgetitem46)
        self.network_connection_frame_tablewidget.setObjectName(u"network_connection_frame_tablewidget")

        self.verticalLayout_15.addWidget(self.network_connection_frame_tablewidget)


        self.verticalLayout_10.addWidget(self.network_connection_frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.network)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 40, 40);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.footer_left_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.label_3, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.footer_right_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_7.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setSizeIncrement(QSize(10, 10))
        self.size_grip.setBaseSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"System Monitoring", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.cpu_page_btn.setText("")
        self.network_page_btn.setText("")
        self.battery_page_btn.setText("")
        self.system_info_page_btn.setText("")
        self.sensor_page_btn.setText("")
        self.storage_page_btn.setText("")
        self.activity_page_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cpu", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Networks", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU Per", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total Ram", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Free Ram", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.ram_usage_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Used Ram", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Battery Information", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"System Time", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"System Date", None))
        self.system_system.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Activities", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Processes", None))
        self.process_search_btn.setText("")
        ___qtablewidgetitem = self.activities_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PROCESS ID", None));
        ___qtablewidgetitem1 = self.activities_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"PROCESSES ID", None));
        ___qtablewidgetitem2 = self.activities_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PROCESS STATUS", None));
        ___qtablewidgetitem3 = self.activities_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"SUSPEND", None));
        ___qtablewidgetitem4 = self.activities_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"STARTED", None));
        ___qtablewidgetitem5 = self.activities_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"SUSPEND", None));
        ___qtablewidgetitem6 = self.activities_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"TERMINATE", None));
        ___qtablewidgetitem7 = self.activities_table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"KILL", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"SUSPEND", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"RESUME", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"TERMINATE", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"KILL", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Disk Partition", None))
        ___qtablewidgetitem8 = self.storage_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DEVICE", None));
        ___qtablewidgetitem9 = self.storage_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.storage_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem11 = self.storage_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem12 = self.storage_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"MAX FILE", None));
        ___qtablewidgetitem13 = self.storage_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"MAX PATH", None));
        ___qtablewidgetitem14 = self.storage_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"TOTAL STORAGE", None));
        ___qtablewidgetitem15 = self.storage_table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"FREE STORAGE", None));
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        ___qtablewidgetitem16 = self.sensor_table_Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem17 = self.sensor_table_Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"SENSOR", None));
        ___qtablewidgetitem18 = self.sensor_table_Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"CURRENT", None));
        ___qtablewidgetitem19 = self.sensor_table_Widget.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"HIGH", None));
        ___qtablewidgetitem20 = self.sensor_table_Widget.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"CRITICAL", None));
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"DUPLEX", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"SPEED", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Network IO Counter", None))
        ___qtablewidgetitem25 = self.network_io_counter_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"IO", None));
        ___qtablewidgetitem26 = self.network_io_counter_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"BYTES SENT", None));
        ___qtablewidgetitem27 = self.network_io_counter_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"BYTES RECEIVED", None));
        ___qtablewidgetitem28 = self.network_io_counter_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"PACKET SENT", None));
        ___qtablewidgetitem29 = self.network_io_counter_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"PACKET RECEIVED", None));
        ___qtablewidgetitem30 = self.network_io_counter_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ERR IN", None));
        ___qtablewidgetitem31 = self.network_io_counter_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"ERR OUT", None));
        ___qtablewidgetitem32 = self.network_io_counter_table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"DROP IN", None));
        ___qtablewidgetitem33 = self.network_io_counter_table_widget.horizontalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"DROP OUT", None));
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Network Addresses", None))
        ___qtablewidgetitem34 = self.network_addresses_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem35 = self.network_addresses_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"ADDRESSES", None));
        ___qtablewidgetitem36 = self.network_addresses_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"NETMASK", None));
        ___qtablewidgetitem37 = self.network_addresses_tablewidget.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"ROADCAST", None));
        ___qtablewidgetitem38 = self.network_addresses_tablewidget.horizontalHeaderItem(5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Network Connection", None))
        ___qtablewidgetitem39 = self.network_connection_frame_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem40 = self.network_connection_frame_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem41 = self.network_connection_frame_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"FAMILY", None));
        ___qtablewidgetitem42 = self.network_connection_frame_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem43 = self.network_connection_frame_tablewidget.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem44 = self.network_connection_frame_tablewidget.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Copyright System Co", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

