# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/clients.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Clients(object):
    def setupUi(self, Clients):
        Clients.setObjectName("Clients")
        Clients.resize(510, 251)
        self.centralwidget = QtWidgets.QWidget(Clients)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setWordWrap(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        Clients.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Clients)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menuBar.setObjectName("menuBar")
        Clients.setMenuBar(self.menuBar)
        self.clients_action = QtWidgets.QAction(Clients)
        self.clients_action.setObjectName("clients_action")
        self.suppliers_action = QtWidgets.QAction(Clients)
        self.suppliers_action.setObjectName("suppliers_action")
        self.products_action = QtWidgets.QAction(Clients)
        self.products_action.setObjectName("products_action")

        self.retranslateUi(Clients)
        QtCore.QMetaObject.connectSlotsByName(Clients)

    def retranslateUi(self, Clients):
        _translate = QtCore.QCoreApplication.translate
        Clients.setWindowTitle(_translate("Clients", "Клиенты"))
        self.pushButton_3.setText(_translate("Clients", "Изменить данные клиента"))
        self.pushButton_2.setText(_translate("Clients", "Удалить клиента"))
        self.pushButton.setText(_translate("Clients", "Добавить клиента"))
        self.pushButton_4.setText(_translate("Clients", "Найти"))
        self.clients_action.setText(_translate("Clients", "Клиенты"))
        self.suppliers_action.setText(_translate("Clients", "Поставщики"))
        self.products_action.setText(_translate("Clients", "Продукты"))
