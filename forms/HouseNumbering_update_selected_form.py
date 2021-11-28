# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HouseNumbering_update_selected_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HouseNumbering_update_selected_form(object):
    def setupUi(self, HouseNumbering_update_selected_form):
        HouseNumbering_update_selected_form.setObjectName("HouseNumbering_update_selected_form")
        HouseNumbering_update_selected_form.resize(560, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HouseNumbering_update_selected_form.sizePolicy().hasHeightForWidth())
        HouseNumbering_update_selected_form.setSizePolicy(sizePolicy)
        HouseNumbering_update_selected_form.setMinimumSize(QtCore.QSize(560, 235))
        HouseNumbering_update_selected_form.setMaximumSize(QtCore.QSize(580, 235))
        self.buttonBox = QtWidgets.QDialogButtonBox(HouseNumbering_update_selected_form)
        self.buttonBox.setGeometry(QtCore.QRect(295, 155, 201, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.CBfields = QtWidgets.QComboBox(HouseNumbering_update_selected_form)
        self.CBfields.setGeometry(QtCore.QRect(5, 30, 211, 24))
        self.CBfields.setObjectName("CBfields")
        self.QLEvalore = QtWidgets.QLineEdit(HouseNumbering_update_selected_form)
        self.QLEvalore.setGeometry(QtCore.QRect(225, 60, 65, 24))
        self.QLEvalore.setObjectName("QLEvalore")
        self.label = QtWidgets.QLabel(HouseNumbering_update_selected_form)
        self.label.setGeometry(QtCore.QRect(10, 5, 536, 20))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(HouseNumbering_update_selected_form)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 201, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(HouseNumbering_update_selected_form)
        self.label_3.setGeometry(QtCore.QRect(10, 195, 536, 21))
        self.label_3.setObjectName("label_3")
        self.cBkeepLatestValue = QtWidgets.QCheckBox(HouseNumbering_update_selected_form)
        self.cBkeepLatestValue.setGeometry(QtCore.QRect(10, 155, 251, 19))
        self.cBkeepLatestValue.setChecked(True)
        self.cBkeepLatestValue.setObjectName("cBkeepLatestValue")
        self.QLEnsteps = QtWidgets.QLineEdit(HouseNumbering_update_selected_form)
        self.QLEnsteps.setGeometry(QtCore.QRect(330, 60, 45, 24))
        self.QLEnsteps.setAutoFillBackground(True)
        self.QLEnsteps.setMaxLength(4)
        self.QLEnsteps.setObjectName("QLEnsteps")
        self.cBkeepCharFixed = QtWidgets.QCheckBox(HouseNumbering_update_selected_form)
        self.cBkeepCharFixed.setGeometry(QtCore.QRect(10, 95, 526, 22))
        self.cBkeepCharFixed.setObjectName("cBkeepCharFixed")
        self.label_4 = QtWidgets.QLabel(HouseNumbering_update_selected_form)
        self.label_4.setGeometry(QtCore.QRect(310, 60, 10, 20))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(HouseNumbering_update_selected_form)
        self.label_5.setGeometry(QtCore.QRect(380, 60, 146, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setObjectName("label_5")
        self.cBsetLabel = QtWidgets.QCheckBox(HouseNumbering_update_selected_form)
        self.cBsetLabel.setGeometry(QtCore.QRect(10, 125, 426, 22))
        self.cBsetLabel.setObjectName("cBsetLabel")

        self.retranslateUi(HouseNumbering_update_selected_form)
        self.buttonBox.accepted.connect(HouseNumbering_update_selected_form.accept)
        self.buttonBox.rejected.connect(HouseNumbering_update_selected_form.reject)
        QtCore.QMetaObject.connectSlotsByName(HouseNumbering_update_selected_form)
        HouseNumbering_update_selected_form.setTabOrder(self.QLEvalore, self.CBfields)
        HouseNumbering_update_selected_form.setTabOrder(self.CBfields, self.cBkeepLatestValue)
        HouseNumbering_update_selected_form.setTabOrder(self.cBkeepLatestValue, self.buttonBox)

    def retranslateUi(self, HouseNumbering_update_selected_form):
        _translate = QtCore.QCoreApplication.translate
        HouseNumbering_update_selected_form.setWindowTitle(_translate("HouseNumbering_update_selected_form", "HouseNumbering"))
        self.label.setText(_translate("HouseNumbering_update_selected_form", "Set value for the data field:"))
        self.label_2.setText(_translate("HouseNumbering_update_selected_form", "Start value: (example1 or 1a)"))
        self.label_3.setText(_translate("HouseNumbering_update_selected_form", "You can also activate this form with F9 funct key - by Marco Braida 2014-2021"))
        self.cBkeepLatestValue.setText(_translate("HouseNumbering_update_selected_form", "Remember latest inserted  value"))
        self.cBkeepCharFixed.setText(_translate("HouseNumbering_update_selected_form", "based on start value keep letter part fixed and increase only numeric part"))
        self.label_4.setText(_translate("HouseNumbering_update_selected_form", "+"))
        self.label_5.setText(_translate("HouseNumbering_update_selected_form", "numeric step value"))
        self.cBsetLabel.setText(_translate("HouseNumbering_update_selected_form", "set the working field as active label for current layer"))
