# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goMarkov.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os
class Ui_UniqueWindow(object):
    #-- Tools --
    def Undo(self):
       self.textArea1.undo()

    def Delete(self):
       self.textArea1.clear()

    def Redo(self):
       self.textArea1.redo()
 
    def Cut(self):
       self.textArea1.cut()
 
    def Copy(self):
       self.textArea1.copy()
 
    def Paste(self):
       self.textArea1.paste()

    def new_file(self):
        self.textArea1.clear()
        self.results.clear()

    def open_file(self):
        name = QFileDialog.getOpenFileName()
        if name[0]:
            try:
                file = open(name[0],'r')
                with file:
                    text = file.read()
                self.textArea1.setPlainText(text)
            except Exception as error:
                            raise Exception("There was an error with the file: ".format(error))
   
    def save_file(self):
        information = self.textArea1.toPlainText()        

    def save_fileAs(self):
        information = self.textArea1.toPlainText()
        
        if information:

            path = QFileDialog.getSaveFileName(self.menuFile, 'Save As', os.getenv('HOME'), 'TXT(*.txt)')
            
            try:
                file = open(path[0], 'w')

                with file:    
                    file.write(information)

            except Exception as error:
                raise Exception("There was an error saving the file: ".format(error))

            self.currentFile = path[0]
            self.UniqueWindow.setWindowTitle(file.name.split("/")[-1])
        
        else:
            msg = QMessageBox(self.centralwidget)
            msg.setText("You cannot save an empty file")
            msg.setInformativeText("Please type something before saving")
            msg.setWindowTitle("Warning!")
            msg.exec_()

    def about(self):            
         msg = QMessageBox(self.centralwidget)
         msg.setText("Welcome to GoMarkov")
         msg.setInformativeText("This is a educational project")
         msg.setWindowTitle("GoMarkov")
         msg.exec_()


    #-- Init interface complements
    def setupUi(self, UniqueWindow):
        
        self.centralwidget = QtWidgets.QWidget(UniqueWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.buttonsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.buttonsGroupBox.setMaximumSize(QtCore.QSize(594, 16777215))
        self.buttonsGroupBox.setTitle("")
        self.buttonsGroupBox.setFlat(False)
        self.buttonsGroupBox.setCheckable(False)
        self.buttonsGroupBox.setObjectName("buttonsGroupBox")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttonsGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.chooser1 = QtWidgets.QComboBox(self.buttonsGroupBox)
        self.chooser1.setEditable(False)
        self.chooser1.setObjectName("chooser1")
        self.chooser1.addItem("")
        self.chooser1.addItem("")
        self.chooser1.addItem("")
        self.chooser1.addItem("")
        self.chooser1.addItem("")

        self.horizontalLayout.addWidget(self.chooser1)

        self.chooser2 = QtWidgets.QComboBox(self.buttonsGroupBox)
        self.chooser2.setEditable(False)
        self.chooser2.setObjectName("chooser2")
        self.chooser2.addItem("")
        self.chooser2.addItem("")
        self.chooser2.addItem("")
        self.chooser2.addItem("")
        self.chooser2.addItem("")

        self.horizontalLayout.addWidget(self.chooser2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Stop = QtWidgets.QPushButton(self.buttonsGroupBox)
        self.Stop.setObjectName("Stop")
        self.horizontalLayout.addWidget(self.Stop)
        self.Run = QtWidgets.QPushButton(self.buttonsGroupBox)
        self.Run.setObjectName("Run")
        self.horizontalLayout.addWidget(self.Run)
        self.verticalLayout_3.addWidget(self.buttonsGroupBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textArea1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textArea1.setObjectName("textArea1")
        self.verticalLayout_2.addWidget(self.textArea1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.results.setObjectName("results")
        self.results.setEnabled(False)
        self.verticalLayout_2.addWidget(self.results)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        UniqueWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(UniqueWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menuBar.setObjectName("menuBar")
        
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")

        self.menuGoMarcov = QtWidgets.QMenu(self.menuBar)
        self.menuGoMarcov.setObjectName("menuGoMarcov")

        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")

        UniqueWindow.setMenuBar(self.menuBar)

        self.statusBar = QtWidgets.QStatusBar(UniqueWindow)
        self.statusBar.setObjectName("statusBar")
        UniqueWindow.setStatusBar(self.statusBar)

        #Actions 
        self.actionNew = QtWidgets.QAction(UniqueWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setStatusTip("Open new window")
        self.actionNew.setShortcut("Ctrl+N")

        self.actionRecent = QtWidgets.QAction(UniqueWindow)
        self.actionRecent.setObjectName("actionRecent")

        self.actionExit = QtWidgets.QAction(UniqueWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Ctrl+E")

        self.actionCopy = QtWidgets.QAction(UniqueWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionCopy.triggered.connect(self.Copy)

        self.actionPaste = QtWidgets.QAction(UniqueWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste.setShortcut("Ctrl+P")
        self.actionPaste.triggered.connect(self.Paste)

        self.actionDelete = QtWidgets.QAction(UniqueWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.setShortcut("Supr")
        self.actionDelete.triggered.connect(self.Delete)

        self.actionRedo = QtWidgets.QAction(UniqueWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.setShortcut("Ctrl+Y")
        self.actionRedo.triggered.connect(self.Redo)

        self.actionUndo = QtWidgets.QAction(UniqueWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionUndo.triggered.connect(self.Undo)

        self.actionOpen = QtWidgets.QAction(UniqueWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open_file)
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setStatusTip("Open existing document")

        self.actionNew_tab = QtWidgets.QAction(UniqueWindow)
        self.actionNew_tab.setObjectName("actionNew_tab")
        self.actionNew_tab.setStatusTip("Open new tab")

        self.actionSave = QtWidgets.QAction(UniqueWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip("Save file")
        self.actionSave.triggered.connect(self.save_file)  

        self.actionSave_As = QtWidgets.QAction(UniqueWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.setShortcut("Ctrl+A")
        self.actionSave_As.setStatusTip("Save file")
        self.actionSave_As.triggered.connect(self.save_fileAs) 

        self.actionRun = QtWidgets.QAction(UniqueWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionRun.setShortcut("Ctrl+R")

        self.actionAbout = QtWidgets.QAction(UniqueWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about)

        self.actionCut = QtWidgets.QAction(UniqueWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCut.triggered.connect(self.Cut)

        self.actionSelect_all = QtWidgets.QAction(UniqueWindow)
        self.actionSelect_all.setObjectName("actionSelect_all")

        self.actionToolbar = QtWidgets.QAction(UniqueWindow)
        self.actionToolbar.setObjectName("actionToolbar")

        self.menuFile.addAction(self.actionNew_tab)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecent)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)

        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionSelect_all)

        self.menuView.addAction(self.actionToolbar)

        self.menuGoMarcov.addAction(self.actionRun)

        self.menuHelp.addAction(self.actionAbout)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuGoMarcov.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(UniqueWindow)
        QtCore.QMetaObject.connectSlotsByName(UniqueWindow)

    def retranslateUi(self, UniqueWindow):
        _translate = QtCore.QCoreApplication.translate
        UniqueWindow.setWindowTitle(_translate("UniqueWindow", "GoMarkov"))
        self.chooser1.setItemText(0, _translate("UniqueWindow", "op1"))
        self.chooser1.setItemText(1, _translate("UniqueWindow", "op2"))
        self.chooser1.setItemText(2, _translate("UniqueWindow", "op3"))
        self.chooser1.setItemText(3, _translate("UniqueWindow", "op4"))
        self.chooser1.setItemText(4, _translate("UniqueWindow", "op5"))
        self.chooser2.setItemText(0, _translate("UniqueWindow", "op1"))
        self.chooser2.setItemText(1, _translate("UniqueWindow", "op2"))
        self.chooser2.setItemText(2, _translate("UniqueWindow", "op3"))
        self.chooser2.setItemText(3, _translate("UniqueWindow", "op4"))
        self.chooser2.setItemText(4, _translate("UniqueWindow", "op5"))
        
        self.Stop.setText(_translate("UniqueWindow", "Run"))
        self.Run.setText(_translate("UniqueWindow", "Stop"))
        self.menuFile.setTitle(_translate("UniqueWindow", "File"))
        self.menuEdit.setTitle(_translate("UniqueWindow", "Edit"))
        self.menuView.setTitle(_translate("UniqueWindow", "View"))
        self.menuGoMarcov.setTitle(_translate("UniqueWindow", "GoMarcov"))
        self.menuHelp.setTitle(_translate("UniqueWindow", "Help"))
        self.actionNew.setText(_translate("UniqueWindow", "New"))
        self.actionRecent.setText(_translate("UniqueWindow", "Open Recent"))
        self.actionExit.setText(_translate("UniqueWindow", "Exit"))
        self.actionCopy.setText(_translate("UniqueWindow", "Copy"))
        self.actionPaste.setText(_translate("UniqueWindow", "Paste"))
        self.actionDelete.setText(_translate("UniqueWindow", "Delete"))
        self.actionRedo.setText(_translate("UniqueWindow", "Redo"))
        self.actionUndo.setText(_translate("UniqueWindow", "Undo"))
        self.actionOpen.setText(_translate("UniqueWindow", "Open..."))
        self.actionNew_tab.setText(_translate("UniqueWindow", "New tab"))
        self.actionSave.setText(_translate("UniqueWindow", "Save"))
        self.actionSave_As.setText(_translate("UniqueWindow", "Save As"))
        self.actionRun.setText(_translate("UniqueWindow", "Run"))
        self.actionAbout.setText(_translate("UniqueWindow", "About"))
        self.actionCut.setText(_translate("UniqueWindow", "Cut"))
        self.actionSelect_all.setText(_translate("UniqueWindow", "Select all"))
        self.actionToolbar.setText(_translate("UniqueWindow", "Toolbar"))

class Find(QDialog):
    def __init__(self,parent = None):
        QDialog.__init__(self, parent)
         
        self.initUI()
 
    def initUI(self):
 
        self.lb1 = QLabel("Search for: ",self)
        self.lb1.setStyleSheet("font-size: 15px; ")
        self.lb1.move(10,10)
 
        self.te = QTextEdit(self)
        self.te.move(10,40)
        self.te.resize(250,25)
 
        self.src = QPushButton("Find",self)
        self.src.move(270,40)
 
        self.lb2 = QLabel("Replace all by: ",self)
        self.lb2.setStyleSheet("font-size: 15px; ")
        self.lb2.move(10,80)
 
        self.rp = QTextEdit(self)
        self.rp.move(10,110)
        self.rp.resize(250,25)
 
        self.rpb = QPushButton("Replace",self)
        self.rpb.move(270,110)
 
        self.opt1 = QCheckBox("Case sensitive",self)
        self.opt1.move(10,160)
        self.opt1.stateChanged.connect(self.CS)
         
        self.opt2 = QCheckBox("Whole words only",self)
        self.opt2.move(10,190)
        self.opt2.stateChanged.connect(self.WWO)
 
        self.close = QPushButton("Close",self)
        self.close.move(270,220)
        self.close.clicked.connect(self.Close)
         
         
        self.setGeometry(300,300,360,250)
 
    def CS(self, state):
        global cs
 
        if state == QtCore.Qt.Checked:
            cs = True
        else:
            cs = False
 
    def WWO(self, state):
        global wwo
        print(wwo)
 
        if state == QtCore.Qt.Checked:
            wwo = True
        else:
            wwo = False
 
    def Close(self):
        self.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UniqueWindow = QtWidgets.QMainWindow()
    ui = Ui_UniqueWindow()
    ui.setupUi(UniqueWindow)
    UniqueWindow.show()
    sys.exit(app.exec_())

