# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/updateproductcategories.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateProductsCategories(object):
    def setupUi(self, UpdateProductsCategories):
        UpdateProductsCategories.setObjectName("UpdateProductsCategories")
        UpdateProductsCategories.resize(497, 285)
        self.centralwidget = QtWidgets.QWidget(UpdateProductsCategories)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        UpdateProductsCategories.setCentralWidget(self.centralwidget)

        self.retranslateUi(UpdateProductsCategories)
        QtCore.QMetaObject.connectSlotsByName(UpdateProductsCategories)

    def retranslateUi(self, UpdateProductsCategories):
        _translate = QtCore.QCoreApplication.translate
        UpdateProductsCategories.setWindowTitle(_translate("UpdateProductsCategories", "Категории продуктов"))
        self.pushButton.setText(_translate("UpdateProductsCategories", "Добавить"))
        self.pushButton_2.setText(_translate("UpdateProductsCategories", "Удалить"))
