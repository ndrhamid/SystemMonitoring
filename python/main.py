import sys
import os
import platform
import datetime
import psutil

import PySide2extn
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QPropertyAnimation
from PySide2.QtWidgets import QMainWindow, QSizeGrip, QGraphicsDropShadowEffect, QPushButton, QTableWidgetItem
from qt_material import *
from multiprocessing import cpu_count
# IMPORT GUI FILE
from ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowTitle("SystemMonitoring")
        QSizeGrip(self.ui.size_grip)
        self.manage_button()
        self.cpu_ram()
        self.system_info()
        self.processes()
        # self.battery_information()
        self.set_style()
        self.show()
    def set_style(self):
        apply_stylesheet(app, theme="dark_cyan.xml")
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

    def manage_button(self):
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        self.ui.cpu_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))
        self.ui.battery_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
        self.ui.system_info_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_information))
        self.ui.activity_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activities))
        self.ui.storage_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
        self.ui.sensor_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
        self.ui.network_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.network))

        self.ui.menu_btn.clicked.connect(lambda: self.ui.left_menu_count_frame)
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            # self.ui.restore_window_button.setIcon(QtGui.QIcon(u""))
        else:
            self.showMaximized()
            # self.ui.restore_window_button.setIcon(QtGui.QIcon(u""))

    def side_left_menu(self):
        width = self.ui.left_menu_count_frame.width()
        if width == 40:
            newWidth = 200
        else:
            newWidth = 40
        self.animation = QPropertyAnimation(self.ui.left_menu_count_frame, b"minimumwidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InQutQuart)
        self.animation.start()
    def menu_button_style(self):
        for button in self.ui.menu_frame.findChildren(QPushButton):
            button.clicked.connect(self.apply_button_style)

    def apply_button_style(self):
        for button in self.ui.menu_frame.findChildren(QPushButton):
            if button.objectName() != self.sender().objectName():
                button.setStyleSheet("border-bottom: none;")
        self.sender().setStyleSheet("border-bottom: 2px solid")
        return

    def system_info(self):
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.ui.system_date.setText(str(time))
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.system_time.setText(str(date))

        self.ui.system_machine.setText(platform.machine())
        self.ui.system_version.setText(platform.version())
        self.ui.system_platform.setText(platform.platform())
        self.ui.system_system.setText(platform.system())
        self.ui.system_processor.setText(platform.processor())


    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" %(hh, mm, ss)

    def battery_information(self):
        batt = psutil.sensors_battery()

        if not hasattr(psutil, "sensors_battery"):
            self.ui.battery_status.setText("Platform not supported")
        if batt is None:
            self.ui.battery_status.setText("No battery installed")
        if batt.power_plugged:
            self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
            self.ui.battery_time_left.setText("N/A")
            if batt.percent < 100:
                self.ui.battery_status.setText("Charging")
            else:
                self.ui.battery_status.setText("Fully Charged")
            self.ui.battery_plugged.setText("Yes")
        else:
            self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
            self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))

            if batt.percent < 100:
                self.ui.battery_status.setText("Discharging")
            else:
                self.ui.battery_status.setText("Fully Charged")
            self.ui.battery_plugged.setText("No")

        self.ui.battery_usage.rpb_setMaximum(100)
        self.ui.battery_usage.rpb_setValue(batt.percent)
        self.ui.battery_usage.rpb_setBarStyle("Hybrid2")
        self.ui.battery_usage.rpb_setLineColor((255, 30, 99))
        self.ui.battery_usage.rpb_setPieColor((45, 74, 83))
        self.ui.battery_usage.rpb_setTextColor((255, 255, 255))
        self.ui.battery_usage.rpb_setInitialPos("west")
        self.ui.battery_usage.rpb_setTextFormat("Percentage")
        self.ui.battery_usage.rpb_setLineWidth(15)
        self.ui.battery_usage.rpb_setPathWidth(15)
        self.ui.battery_usage.rpb_setLineCap("RoundCap")

    def cpu_ram(self):
        totalRam = 1.0
        totalRam = psutil.virtual_memory()[0] * totalRam
        totalRam = totalRam / (1024 * 1024 * 1024)
        self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + " GB"))

        availRam = 1.0
        availRam = psutil.virtual_memory()[1] * availRam
        availRam = availRam / (1024 * 1024 * 1024)
        self.ui.available_ram.setText(str("{:.4f}".format(availRam) + " GB"))

        ramUsed = 1.0
        ramUsed = psutil.virtual_memory()[3] * ramUsed
        ramUsed = ramUsed / (1024 * 1024 * 1024)
        self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + " GB"))

        ramFree = 1.0
        ramFree = psutil.virtual_memory()[4] * ramFree
        ramFree = ramFree / (1024 * 1024 * 1024)
        self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + " GB"))

        ramUsages = str(psutil.virtual_memory()[2]) + "%"
        self.ui.ram_usage_2.setText(str("{:.4f}".format(totalRam) + " GB"))

        core = cpu_count()
        self.ui.cpu_count.setText(str(core))

        cpuPer = psutil.cpu_percent()
        self.ui.cpu_per.setText(str(cpuPer) + " %")

        cpuMainCore = psutil.cpu_count(logical=False)
        self.ui.cpu_main_core.setText(str(cpuMainCore))

        self.ui.cpu_percentage.rpb_setMaximum(100)
        self.ui.cpu_percentage.rpb_setValue(cpuPer)
        self.ui.cpu_percentage.rpb_setBarStyle("Hybrid2")
        self.ui.cpu_percentage.rpb_setLineColor((255, 30, 99))
        self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
        self.ui.cpu_percentage.rpb_setTextColor((255, 255, 255))
        self.ui.cpu_percentage.rpb_setInitialPos("West")
        self.ui.cpu_percentage.rpb_setTextFormat("Percentage")
        self.ui.cpu_percentage.rpb_setTextFont("Arial")
        self.ui.cpu_percentage.rpb_setLineWidth(15)
        self.ui.cpu_percentage.rpb_setPathWidth(15)
        self.ui.cpu_percentage.rpb_setLineCap("RoundCap")

        self.ui.ram_percentage.spb_setMinimum((0, 0, 0))
        self.ui.ram_percentage.spb_setMaximum((totalRam, totalRam, totalRam))
        self.ui.ram_percentage.spb_setValue((availRam, ramUsed, ramFree))
        self.ui.ram_percentage.spb_lineColor(((6, 233, 38), (6, 201, 233), (233, 6, 201)))
        self.ui.ram_percentage.spb_setInitialPos(("West", "West", "West"))
        self.ui.ram_percentage.spb_lineWidth(15)
        self.ui.ram_percentage.spb_lineStyle(("SolidLine", "SolidLine", "SolidLine"))
        self.ui.ram_percentage.spb_lineCap(("RoundCap", "RoundCap", "RoundCap"))
        self.ui.ram_percentage.spb_setPathHidden(True)

    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtablewidgetitem.setText(text)
    def processes(self):
        for x in psutil.pids():
            rowPosition = self.ui.activities_table_widget.rowCount()
            self.ui.activities_table_widget.insertRow(rowPosition)

            try:
                process = psutil.Process(x)

                self.create_table_widget(rowPosition, 0, str(process.pid), "activities_table_widget")
                self.create_table_widget(rowPosition, 1, process.name(), "activities_table_widget")
                self.create_table_widget(rowPosition, 2, process.status(), "activities_table_widget")
                self.create_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")), "activities_table_widget")

                suspend_btn = QPushButton(self.ui.activities_table_widget)
                suspend_btn.setText("Suspend")
                self.ui.suspend_btn.setStyleSheet("color: brown")
                suspend_btn.setStyleSheet("color: brown")
                self.ui.activities_table_widget.setCellWidget(rowPosition, 4, suspend_btn)

                resume_btn = QPushButton(self.ui.activities_table_widget)
                resume_btn.setText("Resume")
                resume_btn.setStyleSheet("color: green")
                self.ui.resume_btn.setStyleSheet("color: green")
                self.ui.activities_table_widget.setCellWidget(rowPosition, 5, resume_btn)

                terminate_btn = QPushButton(self.ui.activities_table_widget)
                terminate_btn.setText("Terminate")
                terminate_btn.setStyleSheet("color: orange")
                self.ui.terminate_btn.setStyleSheet("color: orange")
                self.ui.activities_table_widget.setCellWidget(rowPosition, 6, terminate_btn)

                kill_btn = QPushButton(self.ui.activities_table_widget)
                kill_btn.setText("Kill")
                kill_btn.setStyleSheet("color: red")
                self.ui.kill_btn.setStyleSheet("color: red")
                self.ui.activities_table_widget.setCellWidget(rowPosition, 7, kill_btn)

            except Exception as e:
                print(e)

        self.ui.activity_search.textChanged.connect(self.findName())

    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.activities_table_widget.rowCount()):
            item = self.ui.activities_table_widget.item(row, 1)
            self.ui.activities_table_widget.setRowHidden(row, name not in item.text().lower())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
