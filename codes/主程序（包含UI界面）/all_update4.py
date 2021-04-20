# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_update4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import time
from predict import predict_camera

import os
import filetype
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtWidgets import *
from copy import copy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 871)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_all = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_all.setGeometry(QtCore.QRect(20, 0, 1161, 831))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget_all.setFont(font)
        self.tabWidget_all.setMouseTracking(False)
        self.tabWidget_all.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_all.setIconSize(QtCore.QSize(34, 24))
        self.tabWidget_all.setObjectName("tabWidget_all")
        self.tab_realtime = QtWidgets.QWidget()
        self.tab_realtime.setObjectName("tab_realtime")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_realtime)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 60, 1051, 531))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.original_real_2 = QtWidgets.QGroupBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.original_real_2.setFont(font)
        self.original_real_2.setObjectName("original_real_2")
        self.horizontalLayout_3.addWidget(self.original_real_2)
        self.tested_real_2 = QtWidgets.QGroupBox(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tested_real_2.setFont(font)
        self.tested_real_2.setObjectName("tested_real_2")
        self.horizontalLayout_3.addWidget(self.tested_real_2)
        self.groupBox_news = QtWidgets.QGroupBox(self.tab_realtime)
        self.groupBox_news.setGeometry(QtCore.QRect(30, 690, 1051, 121))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_news.setFont(font)
        self.groupBox_news.setObjectName("groupBox_news")
        self.textEdit_real = QtWidgets.QTextEdit(self.groupBox_news)
        self.textEdit_real.setGeometry(QtCore.QRect(30, 40, 991, 61))
        self.textEdit_real.setObjectName("textEdit_real")
        self.label_8 = QtWidgets.QLabel(self.tab_realtime)
        self.label_8.setGeometry(QtCore.QRect(450, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox = QtWidgets.QGroupBox(self.tab_realtime)
        self.groupBox.setGeometry(QtCore.QRect(30, 600, 521, 81))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_4.setGeometry(QtCore.QRect(40, 30, 461, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Button_openCV_real_2 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Button_openCV_real_2.setFont(font)
        self.Button_openCV_real_2.setObjectName("Button_openCV_real_2")
        self.horizontalLayout_4.addWidget(self.Button_openCV_real_2)
        self.Button_YOLO_real_2 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.Button_YOLO_real_2.setFont(font)
        self.Button_YOLO_real_2.setObjectName("Button_YOLO_real_2")
        self.horizontalLayout_4.addWidget(self.Button_YOLO_real_2)
        self.Button_combin_real_2 = QtWidgets.QRadioButton(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Button_combin_real_2.setFont(font)
        self.Button_combin_real_2.setObjectName("Button_combin_real_2")
        self.horizontalLayout_4.addWidget(self.Button_combin_real_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_realtime)
        self.groupBox_3.setGeometry(QtCore.QRect(560, 600, 521, 81))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_end_real = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_end_real.setGeometry(QtCore.QRect(320, 30, 111, 41))
        self.pushButton_end_real.setObjectName("pushButton_end_real")
        self.pushButton_begin_real = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_begin_real.setGeometry(QtCore.QRect(130, 30, 111, 41))
        self.pushButton_begin_real.setObjectName("pushButton_begin_real")
        self.tabWidget_all.addTab(self.tab_realtime, "")
        self.tab_offline = QtWidgets.QWidget()
        self.tab_offline.setObjectName("tab_offline")
        self.groupBox_news_2 = QtWidgets.QGroupBox(self.tab_offline)
        self.groupBox_news_2.setGeometry(QtCore.QRect(40, 700, 1011, 111))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_news_2.setFont(font)
        self.groupBox_news_2.setObjectName("groupBox_news_2")
        self.textEdit_unreal = QtWidgets.QTextEdit(self.groupBox_news_2)
        self.textEdit_unreal.setGeometry(QtCore.QRect(50, 40, 921, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit_unreal.setFont(font)
        self.textEdit_unreal.setObjectName("textEdit_unreal")
        self.un_root_addr = QtWidgets.QLineEdit(self.tab_offline)
        self.un_root_addr.setGeometry(QtCore.QRect(170, 60, 591, 31))
        self.un_root_addr.setObjectName("un_root_addr")
        self.pushButton_confirm = QtWidgets.QPushButton(self.tab_offline)
        self.pushButton_confirm.setGeometry(QtCore.QRect(940, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.pushButton_skim = QtWidgets.QPushButton(self.tab_offline)
        self.pushButton_skim.setGeometry(QtCore.QRect(800, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_skim.setFont(font)
        self.pushButton_skim.setObjectName("pushButton_skim")
        self.progressBar = QtWidgets.QProgressBar(self.tab_offline)
        self.progressBar.setGeometry(QtCore.QRect(40, 600, 1011, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.tab_offline)
        self.label.setGeometry(QtCore.QRect(50, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.tab_offline)
        self.label_6.setGeometry(QtCore.QRect(410, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_offline)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 630, 1011, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 30, 751, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_openCV_unreal = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Button_openCV_unreal.setFont(font)
        self.Button_openCV_unreal.setObjectName("Button_openCV_unreal")
        self.horizontalLayout.addWidget(self.Button_openCV_unreal)
        self.Button_YOLO_unreal = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Button_YOLO_unreal.setFont(font)
        self.Button_YOLO_unreal.setObjectName("Button_YOLO_unreal")
        self.horizontalLayout.addWidget(self.Button_YOLO_unreal)
        self.Button_combin_unreal = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Button_combin_unreal.setFont(font)
        self.Button_combin_unreal.setObjectName("Button_combin_unreal")
        self.horizontalLayout.addWidget(self.Button_combin_unreal)
        self.checkBox_backstage = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_backstage.setFont(font)
        self.checkBox_backstage.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_backstage.setObjectName("checkBox_backstage")
        self.horizontalLayout.addWidget(self.checkBox_backstage)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_offline)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 100, 1011, 481))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.original_unreal = QtWidgets.QGroupBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.original_unreal.setFont(font)
        self.original_unreal.setObjectName("original_unreal")
        self.horizontalLayout_6.addWidget(self.original_unreal)
        self.test_unreal = QtWidgets.QGroupBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.test_unreal.setFont(font)
        self.test_unreal.setObjectName("test_unreal")
        self.horizontalLayout_6.addWidget(self.test_unreal)
        self.tabWidget_all.addTab(self.tab_offline, "")
        self.tab_record = QtWidgets.QWidget()
        self.tab_record.setObjectName("tab_record")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_record)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 60, 1051, 591))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_Realrecord_show = QtWidgets.QGroupBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_Realrecord_show.setFont(font)
        self.groupBox_Realrecord_show.setObjectName("groupBox_Realrecord_show")
        self.treeWidget_realrecord = QtWidgets.QTreeWidget(self.groupBox_Realrecord_show)
        self.treeWidget_realrecord.setGeometry(QtCore.QRect(30, 30, 481, 551))
        self.treeWidget_realrecord.setObjectName("treeWidget_realrecord")
        self.treeWidget_realrecord.headerItem().setText(0, "1")
        self.horizontalLayout_2.addWidget(self.groupBox_Realrecord_show)
        self.groupBox_Unrealrecord_show = QtWidgets.QGroupBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_Unrealrecord_show.setFont(font)
        self.groupBox_Unrealrecord_show.setObjectName("groupBox_Unrealrecord_show")
        self.sl = QtWidgets.QSlider(self.groupBox_Unrealrecord_show)
        self.sl.setGeometry(QtCore.QRect(30, 510, 431, 21))
        self.sl.setOrientation(QtCore.Qt.Horizontal)
        self.sl.setObjectName("sl")
        self.horizontalLayout_2.addWidget(self.groupBox_Unrealrecord_show)
        self.groupBox_news_3 = QtWidgets.QGroupBox(self.tab_record)
        self.groupBox_news_3.setGeometry(QtCore.QRect(30, 660, 1051, 151))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_news_3.setFont(font)
        self.groupBox_news_3.setObjectName("groupBox_news_3")
        self.tableWidget_detial = QtWidgets.QTableWidget(self.groupBox_news_3)
        self.tableWidget_detial.setGeometry(QtCore.QRect(30, 40, 981, 101))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_detial.setFont(font)
        self.tableWidget_detial.setObjectName("tableWidget_detial")
        self.tableWidget_detial.setColumnCount(0)
        self.tableWidget_detial.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.tab_record)
        self.label_5.setGeometry(QtCore.QRect(450, 0, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tabWidget_all.addTab(self.tab_record, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.show_pushButton_confirm = QtWidgets.QPushButton(self.tab)
        self.show_pushButton_confirm.setGeometry(QtCore.QRect(830, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.show_pushButton_confirm.setFont(font)
        self.show_pushButton_confirm.setObjectName("show_pushButton_confirm")
        self.show_root_addr = QtWidgets.QLineEdit(self.tab)
        self.show_root_addr.setGeometry(QtCore.QRect(120, 50, 591, 31))
        self.show_root_addr.setObjectName("show_root_addr")
        self.show_pushButton_skim = QtWidgets.QPushButton(self.tab)
        self.show_pushButton_skim.setGeometry(QtCore.QRect(730, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.show_pushButton_skim.setFont(font)
        self.show_pushButton_skim.setObjectName("show_pushButton_skim")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(480, 0, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 80, 1121, 741))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_show_original = QtWidgets.QGroupBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.groupBox_show_original.setFont(font)
        self.groupBox_show_original.setObjectName("groupBox_show_original")
        self.gridLayout.addWidget(self.groupBox_show_original, 0, 0, 1, 1)
        self.groupBox_show_opencv = QtWidgets.QGroupBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_show_opencv.setFont(font)
        self.groupBox_show_opencv.setObjectName("groupBox_show_opencv")
        self.gridLayout.addWidget(self.groupBox_show_opencv, 0, 1, 1, 1)
        self.groupBox_show_yolo = QtWidgets.QGroupBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_show_yolo.setFont(font)
        self.groupBox_show_yolo.setObjectName("groupBox_show_yolo")
        self.gridLayout.addWidget(self.groupBox_show_yolo, 1, 0, 1, 1)
        self.groupBox_show_combin = QtWidgets.QGroupBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_show_combin.setFont(font)
        self.groupBox_show_combin.setObjectName("groupBox_show_combin")
        self.gridLayout.addWidget(self.groupBox_show_combin, 1, 1, 1, 1)
        self.pushButton_real_show = QtWidgets.QPushButton(self.tab)
        self.pushButton_real_show.setGeometry(QtCore.QRect(1000, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.pushButton_real_show.setFont(font)
        self.pushButton_real_show.setObjectName("pushButton_real_show")
        self.tabWidget_all.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1186, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ########## 槽信号连接
        self.slot_init()
        # 翻页信号
        self.tabWidget_all.currentChanged.connect(self.refresh)

        #######tab1实时检测部分
        ##################Qlable初始化 用于显示图片
        self.label_show_original_real = QtWidgets.QLabel()
        self.label_show_tested_real = QtWidgets.QLabel()
        # 创建布局
        self.hboxL_original_real = QtWidgets.QHBoxLayout()
        self.hboxL_tested_real = QtWidgets.QHBoxLayout()
        # 初始化
        self.hboxL_original_real.addWidget(self.label_show_original_real)
        self.hboxL_tested_real.addWidget(self.label_show_tested_real)
        self.original_real_2.setLayout(self.hboxL_original_real)
        self.tested_real_2.setLayout(self.hboxL_tested_real)

        #############tab2离线检测部分
        # 按键浏览初始化
        self.renew_addr = ''
        self.not_empty = 0

        # Qlable初始化 用于显示图片
        self.label_show_original_unreal = QtWidgets.QLabel()
        self.label_show_tested_unreal = QtWidgets.QLabel()
        # 创建布局
        self.hboxL_original_unreal = QtWidgets.QHBoxLayout()
        self.hboxL_tested_unreal = QtWidgets.QHBoxLayout()
        # 初始化
        self.hboxL_original_unreal.addWidget(self.label_show_original_unreal)
        self.hboxL_tested_unreal.addWidget(self.label_show_tested_unreal)
        self.original_unreal.setLayout(self.hboxL_original_unreal)
        self.test_unreal.setLayout(self.hboxL_tested_unreal)

        # 进度条设置初始值
        self.progressBar.setProperty("value", 0)

        ########tab3检测记录
        # 树形图像根目录定义
        # 检测信息树形显示部分
        self.treeWidget_realrecord.setColumnCount(4)
        self.treeWidget_realrecord.setHeaderLabels(['id', '文件名', '检测结果统计', '文件地址'])

        self.treeWidget_realrecord.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.treeWidget_realrecord.customContextMenuRequested.connect(self.generaterecordMenu)  ####右键菜单

        self.root_real = QTreeWidgetItem(self.treeWidget_realrecord)
        self.root_real.setText(0, '实时检测录像')

        self.root_unreal_original = QTreeWidgetItem(self.treeWidget_realrecord)
        self.root_unreal_original.setText(0, '离线原始视频')

        self.root_unreal_tested = QTreeWidgetItem(self.treeWidget_realrecord)
        self.root_unreal_tested.setText(0, '离线检测视频')

        # 插入节点测试
        '''
        self.addNode(root_unreal_original, 'child1', '', 'E:/毕业设计/火灾数据集/barbeq.avi')
        self.addNode(root_unreal_tested, 'child2', 'fire：2 spark:3', 'E:/毕业设计/火灾数据集/barbeq.avi')
        self.addNode(root_real, 'child3', 'fire：4 spark:5', 'E:/毕业设计/火灾数据集/barbeq.avi')
        '''
        # 添加响应事件
        self.treeWidget_realrecord.clicked.connect(self.onClicked_real)
        self.treeWidget_realrecord.expandAll()

        # Qlable初始化 用于显示图片
        self.label_show_video = QtWidgets.QLabel()
        self.label_show_video.setScaledContents(False)
        # 创建布局
        self.hboxL_original_record = QtWidgets.QVBoxLayout()
        # 初始化
        self.hboxL_original_record.addWidget(self.label_show_video)
        self.groupBox_Unrealrecord_show.setLayout(self.hboxL_original_record)

        # slider用于控制进度
        self.sl = QtWidgets.QSlider(self.groupBox_Unrealrecord_show)
        self.sl.setGeometry(QtCore.QRect(10, 550, 431, 21))
        self.sl.setOrientation(QtCore.Qt.Horizontal)
        self.sl.setObjectName("sl")
        self.sl.setMinimum(0)
        self.sl.setMaximum(50)
        self.sl.setSingleStep(1)
        self.sl.setValue(0)
        self.sl.setTickPosition(QSlider.TicksBelow)

        # 初始化数据库与信息
        self.inquiry_database()

        # 详细信息初始化
        self.tableWidget_detial.setColumnCount(5)
        self.tableWidget_detial.setRowCount(5)  ####表格行数
        self.tableWidget_detial.setHorizontalHeaderLabels(['id', '文件名', '类别', '开始帧', '结束帧'])
        self.tableWidget_detial.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_detial.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单
        self.tableWidget_detial.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单

        ######tab4算法展示与tab2公用变量

        # Qlable初始化 用于显示图片
        self.label_show_original_show = QtWidgets.QLabel()
        self.label_show_opencv_show = QtWidgets.QLabel()
        self.label_show_yolo_show = QtWidgets.QLabel()
        self.label_show_combine_show = QtWidgets.QLabel()

        # 创建布局
        self.hboxL_original_show = QtWidgets.QHBoxLayout()
        self.hboxL_opencv_show = QtWidgets.QHBoxLayout()
        self.hboxL_yolo_show = QtWidgets.QHBoxLayout()
        self.hboxL_combine_show = QtWidgets.QHBoxLayout()
        # 初始化
        self.hboxL_original_show.addWidget(self.label_show_original_show)
        self.hboxL_opencv_show.addWidget(self.label_show_opencv_show)
        self.hboxL_yolo_show.addWidget(self.label_show_yolo_show)
        self.hboxL_combine_show.addWidget(self.label_show_combine_show)
        self.groupBox_show_original.setLayout(self.hboxL_original_show)
        self.groupBox_show_opencv.setLayout(self.hboxL_opencv_show)
        self.groupBox_show_yolo.setLayout(self.hboxL_yolo_show)
        self.groupBox_show_combin.setLayout(self.hboxL_combine_show)

        # 按键初始化
        self.show_pushButton_skim.clicked.connect(self.getfiles_show)
        self.show_pushButton_confirm.clicked.connect(self.confirm_files_show)
        self.pushButton_real_show.clicked.connect(self.open_camera_click_show)

        self.timer_show.timeout.connect(self.video_test_show)
        self.timer_show_real.timeout.connect(self.camera_test_show)

        self.retranslateUi(MainWindow)
        self.tabWidget_all.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.original_real_2.setTitle(_translate("MainWindow", "原图像"))
        self.tested_real_2.setTitle(_translate("MainWindow", "检测图像"))
        self.groupBox_news.setTitle(_translate("MainWindow", "详细信息"))
        self.textEdit_real.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">制作人：陈久阳</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">软件版本：python3.7.1 pytorch openCV QtDesigner</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "火焰实时检测"))
        self.groupBox.setTitle(_translate("MainWindow", "检测方式"))
        self.Button_openCV_real_2.setText(_translate("MainWindow", "OpenCV"))
        self.Button_YOLO_real_2.setText(_translate("MainWindow", "YOLO"))
        self.Button_combin_real_2.setText(_translate("MainWindow", "Combination"))
        self.groupBox_3.setTitle(_translate("MainWindow", "控制面板"))
        self.pushButton_end_real.setText(_translate("MainWindow", "结束"))
        self.pushButton_begin_real.setText(_translate("MainWindow", "开始"))
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_realtime), _translate("MainWindow", "实时检测"))
        self.groupBox_news_2.setTitle(_translate("MainWindow", "详细信息"))
        self.textEdit_unreal.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">制作人：陈久阳</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">软件版本：python3.7.1 pytorch openCV QtDesigner</span></p></body></html>"))
        self.pushButton_confirm.setText(_translate("MainWindow", "开始检测"))
        self.pushButton_skim.setText(_translate("MainWindow", "浏览"))
        self.label.setText(_translate("MainWindow", "文件地址"))
        self.label_6.setText(_translate("MainWindow", "火焰离线视频检测"))
        self.groupBox_2.setTitle(_translate("MainWindow", "检测方式与运行模式"))
        self.Button_openCV_unreal.setText(_translate("MainWindow", "OpenCV"))
        self.Button_YOLO_unreal.setText(_translate("MainWindow", "YOLO"))
        self.Button_combin_unreal.setText(_translate("MainWindow", "COMBINE"))
        self.checkBox_backstage.setText(_translate("MainWindow", "后台检测"))
        self.original_unreal.setTitle(_translate("MainWindow", "原视频"))
        self.test_unreal.setTitle(_translate("MainWindow", "检测视频"))
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_offline), _translate("MainWindow", "离线检测"))
        self.groupBox_Realrecord_show.setTitle(_translate("MainWindow", "检测记录"))
        self.groupBox_Unrealrecord_show.setTitle(_translate("MainWindow", "视频播放"))
        self.groupBox_news_3.setTitle(_translate("MainWindow", "详细信息"))
        self.label_5.setText(_translate("MainWindow", "检测记录查询"))
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab_record), _translate("MainWindow", "检测记录"))
        self.label_2.setText(_translate("MainWindow", "文件地址"))
        self.show_pushButton_confirm.setText(_translate("MainWindow", "开始检测"))
        self.show_pushButton_skim.setText(_translate("MainWindow", "浏览"))
        self.label_7.setText(_translate("MainWindow", "算法展示"))
        self.groupBox_show_original.setTitle(_translate("MainWindow", "原视频"))
        self.groupBox_show_opencv.setTitle(_translate("MainWindow", "OpenCV"))
        self.groupBox_show_yolo.setTitle(_translate("MainWindow", "YOLO"))
        self.groupBox_show_combin.setTitle(_translate("MainWindow", "combine"))
        self.pushButton_real_show.setText(_translate("MainWindow", "实时检测"))
        self.tabWidget_all.setTabText(self.tabWidget_all.indexOf(self.tab), _translate("MainWindow", "算法展示"))




######页面刷新
    def refresh(self):
        self.timer_camera.stop()   # 实时检测
        self.timer_video.stop()  # 离线检测
        self.timer_record.stop()  # 检测记录
        self.timer_show.stop()
        self.timer_show_real.stop()
        self.flag = [0, 0, 0, 0]  # 打火机火焰，森林火焰，烟雾，电火花
        self.begin_frame = [0, 0, 0, 0]
        self.type_counting = [0, 0, 0, 0]
        self.counting = 0
        try:
            if self.VWirte.isOpened():
                self.VWirte.release()
        except:
            pass

        if self.cap.isOpened():
            self.cap.release()

        self.cap = cv2.VideoCapture()

        index = self.tabWidget_all.currentIndex()
        if index == 2:
            self.label_show_video.setPixmap(QtGui.QPixmap(""))
            self.inquiry_database()

        elif index ==0 :
            self.label_show_original_real.setPixmap(QtGui.QPixmap(""))
            self.label_show_tested_real.setPixmap(QtGui.QPixmap(""))
            '''刷新button状态'''
            self.Button_openCV_real_2.setCheckable(False)
            self.Button_YOLO_real_2.setCheckable(False)
            self.Button_combin_real_2.setCheckable(False)
            self.Button_openCV_real_2.setCheckable(True)
            self.Button_YOLO_real_2.setCheckable(True)
            self.Button_combin_real_2.setCheckable(True)

            self.mode = ''
        elif index ==1 :
            self.label_show_original_unreal.setPixmap(QtGui.QPixmap(""))
            self.label_show_tested_unreal.setPixmap(QtGui.QPixmap(""))
            '''刷新button状态'''
            self.Button_openCV_unreal.setCheckable(False)
            self.Button_YOLO_unreal.setCheckable(False)
            self.Button_combin_unreal.setCheckable(False)
            self.Button_openCV_unreal.setCheckable(True)
            self.Button_YOLO_unreal.setCheckable(True)
            self.Button_combin_unreal.setCheckable(True)
            self.mode = ''

        elif index ==3:
            self.label_show_original_show.setPixmap(QtGui.QPixmap(""))
            self.label_show_opencv_show.setPixmap(QtGui.QPixmap(""))
            self.label_show_yolo_show.setPixmap(QtGui.QPixmap(""))
            self.label_show_combine_show.setPixmap(QtGui.QPixmap(""))


###############tab1实时检测部分函数


    # 建立检测按键通信连接
    def slot_init(self):
        #实时检测部分
        self.Button_openCV_real_2.toggled.connect(self.testing_opencv_unreal)
        self.Button_YOLO_real_2.toggled.connect(self.testing_YOLO_unreal)
        self.Button_combin_real_2.toggled.connect(self.testing_combin_unreal)
        self.pushButton_end_real.clicked.connect(self.terminate)
        self.pushButton_begin_real.clicked.connect(self.start)
        #离线检测部分
        # 按键确认初始化
        self.pushButton_skim.clicked.connect(self.getfiles)
        self.pushButton_confirm.clicked.connect(self.confirm_files)
        self.Button_openCV_unreal.toggled.connect(self.testing_opencv_unreal)
        self.Button_YOLO_unreal.toggled.connect(self.testing_YOLO_unreal)
        self.Button_combin_unreal.toggled.connect(self.testing_combin_unreal)
        # 时间信号
        self.timer_camera.timeout.connect(self.camera_test)
        self.timer_video.timeout.connect(self.video_test)
        self.timer_record.timeout.connect(self.video_play)

    '''###实时检测功能分类
    def testing_opencv_real(self):
        self.open_camera_click()
        self.mode = 'opencv'

    def testing_YOLO_real(self):
        self.open_camera_click()
        self.mode = 'YOLO'

    def testing_combin_real(self):
        self.open_camera_click()
        self.mode = 'combin'
    '''
####开始结束按键功能
    def start(self):
        if self.timer_camera.isActive():
            return
        elif self.mode =='':
            QMessageBox.information(self, "提示", "请选择检测方式")
        else:
            self.flag = [0, 0, 0, 0]  # 打火机火焰，森林火焰，烟雾，电火花
            self.begin_frame = [0, 0, 0, 0]
            self.type_counting = [0, 0, 0, 0]
            self.counting = 0
            self.open_camera_click()

    def terminate(self):
        self.refresh()
###实时/离线检测功能分类
    def testing_opencv_unreal(self):
        self.mode = 'opencv'


    def testing_YOLO_unreal(self):
        self.mode = 'YOLO'


    def testing_combin_unreal(self):
        self.mode = 'combin'


    #初始化timer_camera
    def open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg =QMessageBox.information(self, "提示", "请检查摄像头连接")
                return

            else:
                self.addr = './' + self.saving_addr + '/' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.avi'
                self.file_name = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.avi'
                self.fps = self.cap.get(cv2.CAP_PROP_FPS)
                self.total = self.record_time * self.fps
                self.VWirte = cv2.VideoWriter(
                    self.addr, cv2.VideoWriter_fourcc('I', '4', '2', '0'), self.fps, self.shape)
                ##存入数据库
                self.database.retime_insert_auto(self.file_name, self.addr)
                self.textEdit_real.clear()
                self.counting = 0
                self.timer_camera.start(30)#30毫秒发一次信号
        else:
            pass

    def camera_test(self):
        if self.counting < self.total:
            pass
        else:
            time.sleep(1)
            self.VWirte.release()
            if self.flag == 1:
                self.database.insert_retime_detial_end(self.file_name, self.begin_frame, self.counting)
            self.counting = 0
            #
            self.addr = './' + self.saving_addr + '/' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.avi'
            self.file_name = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) + '.avi'
            self.VWirte = cv2.VideoWriter(
                self.addr, cv2.VideoWriter_fourcc('I', '4', '2', '0'), self.fps, self.shape)
            ##存入数据库
            self.database.retime_insert_auto(self.file_name, self.addr)
            print(self.file_name)

        flag, self.image = self.cap.read()
        original_BGR = cv2.resize(self.image, self.shape)
        original_RGB = cv2.cvtColor(original_BGR, cv2.COLOR_BGR2RGB)
        if self.mode == 'opencv':
            result = self.opencv_testing.testing(self.image)
            tested_BGR = cv2.resize(self.image, self.shape)
            tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
        elif self.mode == 'YOLO':
            #print('using YOLO testing')
            result = predict_camera(self.net, self.image)
            tested_BGR = cv2.resize(self.image, self.shape)
            tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
        elif self.mode =='combin':
            result = self.combine_testing.combine(self.net, self.image)
            tested_BGR = cv2.resize(self.image, self.shape)
            tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
        self.VWirte.write(tested_BGR)
        original_Image = QtGui.QImage(original_RGB.data, original_RGB.shape[1], original_RGB.shape[0], QtGui.QImage.Format_RGB888)
        tested_Image = QtGui.QImage(tested_RGB.data, original_RGB.shape[1], original_RGB.shape[0],
                                      QtGui.QImage.Format_RGB888)
        self.label_show_original_real.setPixmap(QtGui.QPixmap.fromImage(original_Image))
        self.label_show_tested_real.setPixmap(QtGui.QPixmap.fromImage(tested_Image))
        '''
        if len(result) != 0 and self.flag == 0:
            self.begin_frame = self.counting
            self.flag = 1
            self.database.insert_retime_detial(self.file_name, result[0][2], self.begin_frame)
            self.textEdit_real.setPlainText('时间：'+ time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) +
                                       ' 类型： '+ result[0][2] +
                                       ' 文件名： '+self.file_name+
                                       '起始帧： ' +str(self.begin_frame))
        elif len(result) == 0 and self.flag == 1:
            if self.type_counting>self.tolerance:
                self.database.insert_retime_detial_end(self.file_name, self.begin_frame, self.counting)
                self.type_counting = 0
                self.flag = 0
            else:
                self.type_counting += 1
        else:
            pass
        '''
        if len(result) != 0:
            for i in result:
                temp = [0,0,0,0]
                if i[2] == 'fire':
                    temp[0] = 1
                elif i[2] == 'forestfire':
                    temp[1] = 1
                elif i[2] == 'smog':
                    temp[2] = 1
                elif i[2] == 'spark':
                    temp[3] = 1
            for i in range(4):
                if temp[i] == 1 :
                    if self.flag[i] == 0:
                        self.flag[i] = 1
                        self.begin_frame[i] = self.counting
                        self.database.insert_retime_detial(self.file_name, self.type[i], self.begin_frame[i])
                        self.textEdit_real.setPlainText('时间：' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) +
                                                        ' 类型： ' +self.type[i] +
                                                        ' 文件名： ' + self.file_name +
                                                        '起始帧： ' + str(self.begin_frame[i]))
                        self.type_counting[i] = 0
                    else:
                        self.type_counting[i] =0
                elif temp[i] == 0 and self.flag[i] ==1:
                    if self.type_counting[i] >= self.tolerance:
                        self.database.insert_retime_detial_end(self.file_name, self.type[i],self.begin_frame[i], self.counting)
                        self.type_counting[i] = 0
                        self.flag[i] = 0
                        self.textEdit_real.setPlainText('时间：' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) +
                                                        ' 类型： ' + self.type[i] +
                                                        ' 文件名： ' + self.file_name +
                                                        '起始帧： ' + str(self.begin_frame[i])+
                                                          '结束帧： ' + str(self.counting))
                    else:
                        self.type_counting[i] += 1
        elif len(result) == 0 and self.flag != [0,0,0,0]:
            for i in range(4):
                if self.flag[i] ==1:
                    if self.type_counting[i]>= self.tolerance:
                        self.database.insert_retime_detial_end(self.file_name, self.type[i],self.begin_frame[i], self.counting)
                        self.type_counting[i] = 0
                        self.flag[i] = 0
                        self.textEdit_real.setPlainText('时间：' + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) +
                                                        ' 类型： ' + self.type[i] +
                                                        ' 文件名： ' + self.file_name +
                                                        '起始帧： ' + str(self.begin_frame[i]) +
                                                        '结束帧： ' + str(self.counting))
                    else:
                        self.type_counting[i] += 1
        else:
            pass
        self.counting += 1

##########离线检测部分

    ##########检测文件并显示存储
    def video_test(self):
        if self.cap.isOpened():
            res, image_raw = self.cap.read()
            if res:
                original_BGR = cv2.resize(image_raw, self.shape)
                original_RGB = cv2.cvtColor(original_BGR, cv2.COLOR_BGR2RGB)
                if self.mode == 'opencv':
                    result = self.opencv_testing.testing(image_raw)
                    tested_BGR = cv2.resize(image_raw, self.shape)
                    tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
                elif self.mode == 'YOLO':
                    #print('using YOLO testing')
                    result = predict_camera(self.net, image_raw)
                    tested_BGR = cv2.resize(image_raw, self.shape)
                    tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
                elif self.mode =='combin':
                    #print('unsing combine testing')
                    result = self.combine_testing.combine(self.net, image_raw)
                    tested_BGR = cv2.resize(image_raw, self.shape)
                    tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
                else:
                    return

                #数据库存储
                '''
                if len(result) != 0 and self.flag == 0:
                    self.begin_frame = self.counting
                    self.flag = 1

                    self.database.insert_offline_detial(self.original_name[1], self.tested_name[1], result[0][2], self.begin_frame)
                    self.textEdit_unreal.clear()
                    self.textEdit_unreal.setPlainText( ' 文件名： ' + self.tested_name[1] +
                                               ' 类型： ' + result[0][2] +
                                               '起始帧： ' + str(self.begin_frame))
                    self.type = result[0][2]
                elif len(result) == 0 and self.flag == 1:
                    if self.type_counting > 5:
                        self.database.insert_offline_detail_end(self.original_name[1],self.begin_frame,self.counting)
                        self.type_counting = 0
                        self.flag = 0
                        self.textEdit_unreal.clear()
                        self.textEdit_unreal.setPlainText(' 文件名： ' + self.tested_name[1] +
                                                   ' 类型： ' + self.type +
                                                   '起始帧： ' + str(self.begin_frame)+
                                                   '结束帧： '+ str(self.counting))
                    else:
                        self.type_counting += 1
                else:
                    pass
                '''
                if len(result) != 0:
                    for i in result:
                        temp = [0, 0, 0, 0]
                        if i[2] == 'fire':
                            temp[0] = 1
                        elif i[2] == 'forestfire':
                            temp[1] = 1
                        elif i[2] == 'smog':
                            temp[2] = 1
                        elif i[2] == 'spark':
                            temp[3] = 1
                    for i in range(4):
                        if temp[i] == 1:
                            if self.flag[i] == 0:
                                self.flag[i] = 1
                                self.begin_frame[i] = self.counting
                                self.database.insert_offline_detial(self.original_name[1], self.tested_name[1], self.type[i], self.begin_frame[i])
                                self.textEdit_unreal.setPlainText(' 文件名： ' + self.tested_name[1] +
                                                                  ' 类型： ' + self.type[i] +
                                                                  '起始帧： ' + str(self.begin_frame[i]))
                                self.type_counting[i] = 0
                            else:
                                self.type_counting[i] = 0
                        elif temp[i] == 0 and self.flag[i] == 1:
                            if self.type_counting[i] >= self.tolerance:
                                self.database.insert_offline_detail_end(self.original_name[1],self.type[i], self.begin_frame[i],
                                                                        self.counting)
                                self.textEdit_unreal.setPlainText(' 文件名： ' + self.tested_name[1] +
                                                                  ' 类型： ' + self.type[i] +
                                                                  '起始帧： ' + str(self.begin_frame[i]) +
                                                                  '结束帧： ' + str(self.counting))
                                self.type_counting[i] = 0
                                self.flag[i] = 0
                            else:
                                self.type_counting[i] += 1
                elif len(result) == 0 and self.flag != [0, 0, 0, 0]:
                    for i in range(4):
                        if self.flag[i] == 1:
                            if self.type_counting[i] >= self.tolerance:
                                self.database.insert_offline_detail_end(self.original_name[1], self.type[i],
                                                                        self.begin_frame[i],
                                                                        self.counting)
                                self.type_counting[i] = 0
                                self.flag[i] = 0
                                self.textEdit_unreal.setPlainText(' 文件名： ' + self.tested_name[1] +
                                                                  ' 类型： ' + self.type[i] +
                                                                  '起始帧： ' + str(self.begin_frame[i]) +
                                                                  '结束帧： ' + str(self.counting))
                            else:
                                self.type_counting[i] += 1

                #显示图像
                self.VWirte.write(tested_BGR)

                original_image = QtGui.QImage(original_RGB.flatten(), original_RGB.shape[1], original_RGB.shape[0], QtGui.QImage.Format_RGB888)
                tested_image = QtGui.QImage(tested_RGB.flatten(), original_RGB.shape[1], original_RGB.shape[0], QtGui.QImage.Format_RGB888)
                self.label_show_original_unreal.setPixmap(QtGui.QPixmap.fromImage(original_image))
                self.label_show_tested_unreal.setPixmap(QtGui.QPixmap.fromImage(tested_image))
                '''
                temp_image = QImage(original.flatten(), width, height, QImage.Format_RGB888)
                temp_pixmap = QPixmap.fromImage(temp_image)
                self.label_show_original.setPixmap(temp_pixmap)
            '''
                self.counting += 1
                self.progressBar.setValue(self.counting)

            else:
                self.timer_video.stop()
                self.cap.release()
                time.sleep(1)
                self.VWirte.release()
                return

    def backstage_testing(self):
        self.counting = 0
        if self.cap.isOpened():
            res, image_raw = self.cap.read()
            while res:
                #original_BGR = cv2.resize(image_raw, self.shape)
                #original_RGB = cv2.cvtColor(original_BGR, cv2.COLOR_BGR2RGB)
                if self.mode == 'opencv':
                    result = self.opencv_testing.testing(image_raw)
                    tested_BGR = cv2.resize(image_raw, self.shape)
                    #tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
                elif self.mode == 'YOLO':
                    # print('using YOLO testing')
                    result = predict_camera(self.net, image_raw)
                    tested_BGR = cv2.resize(image_raw, self.shape)
                    #tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
                elif self.mode == 'combin':
                    # print('unsing combine testing')
                    result = self.combine_testing.combine(self.net, image_raw)
                    tested_BGR = cv2.resize(image_raw, self.shape)
                    #tested_RGB = cv2.cvtColor(tested_BGR, cv2.COLOR_BGR2RGB)
                else:
                    return

                #存储显示图像
                self.VWirte.write(tested_BGR)

                # 数据库存储

                if len(result) != 0:
                    for i in result:
                        temp = [0, 0, 0, 0]
                        if i[2] == 'fire':
                            temp[0] = 1
                        elif i[2] == 'forestfire':
                            temp[1] = 1
                        elif i[2] == 'smog':
                            temp[2] = 1
                        elif i[2] == 'spark':
                            temp[3] = 1
                    for i in range(4):
                        if temp[i] == 1:
                            if self.flag[i] == 0:
                                self.flag[i] = 1
                                self.begin_frame[i] = self.counting
                                self.database.insert_offline_detial(self.original_name[1], self.tested_name[1],
                                                                    self.type[i], self.begin_frame[i])
                                self.textEdit_unreal.setPlainText(' 文件名： ' + self.tested_name[1] +
                                                                  ' 类型： ' + self.type[i] +
                                                                  '起始帧： ' + str(self.begin_frame[i]))
                                self.type_counting[i] = 0
                            else:
                                self.type_counting[i] = 0
                        elif temp[i] == 0 and self.flag[i] == 1:
                            if self.type_counting[i] >= self.tolerance:
                                self.database.insert_offline_detail_end(self.original_name[1], self.type[i],
                                                                        self.begin_frame[i],
                                                                        self.counting)
                                self.textEdit_unreal.setPlainText(' 文件名： ' + self.tested_name[1] +
                                                                  ' 类型： ' + self.type[i] +
                                                                  '起始帧： ' + str(self.begin_frame[i]) +
                                                                  '结束帧： ' + str(self.counting))
                                self.type_counting[i] = 0
                                self.flag[i] = 0
                            else:
                                self.type_counting[i] += 1
                elif len(result) == 0 and self.flag != [0, 0, 0, 0]:
                    for i in range(4):
                        if self.flag[i] == 1:
                            if self.type_counting[i] >= self.tolerance:
                                self.database.insert_offline_detail_end(self.original_name[1], self.type[i],
                                                                        self.begin_frame[i],
                                                                        self.counting)
                                self.type_counting[i] = 0
                                self.flag[i] = 0
                                self.textEdit_unreal.setPlainText(' 文件名： ' + self.tested_name[1] +
                                                                  ' 类型： ' + self.type[i] +
                                                                  '起始帧： ' + str(self.begin_frame[i]) +
                                                                  '结束帧： ' + str(self.counting))
                            else:
                                self.type_counting[i] += 1
                self.counting += 1

                self.progressBar.setValue(self.counting)

                res, image_raw = self.cap.read()

            #视屏处理完毕释放资源
            self.cap.release()
            time.sleep(1)
            self.VWirte.release()
            return

    #############选择文件功能
    def getfiles(self):
        addr = self.un_root_addr.text()
        self.renew_addr = ''
        if len(addr) == 0:
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      "./",
                                                      "All Files (*);;MP4 Files (*.mp4);;AVI Files (*.avi);;")

        elif os.path.isdir(addr)|os.path.isfile(addr):
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      addr,
                                                      "All Files (*);;MP4 Files(*.mp4) ;; AVI Files (*.avi);;")

        else:
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      "./",
                                                      "All Files (*);;MP4 Files(*.mp4) ;; AVI Files (*.avi);;")

        self.show_addr(files)

    def confirm_files(self):
        self.timer_video.stop()
        self.cap.release()
        self.flag = [0, 0, 0, 0]  # 打火机火焰，森林火焰，烟雾，电火花
        self.begin_frame = [0, 0, 0, 0]
        self.type_counting = [0, 0, 0, 0]
        self.counting = 0
        if self.mode =='':
            QMessageBox.information(self, "提示", "请选择检测方式")
            return
        addr = self.un_root_addr.text()
        addr = addr.split('\"')
        addr = list(filter(None, addr))
        self.not_empty = 0
        self.renew_addr = ''
        if addr:
            for i in addr:
                while self.cap.isOpened():
                    time.sleep(5)
                kind = filetype.guess(i)
                if kind.extension =='avi' or kind.extension =='mp4' :
                    temp = []
                    temp.append(i)
                    self.show_addr_tested(temp)
            if self.not_empty == 0 :
                files, ok1 = QFileDialog.getOpenFileNames(self,
                                                          "多文件选择",
                                                          "./",
                                                          "All Files (*);;MP4 Files(*.mp4);;AVI Files (*.avi)")
                self.show_addr_tested(files)
        else:
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      "./",
                                                       "All Files (*);;MP4 Files(*.mp4);;AVI Files (*.avi)")
            self.show_addr_tested(files)

    # 在文本框中显示地址
    def show_addr(self,files):
        if files:
            self.not_empty = 1
            for i in files:
                self.renew_addr = self.renew_addr + '\"' + i + '\"'
        self.un_root_addr.setText(self.renew_addr)
        print('open' + self.renew_addr)

    def show_addr_tested(self, files):
        if files:
            self.not_empty = 1
            for i in files:
                self.addr = i
                self.renew_addr = self.renew_addr + '\"' + i + '\"'
                self.un_root_addr.setText(self.renew_addr)
                self.testing()


    def testing(self):
        self.cap.open(self.addr)
        #设置存储视频文件的路径，名称
        temp = self.addr.rsplit('.', 1)
        file_name = temp[0] + '_tested.avi'

        self.original_name = self.addr.rsplit('/',1)
        self.tested_name = file_name.rsplit('/',1)
        self.database.insert_offline_record(self.original_name[1], self.addr, self.tested_name[1], file_name)

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.VWirte = cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc('I', '4', '2', '0'), self.fps,
                                      self.shape)

        self.counting = 0
        self.textEdit_unreal.clear()

        self.progressBar.setMaximum(self.cap.get(7))
        self.progressBar.setRange(0,self.cap.get(7))
        self.progressBar.setValue(0)

        if self.checkBox_backstage.isChecked():
            self.backstage_testing()
        else:
            self.timer_video.start(30)



#########tab3检测记录
    def generateMenu(self, pos):
        # rint( pos)
        row_num = -1
        for i in self.tableWidget_detial.selectionModel().selection().indexes():
            row_num = i.row()

        menu = QMenu()
        item1 = menu.addAction(u"跳转")
        action = menu.exec_(self.tableWidget_detial.mapToGlobal(pos))
        try:
            if action == item1:
                print('您选了跳转到：' + self.tableWidget_detial.item(row_num, 3).text()+'帧')
                self.sl.setValue(int(self.tableWidget_detial.item(row_num, 3).text()))
            else:
                return
        except:
            print('您选了跳转到：' + '0' + '帧')
            self.sl.setValue(0)

    def inquiry_detial(self,id,name):
        list = self.database.inquiry_detial(id, name)
        if list:
            j=0
            for i in list:
                self.add_detial(j, i)
                j += 1


    def inquiry_database(self):
        #清空列表
        self.root_real.takeChildren()
        self.root_unreal_original.takeChildren()
        self.root_unreal_tested.takeChildren()
        list = self.database.inquiry(self.database.table_retime_record)
        for i in list:
            self.addNode(self.root_real,i[0],i[1],i[2],i[3])
        list = self.database.inquiry(self.database.table_offline_original_record)
        for i in list:
            self.addNode(self.root_unreal_original,'0',i[0],'',i[1])
        list = self.database.inquiry(self.database.table_offline_tested_record)
        for i in list:
            self.addNode(self.root_unreal_tested, i[0],i[1],i[2],i[3])

    def add_detial(self,row, list):
        for i in range(0,5):
            if str(list[i]):
                newItem = QTableWidgetItem(str(list[i]))
                self.tableWidget_detial.setItem(row, i, newItem)




    def addNode(self, root, txt1, txt2, txt3,txt4):
        child = QTreeWidgetItem(root)
        if txt1:
            child.setText(0, str(txt1))
        else:
            pass
        if txt2:
            child.setText(1, str(txt2))
        else:
            pass
        if txt2:
            child.setText(2, str(txt3))
        else:
            pass
        if txt2:
            child.setText(3, str(txt4))
        else:
            pass

    def onClicked_real(self):
        item=self.treeWidget_realrecord.currentItem()
        print('id = %s,文件名=%s,检测结果统计=%s,文件地址=%s' % (item.text(0), item.text(1),item.text(2),item.text(3)))
        self.tableWidget_detial.clear()
        self.inquiry_detial(item.text(0), item.text(1))

        self.cap.open(item.text(3))
        self.sl.setMaximum(self.cap.get(7)-1)
        self.sl.setValue(0)
        self.timer_record.start(30)



    def video_play(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES,self.sl.value())
        res, image_raw = self.cap.read()
        if res:
            original_RGB = cv2.cvtColor(image_raw, cv2.COLOR_BGR2RGB)
            original_image = QtGui.QImage(original_RGB.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                          QtGui.QImage.Format_RGB888)
            self.label_show_video.setPixmap(QtGui.QPixmap.fromImage(original_image))
        if self.sl.value()+1 <(self.cap.get(7)-1):
            self.sl.setValue(self.sl.value()+1)
        else :
            pass

    def generaterecordMenu(self, pos):
        if self.cap.isOpened():
            self.cap.release()

        self.cap = cv2.VideoCapture()
        # rint( pos)
        row_num = -1
        for i in self.treeWidget_realrecord.selectionModel().selection().indexes():
            row_num = i.row()

        menu = QMenu()
        item1 = menu.addAction(u"删除")
        action = menu.exec_(self.treeWidget_realrecord.mapToGlobal(pos))
        try:
            if action == item1:
                self.record_right_click()
            else:
                pass
        except:
            pass


    def record_right_click(self):
        item = self.treeWidget_realrecord.currentItem()
        print('id = %s,文件名=%s,检测结果统计=%s,文件地址=%s' % (item.text(0), item.text(1), item.text(2), item.text(3)))
        if item.text(0) =='实时检测录像' or item.text(0) =='离线原始视频' or item.text(0) =='离线检测视频' :
            QMessageBox.information(self, "提示", "目录信息无法删除")
        else:
            reply = QMessageBox.information(self, "提示", "是否删除", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes)
            if reply ==16384:
                self.delete_item(item.text(0), item.text(1))
            else:
                pass

    def delete_item(self,id,name):
        if id.isnumeric():
            if int(id) == 0:
                self.database.offline_file_delete(name)
            else:
                self.database.retime_file_delete(int(id))
        else:
            self.database.offline_file_delete(id)

        self.refresh()

##########算法展示部分部分

    ##########检测文件并显示存储
    def video_test_show(self):
        if self.cap.isOpened():
            res, image_raw = self.cap.read()
            if res:
                original_BGR = cv2.resize(image_raw, (336, 336))
                original_RGB = cv2.cvtColor(original_BGR, cv2.COLOR_BGR2RGB)

                image_raw_opencv = copy(image_raw)
                result1 = self.opencv_testing.testing(image_raw_opencv)
                tested_BGR_opencv = cv2.resize(image_raw_opencv, (336, 336))
                tested_RGB_opencv = cv2.cvtColor(tested_BGR_opencv, cv2.COLOR_BGR2RGB)

                image_raw_yolo = copy(image_raw)
                result2 = predict_camera(self.net, image_raw_yolo)
                tested_BGR_yolo = cv2.resize(image_raw_yolo, (336, 336))
                tested_RGB_yolo = cv2.cvtColor(tested_BGR_yolo , cv2.COLOR_BGR2RGB)

                image_raw_combine = copy(image_raw)
                result3 = self.combine_testing.combine(self.net, image_raw_combine)
                tested_BGR_combine = cv2.resize(image_raw_combine, (336, 336))
                tested_RGB_combine = cv2.cvtColor(tested_BGR_combine, cv2.COLOR_BGR2RGB)


                #显示图像

                original_image = QtGui.QImage(original_RGB.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                              QtGui.QImage.Format_RGB888)
                opencv_image = QtGui.QImage(tested_RGB_opencv.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                            QtGui.QImage.Format_RGB888)
                yolo_image = QtGui.QImage(tested_RGB_yolo.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                              QtGui.QImage.Format_RGB888)
                combine_image = QtGui.QImage(tested_RGB_combine.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                            QtGui.QImage.Format_RGB888)

                self.label_show_original_show.setPixmap(QtGui.QPixmap.fromImage(original_image))
                self.label_show_opencv_show.setPixmap(QtGui.QPixmap.fromImage(opencv_image))
                self.label_show_yolo_show.setPixmap(QtGui.QPixmap.fromImage(yolo_image))
                self.label_show_combine_show.setPixmap(QtGui.QPixmap.fromImage(combine_image))
                '''
                temp_image = QImage(original.flatten(), width, height, QImage.Format_RGB888)
                temp_pixmap = QPixmap.fromImage(temp_image)
                self.label_show_original.setPixmap(temp_pixmap)
            '''

            else:
                self.timer_show.stop()
                self.cap.release()
                return

    #############选择文件功能
    def getfiles_show(self):
        addr = self.show_root_addr.text()
        self.renew_addr = ''
        if len(addr) == 0:
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      "./",
                                                      "All Files (*);;MP4 Files (*.mp4);;AVI Files (*.avi);;")

        elif os.path.isdir(addr)|os.path.isfile(addr):
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      addr,
                                                      "All Files (*);;MP4 Files(*.mp4) ;; AVI Files (*.avi);;")

        else:
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      "./",
                                                      "All Files (*);;MP4 Files(*.mp4) ;; AVI Files (*.avi);;")

        self.show_addr_show(files)

    def confirm_files_show(self):
        self.timer_camera.stop()  # 实时检测
        self.timer_video.stop()  # 离线检测
        self.timer_record.stop()  # 检测记录
        self.timer_show.stop()
        self.timer_show_real.stop()
        self.cap.release()
        addr = self.show_root_addr.text()
        addr = addr.split('\"')
        addr = list(filter(None, addr))
        self.not_empty = 0
        self.renew_addr = ''
        if addr:
            for i in addr:
                while self.cap.isOpened():
                    time.sleep(5)
                kind = filetype.guess(i)
                if kind.extension =='avi' or kind.extension =='mp4' :
                    temp = []
                    temp.append(i)
                    self.show_addr_tested_show(temp)
            if self.not_empty == 0 :
                files, ok1 = QFileDialog.getOpenFileNames(self,
                                                          "多文件选择",
                                                          "./",
                                                          "All Files (*);;MP4 Files(*.mp4);;AVI Files (*.avi)")
                self.show_addr_tested_show(files)
        else:
            files, ok1 = QFileDialog.getOpenFileNames(self,
                                                      "多文件选择",
                                                      "./",
                                                       "All Files (*);;MP4 Files(*.mp4);;AVI Files (*.avi)")
            self.show_addr_tested_show(files)

    # 在文本框中显示地址
    def show_addr_show(self,files):
        if files:
            self.not_empty = 1
            for i in files:
                self.renew_addr = self.renew_addr + '\"' + i + '\"'
        self.show_root_addr.setText(self.renew_addr)
        print('open' + self.renew_addr)

    def show_addr_tested_show(self, files):
        if files:
            self.not_empty = 1
            for i in files:
                self.addr = i
                self.renew_addr = self.renew_addr + '\"' + i + '\"'
                self.show_root_addr.setText(self.renew_addr)
                self.testing_show()


    def testing_show(self):
        self.cap.open(self.addr)
        #设置存储视频文件的路径，名称

        self.timer_show.start(30)


    def open_camera_click_show(self):
        self.timer_camera.stop()  # 实时检测
        self.timer_video.stop()  # 离线检测
        self.timer_record.stop()  # 检测记录
        self.timer_show.stop()
        self.timer_show_real.stop()
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg =QMessageBox.information(self, "提示", "请检查摄像头连接")
                return
            else:
                self.timer_show_real.start(30)#30毫秒发一次信号
        else:
            pass

    def camera_test_show(self):
        flag, image_raw = self.cap.read()
        if flag:
            original_BGR = cv2.resize(image_raw, (336, 336))
            original_RGB = cv2.cvtColor(original_BGR, cv2.COLOR_BGR2RGB)

            image_raw_opencv = copy(image_raw)
            result1 = self.opencv_testing.testing(image_raw_opencv)
            tested_BGR_opencv = cv2.resize(image_raw_opencv, (336, 336))
            tested_RGB_opencv = cv2.cvtColor(tested_BGR_opencv, cv2.COLOR_BGR2RGB)

            image_raw_yolo = copy(image_raw)
            result2 = predict_camera(self.net, image_raw_yolo)
            tested_BGR_yolo = cv2.resize(image_raw_yolo, (336, 336))
            tested_RGB_yolo = cv2.cvtColor(tested_BGR_yolo, cv2.COLOR_BGR2RGB)

            image_raw_combine = copy(image_raw)
            result3 = self.combine_testing.combine(self.net, image_raw_combine)
            tested_BGR_combine = cv2.resize(image_raw_combine, (336, 336))
            tested_RGB_combine = cv2.cvtColor(tested_BGR_combine, cv2.COLOR_BGR2RGB)

            # 显示图像

            original_image = QtGui.QImage(original_RGB.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                          QtGui.QImage.Format_RGB888)
            opencv_image = QtGui.QImage(tested_RGB_opencv.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                        QtGui.QImage.Format_RGB888)
            yolo_image = QtGui.QImage(tested_RGB_yolo.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                      QtGui.QImage.Format_RGB888)
            combine_image = QtGui.QImage(tested_RGB_combine.flatten(), original_RGB.shape[1], original_RGB.shape[0],
                                         QtGui.QImage.Format_RGB888)

            self.label_show_original_show.setPixmap(QtGui.QPixmap.fromImage(original_image))
            self.label_show_opencv_show.setPixmap(QtGui.QPixmap.fromImage(opencv_image))
            self.label_show_yolo_show.setPixmap(QtGui.QPixmap.fromImage(yolo_image))
            self.label_show_combine_show.setPixmap(QtGui.QPixmap.fromImage(combine_image))
        else:
            pass

