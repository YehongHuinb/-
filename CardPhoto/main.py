# -*- coding: gbk -*-
'''
@Author: YHH
@Date: 2020-06-06 20:58:56
@LastEditTime: 2020-07-08 10:36:44
@Description: ��������
@FilePath: \CardPhoto\main.py
'''

import sys
from PyQt5 import QtWidgets
from UseViews import StartView

app = QtWidgets.QApplication(sys.argv)
start = StartView()
start.show()
sys.exit(app.exec_())
