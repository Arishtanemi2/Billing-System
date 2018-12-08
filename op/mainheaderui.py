# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainheaderui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 739)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.billing = QtWidgets.QPushButton(self.centralwidget)
        self.billing.setGeometry(QtCore.QRect(390, 60, 271, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.billing.setFont(font)
        self.billing.setObjectName("billing")
        self.billing.clicked.connect(self.billingFn)
        self.inventory = QtWidgets.QPushButton(self.centralwidget)
        self.inventory.setGeometry(QtCore.QRect(110, 380, 271, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.inventory.setFont(font)
        self.inventory.setObjectName("inventory")
        self.inventory.clicked.connect(self.inventoryFn)
        self.lol = QtWidgets.QPushButton(self.centralwidget)
        self.lol.setGeometry(QtCore.QRect(670, 380, 271, 201))
        self.lol.setText("")
        self.lol.setObjectName("lol")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.billing.setText(_translate("MainWindow", "Billing"))
        self.inventory.setText(_translate("MainWindow", "Inventory"))

    def billingFn(self):
        print("Billing clicked")

    def inventoryFn(self):
        print("Inventory clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

