# -*- coding: gbk -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from MyButton import MyButton


class Ui_mainView(object):
    def setupUi(self, mainView):
        mainView.setObjectName("mainView")
        mainView.resize(939, 571)
        mainView.setMinimumSize(QtCore.QSize(939, 571))
        mainView.setMaximumSize(QtCore.QSize(939, 571))
        self.centralwidget = QtWidgets.QWidget(mainView)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 50, 471, 381))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gb_bgcolor = QtWidgets.QGroupBox(self.widget)
        self.gb_bgcolor.setObjectName("gb_bgcolor")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gb_bgcolor)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_rbg = QtWidgets.QRadioButton(self.gb_bgcolor)
        self.btn_rbg.setObjectName("btn_rbg")
        self.horizontalLayout.addWidget(self.btn_rbg)
        self.btn_bbg = QtWidgets.QRadioButton(self.gb_bgcolor)
        self.btn_bbg.setObjectName("btn_bbg")
        self.horizontalLayout.addWidget(self.btn_bbg)
        self.btn_wbg = QtWidgets.QRadioButton(self.gb_bgcolor)
        self.btn_wbg.setObjectName("btn_wbg")
        self.horizontalLayout.addWidget(self.btn_wbg)
        self.gridLayout_2.addWidget(self.gb_bgcolor, 0, 0, 1, 1)
        self.gb_size = QtWidgets.QGroupBox(self.widget)
        self.gb_size.setObjectName("gb_size")
        self.gridLayout = QtWidgets.QGridLayout(self.gb_size)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_twoInch = QtWidgets.QRadioButton(self.gb_size)
        self.btn_twoInch.setObjectName("btn_twoInch")
        self.gridLayout.addWidget(self.btn_twoInch, 1, 0, 1, 1)
        self.btn_StwoInch = QtWidgets.QRadioButton(self.gb_size)
        self.btn_StwoInch.setObjectName("btn_StwoInch")
        self.gridLayout.addWidget(self.btn_StwoInch, 1, 1, 1, 1)
        self.btn_oneInch = QtWidgets.QRadioButton(self.gb_size)
        self.btn_oneInch.setObjectName("btn_oneInch")
        self.gridLayout.addWidget(self.btn_oneInch, 0, 0, 1, 1)
        self.btn_LoneInch = QtWidgets.QRadioButton(self.gb_size)
        self.btn_LoneInch.setObjectName("btn_LoneInch")
        self.gridLayout.addWidget(self.btn_LoneInch, 0, 2, 1, 1)
        self.btn_SoneInch = QtWidgets.QRadioButton(self.gb_size)
        self.btn_SoneInch.setObjectName("btn_SoneInch")
        self.gridLayout.addWidget(self.btn_SoneInch, 0, 1, 1, 1)
        self.btn_LtwoInch = QtWidgets.QRadioButton(self.gb_size)
        self.btn_LtwoInch.setObjectName("btn_LtwoInch")
        self.gridLayout.addWidget(self.btn_LtwoInch, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.gb_size, 1, 0, 1, 1)
        self.btn_beauty = QtWidgets.QCheckBox(self.widget)
        self.btn_beauty.setObjectName("btn_beauty")
        self.gridLayout_2.addWidget(self.btn_beauty, 2, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")

        normalImg = QPixmap('./src/icon/exit2.png')
        self.btn_exit = MyButton(self.widget_2, normalImg)
        self.btn_exit.setObjectName("btn_exit")

        self.gridLayout_3.addWidget(self.btn_exit, 0, 3, 1, 1)

        normalImg = QPixmap('./src/icon/save.png')
        self.btn_save = MyButton(self.widget_2, normalImg)
        self.btn_save.setObjectName("btn_save")

        normalImg = QPixmap('./src/icon/reload.png')
        self.btn_reload = MyButton(mainView, normalImg)
        self.btn_reload.setObjectName("btn_reload")
        self.btn_reload.move(660, 500)

        self.gridLayout_3.addWidget(self.btn_save, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 3, 0, 1, 1)
        self.wid_hole = QtWidgets.QFrame(self.centralwidget)
        self.wid_hole.setGeometry(QtCore.QRect(540, 50, 361, 381))
        self.wid_hole.setObjectName("wid_hole")
        self.lab_preview = QtWidgets.QLabel(self.wid_hole)
        self.lab_preview.setGeometry(QtCore.QRect(0, 0, 361, 381))
        self.lab_preview.setText("")
        self.lab_preview.setObjectName("lab_preview")
        self.lab_preview.setObjectName("lab_preview")
        self.lab_sizeShow = QtWidgets.QLabel(mainView)
        self.lab_sizeShow.setGeometry(QtCore.QRect(540, 450, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        self.lab_sizeShow.setFont(font)
        self.lab_sizeShow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lab_sizeShow.setText("")
        self.lab_sizeShow.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_sizeShow.setObjectName("lab_sizeShow")
        mainView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 30))
        self.menubar.setObjectName("menubar")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        mainView.setMenuBar(self.menubar)
        self.actionabout = QtWidgets.QAction(mainView)
        self.actionabout.setObjectName("actionabout")
        self.menuhelp.addAction(self.actionabout)
        self.menubar.addAction(self.menuhelp.menuAction())
        self.retranslateUi(mainView)
        QtCore.QMetaObject.connectSlotsByName(mainView)

    def retranslateUi(self, mainView):
        _translate = QtCore.QCoreApplication.translate
        mainView.setWindowTitle(_translate("mainView", "快证件照"))
        self.gb_bgcolor.setTitle(_translate("mainView", "底色"))
        self.btn_rbg.setText(_translate("mainView", "红色"))
        self.btn_bbg.setText(_translate("mainView", "蓝色"))
        self.btn_wbg.setText(_translate("mainView", "白色"))
        self.gb_size.setTitle(_translate("mainView", "尺寸"))
        self.btn_twoInch.setText(_translate("mainView", "2寸"))
        self.btn_StwoInch.setText(_translate("mainView", "小2寸"))
        self.btn_oneInch.setText(_translate("mainView", "1寸"))
        self.btn_LoneInch.setText(_translate("mainView", "大1寸"))
        self.btn_SoneInch.setText(_translate("mainView", "小1寸"))
        self.btn_LtwoInch.setText(_translate("mainView", "大2寸"))
        self.btn_beauty.setText(_translate("mainView", "美化"))
        self.menuhelp.setTitle(_translate("mainView", "帮助"))
        self.actionabout.setText(_translate("mainView", "关于"))
