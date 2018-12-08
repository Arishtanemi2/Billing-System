from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 741)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 10, 931, 31))
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.label.setObjectName("label")

        self.username_Label = QtWidgets.QLabel(self.widget)
        self.username_Label.setGeometry(QtCore.QRect(70, 0, 111, 31))
        self.username_Label.setObjectName("username_Label")

        self.timeDate = QtWidgets.QLabel(self.widget)
        self.timeDate.setGeometry(QtCore.QRect(766, 0, 161, 31))
        self.timeDate.setObjectName("timeDate")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 470, 921, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.sno_auto = QtWidgets.QLineEdit(self.frame)
        self.sno_auto.setGeometry(QtCore.QRect(0, 0, 81, 31))
        self.sno_auto.setObjectName("sno_auto")

        self.prodNameEnter = QtWidgets.QLineEdit(self.frame)
        self.prodNameEnter.setGeometry(QtCore.QRect(80, 0, 501, 31))
        self.prodNameEnter.setObjectName("prodNameEnter")

        self.QuantEdit = QtWidgets.QLineEdit(self.frame)
        self.QuantEdit.setGeometry(QtCore.QRect(580, 0, 151, 31))
        self.QuantEdit.setObjectName("QuantEdit")

        self.PPerProd = QtWidgets.QLineEdit(self.frame)
        self.PPerProd.setGeometry(QtCore.QRect(730, 0, 191, 31))
        self.PPerProd.setObjectName("PPerProd")

        self.InventoryUpdate = QtWidgets.QPushButton(self.centralwidget)
        self.InventoryUpdate.setGeometry(QtCore.QRect(840, 520, 141, 51))
        self.InventoryUpdate.setObjectName("InventoryUpdate")
        self.InventoryUpdate.clicked.connect(self.update_Inventory)

        self.remProduct = QtWidgets.QPushButton(self.centralwidget)
        self.remProduct.setGeometry(QtCore.QRect(70, 520, 171, 51))
        self.remProduct.setObjectName("remProduct")
        self.remProduct.clicked.connect(self.remove_product)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(29, 49, 981, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 979, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(-5, -9, 991, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.ProductSearch = QtWidgets.QPushButton(self.centralwidget)
        self.ProductSearch.setGeometry(QtCore.QRect(450, 520, 161, 51))
        self.ProductSearch.setObjectName("ProductSearch")
        self.ProductSearch.clicked.connect(self.product_searched)

        self.backoff = QtWidgets.QPushButton(self.centralwidget)
        self.backoff.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.backoff.setObjectName("backoff")
        self.backoff.clicked.connect(self.back_clicked)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 22))
        self.menubar.setObjectName("menubar")

        self.menuGo_Back = QtWidgets.QMenu(self.menubar)
        self.menuGo_Back.setTitle("")
        self.menuGo_Back.setObjectName("menuGo_Back")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGo_Back.menuAction())

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome,"))
        self.username_Label.setText(_translate("MainWindow", "User"))
        self.timeDate.setText(_translate("MainWindow", "00-00-0000 00 : 00 : 00"))
        self.sno_auto.setText(_translate("MainWindow", "     (auto)"))
        self.prodNameEnter.setText(_translate("MainWindow", "Product Name or ID"))
        self.QuantEdit.setText(_translate("MainWindow", "Quantity"))
        self.PPerProd.setText(_translate("MainWindow", "Price per Product"))
        self.InventoryUpdate.setText(_translate("MainWindow", "Update Inventory"))
        self.remProduct.setText(_translate("MainWindow", "Remove Product(s)"))
        self.ProductSearch.setText(_translate("MainWindow", "Search Product"))
        self.backoff.setText(_translate("MainWindow", "<"))

    def update_Inventory(self):
        print("Inventory updated")

    def back_clicked(self):
        print("Bye")

    def remove_product(self):
        print("Product removed")

    def product_searched(self):
        print("Product searched")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
