# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beginwindows.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("拼图游戏")
        Form.resize(800, 600)
        self.backgurand = QtWidgets.QGraphicsView(Form)
        self.backgurand.setGeometry(QtCore.QRect(0, 0, 911, 641))
        self.backgurand.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.backgurand.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.backgurand.setObjectName("backgurand")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 350, 471, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.buttons = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttons.setContentsMargins(0, 0, 0, 0)
        self.buttons.setSpacing(40)
        self.buttons.setObjectName("buttons")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.buttons.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.buttons.addWidget(self.pushButton)
        self.tltle = QtWidgets.QTextEdit(Form)
        self.tltle.setGeometry(QtCore.QRect(180, 90, 411, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tltle.sizePolicy().hasHeightForWidth())
        self.tltle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("汉仪中黑 197")
        font.setPointSize(72)
        self.tltle.setFont(font)
        self.tltle.setTabChangesFocus(False)
        self.tltle.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.tltle.setReadOnly(True)
        self.tltle.setTabStopWidth(120)
        self.tltle.setObjectName("tltle")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "开始游戏"))
        self.pushButton.setText(_translate("Form", "退出游戏"))
        self.tltle.setDocumentTitle(_translate("Form", "开始游戏"))
        self.tltle.setPlaceholderText(_translate("Form", "拼图游戏"))
