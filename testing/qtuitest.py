# Form implementation generated from reading ui file '.\recipie_test\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutLeft = QtWidgets.QVBoxLayout()
        self.verticalLayoutLeft.setContentsMargins(10, 10, 10, 10)
        self.verticalLayoutLeft.setObjectName("verticalLayoutLeft")
        self.pushButtonRandom = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonRandom.setMaximumSize(QtCore.QSize(120, 50))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButtonRandom.setFont(font)
        self.pushButtonRandom.setObjectName("pushButtonRandom")
        self.verticalLayoutLeft.addWidget(self.pushButtonRandom, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayoutLeft.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayoutLeft)
        self.verticalLayoutRight = QtWidgets.QVBoxLayout()
        self.verticalLayoutRight.setObjectName("verticalLayoutRight")
        self.scrollAreaRecipeDisplay = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.scrollAreaRecipeDisplay.setWidgetResizable(True)
        self.scrollAreaRecipeDisplay.setObjectName("scrollAreaRecipeDisplay")
        self.scrollAreaRecipeWidgetContents = QtWidgets.QWidget()
        self.scrollAreaRecipeWidgetContents.setGeometry(QtCore.QRect(0, 0, 576, 535))
        self.scrollAreaRecipeWidgetContents.setObjectName("scrollAreaRecipeWidgetContents")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.scrollAreaRecipeWidgetContents)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 581, 541))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutRecipeScrollArea = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayoutRecipeScrollArea.setContentsMargins(10, 10, 10, 10)
        self.verticalLayoutRecipeScrollArea.setObjectName("verticalLayoutRecipeScrollArea")
        self.labelRecipeName = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(24)
        self.labelRecipeName.setFont(font)
        self.labelRecipeName.setObjectName("labelRecipeName")
        self.verticalLayoutRecipeScrollArea.addWidget(self.labelRecipeName)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutRecipeScrollArea.addWidget(self.line)
        self.labelRecipeIngredients = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.labelRecipeIngredients.setFont(font)
        self.labelRecipeIngredients.setObjectName("labelRecipeIngredients")
        self.verticalLayoutRecipeScrollArea.addWidget(self.labelRecipeIngredients)
        self.textBrowserRecipeIngredients = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowserRecipeIngredients.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.textBrowserRecipeIngredients.setFont(font)
        self.textBrowserRecipeIngredients.setObjectName("textBrowserRecipeIngredients")
        self.verticalLayoutRecipeScrollArea.addWidget(self.textBrowserRecipeIngredients)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutRecipeScrollArea.addWidget(self.line_2)
        self.labelRecipeDirections = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.labelRecipeDirections.setFont(font)
        self.labelRecipeDirections.setObjectName("labelRecipeDirections")
        self.verticalLayoutRecipeScrollArea.addWidget(self.labelRecipeDirections)
        self.textBrowserRecipeDirections = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.textBrowserRecipeDirections.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.textBrowserRecipeDirections.setFont(font)
        self.textBrowserRecipeDirections.setObjectName("textBrowserRecipeDirections")
        self.verticalLayoutRecipeScrollArea.addWidget(self.textBrowserRecipeDirections)
        self.scrollAreaRecipeDisplay.setWidget(self.scrollAreaRecipeWidgetContents)
        self.verticalLayoutRight.addWidget(self.scrollAreaRecipeDisplay)
        self.horizontalLayout.addLayout(self.verticalLayoutRight)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRandom = QtGui.QAction(MainWindow)
        self.actionRandom.setObjectName("actionRandom")
        self.menuFile.addAction(self.actionRandom)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "recipie --TESTING--"))
        self.pushButtonRandom.setText(_translate("MainWindow", "Random Recipe"))
        self.labelRecipeName.setText(_translate("MainWindow", "Recipe Name"))
        self.labelRecipeIngredients.setText(_translate("MainWindow", "Ingredients:"))
        self.labelRecipeDirections.setText(_translate("MainWindow", "Directions:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRandom.setText(_translate("MainWindow", "Random"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
