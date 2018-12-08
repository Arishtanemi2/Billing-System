# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewPrevTrans.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1108, 731)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, -10, 1071, 61))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.backbtnmain = QtWidgets.QPushButton(self.groupBox)
        self.backbtnmain.setGeometry(QtCore.QRect(0, 20, 141, 41))
        self.backbtnmain.setObjectName("backbtnmain")
        self.backbtnmain.clicked.connect(self.backmain)
        self.prevTransTable = QtWidgets.QTableWidget(Dialog)
        self.prevTransTable.setGeometry(QtCore.QRect(35, 61, 1051, 581))
        self.prevTransTable.setObjectName("prevTransTable")
        self.prevTransTable.setColumnCount(6)
        self.prevTransTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.prevTransTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.prevTransTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.prevTransTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.prevTransTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.prevTransTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.prevTransTable.setHorizontalHeaderItem(5, item)
        self.prevTransTable.horizontalHeader().setCascadingSectionResizes(True)
        self.prevTransTable.horizontalHeader().setDefaultSectionSize(174)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.backbtnmain.setText(_translate("Dialog", "Back to Main"))
        item = self.prevTransTable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "S No"))
        item = self.prevTransTable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Invoice Number"))
        item = self.prevTransTable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Time of Transaction"))
        item = self.prevTransTable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Mobile Number"))
        item = self.prevTransTable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Amount paid"))
        item = self.prevTransTable.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Mode of Payment"))

    def backmain(self):
        print("Back button clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

