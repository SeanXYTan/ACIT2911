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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelRecipieLogo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRecipieLogo.sizePolicy().hasHeightForWidth())
        self.labelRecipieLogo.setSizePolicy(sizePolicy)
        self.labelRecipieLogo.setMaximumSize(QtCore.QSize(150, 75))
        self.labelRecipieLogo.setText("")
        self.labelRecipieLogo.setPixmap(QtGui.QPixmap(".\\recipie_test\\../../../image/RecipieLogo.png"))
        self.labelRecipieLogo.setScaledContents(True)
        self.labelRecipieLogo.setObjectName("labelRecipieLogo")
        self.horizontalLayout_2.addWidget(self.labelRecipieLogo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutLeft = QtWidgets.QVBoxLayout()
        self.verticalLayoutLeft.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayoutLeft.setContentsMargins(10, 10, 10, 10)
        self.verticalLayoutLeft.setObjectName("verticalLayoutLeft")
        self.pushButtonRandom = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRandom.sizePolicy().hasHeightForWidth())
        self.pushButtonRandom.setSizePolicy(sizePolicy)
        self.pushButtonRandom.setMinimumSize(QtCore.QSize(110, 25))
        self.pushButtonRandom.setMaximumSize(QtCore.QSize(115, 30))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.pushButtonRandom.setFont(font)
        self.pushButtonRandom.setObjectName("pushButtonRandom")
        self.verticalLayoutLeft.addWidget(self.pushButtonRandom, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayoutLeft.addItem(spacerItem2)
        self.verticalLayoutLeft.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayoutLeft)
        self.verticalLayoutRecipeScrollArea = QtWidgets.QVBoxLayout()
        self.verticalLayoutRecipeScrollArea.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayoutRecipeScrollArea.setContentsMargins(10, 10, 10, 10)
        self.verticalLayoutRecipeScrollArea.setObjectName("verticalLayoutRecipeScrollArea")
        self.labelRecipeName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(24)
        self.labelRecipeName.setFont(font)
        self.labelRecipeName.setObjectName("labelRecipeName")
        self.verticalLayoutRecipeScrollArea.addWidget(self.labelRecipeName)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutRecipeScrollArea.addWidget(self.line)
        self.labelRecipeIngredients = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.labelRecipeIngredients.setFont(font)
        self.labelRecipeIngredients.setObjectName("labelRecipeIngredients")
        self.verticalLayoutRecipeScrollArea.addWidget(self.labelRecipeIngredients)
        self.textBrowserRecipeIngredients = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserRecipeIngredients.setMinimumSize(QtCore.QSize(300, 100))
        self.textBrowserRecipeIngredients.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.textBrowserRecipeIngredients.setFont(font)
        self.textBrowserRecipeIngredients.setObjectName("textBrowserRecipeIngredients")
        self.verticalLayoutRecipeScrollArea.addWidget(self.textBrowserRecipeIngredients)
        self.labelRecipeDirections = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.labelRecipeDirections.setFont(font)
        self.labelRecipeDirections.setObjectName("labelRecipeDirections")
        self.verticalLayoutRecipeScrollArea.addWidget(self.labelRecipeDirections)
        self.textBrowserRecipeDirections = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserRecipeDirections.setMinimumSize(QtCore.QSize(300, 100))
        self.textBrowserRecipeDirections.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        self.textBrowserRecipeDirections.setFont(font)
        self.textBrowserRecipeDirections.setObjectName("textBrowserRecipeDirections")
        self.verticalLayoutRecipeScrollArea.addWidget(self.textBrowserRecipeDirections)
        self.verticalLayoutRecipeScrollArea.setStretch(3, 1)
        self.verticalLayoutRecipeScrollArea.setStretch(5, 1)
        self.horizontalLayout.addLayout(self.verticalLayoutRecipeScrollArea)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)
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
        self.label.setText(_translate("MainWindow", "Welcome to Recipie Beta, please hit \'Random Recipe to try it out!"))
        self.pushButtonRandom.setToolTip(_translate("MainWindow", "Get A Random Recipe"))
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
