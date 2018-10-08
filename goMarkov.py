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
import os, sys
from colorama import *

class Ui_UniqueWindow(object):
    #-- program functions
    def defaultFormat(self):
       comentary = "%"
       dheader = "GoMarkov Project \n \n" 
       symbols = "#symbols abcdefghijklmnopqrstuvwxyz0123456789 \n"
       variables = "#vars wxyz \n"
       markers = "#markers αβγδ \n"
       self.textArea1.setPlainText(dheader+symbols+variables+markers)

    def duplicarHilera(self,chain):
        chain = chain * 2
        return chain

    def esPalindromo(chain):
        standart = str(chain).lower().replace(' ','')
        return standart == standart[::-1]

    def sumaBinarios(a,b):
        return bin(int(a, 2) + int(b, 2))

    def multBinarios(a,b):
        return bin(int(a, 2) * int(b, 2))


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
        data = self.textArea1.toPlainText()
        if data:
            path = QFileDialog.getSaveFileName(self.menuFile, 'Save As', os.getenv('HOME'), 'txt(*.txt)')    
            try:
                file = open(path[0], 'w', encoding='utf-8')
                with file:    
                    file.write(data) 
            except Exception as error:
                raise Exception("There was an error saving the file: ".format(error))
            self.currentFile = path[0]
            self.UniqueWindow.setWindowTitle(file.name.split("/")[-1]) 
        else:
            msg = QMessageBox(self.centralwidget)
            msg.setText("You cannot save an empty file")
            msg.setInformativeText("Please write something before saving")
            msg.setWindowTitle("Warning!")
            msg.exec_()   

    def save_fileAs(self):
        data = self.textArea1.toPlainText()
        if data:
            path = QFileDialog.getSaveFileName(self.menuFile, 'Save As', os.getenv('HOME'), 'txt(*.txt)')    
            try:
                file = open(path[0], 'w', encoding='utf-8')
                with file:    
                    file.write(data)
            except Exception as error:
                raise Exception("There was an error saving the file: ".format(error))
            self.currentFile = path[0]
            self.UniqueWindow.setWindowTitle(file.name.split("/")[-1]) 
        else:
            msg = QMessageBox(self.centralwidget)
            msg.setText("You cannot save an empty file")
            msg.setInformativeText("Please write something before saving")
            msg.setWindowTitle("Warning!")
            msg.exec_()

    def about(self):            
         msg = QMessageBox(self.centralwidget)
         msg.setText("Welcome to GoMarkov")
         msg.setInformativeText("This is a educational project")
         msg.setWindowTitle("GoMarkov")
         msg.exec_()

    def exitApp(self):
        sys.exit()     

    def putAlfa(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B1")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)
    
    def putBeta(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B2")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)

    def putGamma(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B3")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)

    def putDelta(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B4")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)

    def putEpsilon(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B5")

    def putDseta(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B6")

    def putEta(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B7")

    def putTheta(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B8")

    def putIota(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03B9")

    def putKappa(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03BA")
    
    def putLambdaMin(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03BB")
    
    def putLambdaMay(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u039B")

    def putMy(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03BC")
    
    def putNy(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03BD")
    
    def putXi(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03BE")

    def putOmicron(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03BF")

    def putPi(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C0")

    def putRho(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C1")
    
    def putSigma(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C3")
    
    def putTau(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C4")

    def putYpsilon(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C5")

    def putFi(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C6")
    
    def putJi(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C7")

    def putPsi(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C8")
    
    def putOmega(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u03C9")

    def putArrow(self):
        cursor = self.textArea1.textCursor()
        self.textArea1.insertPlainText("\u2192")

    def setupUi(self, UniqueWindow):
        UniqueWindow.setObjectName("UniqueWindow")
        UniqueWindow.resize(762, 585)
        UniqueWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(UniqueWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textArea1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textArea1.sizePolicy().hasHeightForWidth())
        self.textArea1.setSizePolicy(sizePolicy)
        self.textArea1.setObjectName("textArea1")
        self.gridLayout.addWidget(self.textArea1, 2, 0, 1, 6)
        self.groupPalette = QtWidgets.QGroupBox(self.centralwidget)
        self.groupPalette.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupPalette.setObjectName("groupPalette")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupPalette)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.alfabtn = QtWidgets.QPushButton(self.groupPalette)
        self.alfabtn.setObjectName("alfabtn")
        self.gridLayout_2.addWidget(self.alfabtn, 0, 0, 1, 1)
        self.dsetabtn = QtWidgets.QPushButton(self.groupPalette)
        self.dsetabtn.setObjectName("dsetabtn")
        self.gridLayout_2.addWidget(self.dsetabtn, 1, 0, 1, 1)
        self.omicronbtn = QtWidgets.QPushButton(self.groupPalette)
        self.omicronbtn.setObjectName("omicronbtn")
        self.gridLayout_2.addWidget(self.omicronbtn, 3, 0, 1, 1)
        self.lambdaminbtn = QtWidgets.QPushButton(self.groupPalette)
        self.lambdaminbtn.setObjectName("lambdaminbtn")
        self.gridLayout_2.addWidget(self.lambdaminbtn, 2, 0, 1, 1)
        self.etabtn = QtWidgets.QPushButton(self.groupPalette)
        self.etabtn.setObjectName("etabtn")
        self.gridLayout_2.addWidget(self.etabtn, 1, 1, 1, 1)
        self.ypsilonbtn = QtWidgets.QPushButton(self.groupPalette)
        self.ypsilonbtn.setObjectName("ypsilonbtn")
        self.gridLayout_2.addWidget(self.ypsilonbtn, 4, 0, 1, 1)
        self.fibtn = QtWidgets.QPushButton(self.groupPalette)
        self.fibtn.setObjectName("fibtn")
        self.gridLayout_2.addWidget(self.fibtn, 4, 1, 1, 1)
        self.pibtn = QtWidgets.QPushButton(self.groupPalette)
        self.pibtn.setObjectName("pibtn")
        self.gridLayout_2.addWidget(self.pibtn, 3, 1, 1, 1)
        self.lambdamaybtn = QtWidgets.QPushButton(self.groupPalette)
        self.lambdamaybtn.setObjectName("lambdamaybtn")
        self.gridLayout_2.addWidget(self.lambdamaybtn, 2, 1, 1, 1)
        self.rhobtn = QtWidgets.QPushButton(self.groupPalette)
        self.rhobtn.setObjectName("rhobtn")
        self.gridLayout_2.addWidget(self.rhobtn, 3, 2, 1, 1)
        self.thetabtn = QtWidgets.QPushButton(self.groupPalette)
        self.thetabtn.setObjectName("thetabtn")
        self.gridLayout_2.addWidget(self.thetabtn, 1, 2, 1, 1)
        self.mybtn = QtWidgets.QPushButton(self.groupPalette)
        self.mybtn.setObjectName("mybtn")
        self.gridLayout_2.addWidget(self.mybtn, 2, 2, 1, 1)
        self.betabtn = QtWidgets.QPushButton(self.groupPalette)
        self.betabtn.setObjectName("betabtn")
        self.gridLayout_2.addWidget(self.betabtn, 0, 1, 1, 1)
        self.jibtn = QtWidgets.QPushButton(self.groupPalette)
        self.jibtn.setObjectName("jibtn")
        self.gridLayout_2.addWidget(self.jibtn, 4, 2, 1, 1)
        self.gammabtn = QtWidgets.QPushButton(self.groupPalette)
        self.gammabtn.setObjectName("gammabtn")
        self.gridLayout_2.addWidget(self.gammabtn, 0, 2, 1, 1)
        self.deltabtn = QtWidgets.QPushButton(self.groupPalette)
        self.deltabtn.setObjectName("deltabtn")
        self.gridLayout_2.addWidget(self.deltabtn, 0, 3, 1, 1)
        self.iotabtn = QtWidgets.QPushButton(self.groupPalette)
        self.iotabtn.setObjectName("iotabtn")
        self.gridLayout_2.addWidget(self.iotabtn, 1, 3, 1, 1)
        self.psibtn = QtWidgets.QPushButton(self.groupPalette)
        self.psibtn.setObjectName("psibtn")
        self.gridLayout_2.addWidget(self.psibtn, 4, 3, 1, 1)
        self.nybtn = QtWidgets.QPushButton(self.groupPalette)
        self.nybtn.setObjectName("nybtn")
        self.gridLayout_2.addWidget(self.nybtn, 2, 3, 1, 1)
        self.sigmabtn = QtWidgets.QPushButton(self.groupPalette)
        self.sigmabtn.setObjectName("sigmabtn")
        self.gridLayout_2.addWidget(self.sigmabtn, 3, 3, 1, 1)
        self.epsilonbtn = QtWidgets.QPushButton(self.groupPalette)
        self.epsilonbtn.setObjectName("epsilonbtn")
        self.gridLayout_2.addWidget(self.epsilonbtn, 0, 4, 1, 1)
        self.taubtn = QtWidgets.QPushButton(self.groupPalette)
        self.taubtn.setObjectName("taubtn")
        self.gridLayout_2.addWidget(self.taubtn, 3, 4, 1, 1)
        self.omegabtn = QtWidgets.QPushButton(self.groupPalette)
        self.omegabtn.setObjectName("omegabtn")
        self.gridLayout_2.addWidget(self.omegabtn, 4, 4, 1, 1)
        self.kappabtn = QtWidgets.QPushButton(self.groupPalette)
        self.kappabtn.setObjectName("kappabtn")
        self.gridLayout_2.addWidget(self.kappabtn, 1, 4, 1, 1)
        self.xibtn = QtWidgets.QPushButton(self.groupPalette)
        self.xibtn.setObjectName("xibtn")
        self.gridLayout_2.addWidget(self.xibtn, 2, 4, 1, 1)
        self.arrowbtn = QtWidgets.QPushButton(self.groupPalette)
        self.arrowbtn.setObjectName("arrowbtn")
        self.gridLayout_2.addWidget(self.arrowbtn, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.groupPalette, 2, 7, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 6)
        self.textArea2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textArea2.setObjectName("textArea2")
        self.gridLayout.addWidget(self.textArea2, 4, 0, 1, 6)
        self.Run = QtWidgets.QPushButton(self.centralwidget)
        self.Run.setObjectName("Run")
        self.gridLayout.addWidget(self.Run, 0, 1, 1, 1)
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setObjectName("Steps")
        self.gridLayout.addWidget(self.Stop, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        UniqueWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(UniqueWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 762, 21))
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
        self.actionExit.triggered.connect(self.exitApp)

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

        self.actionStep = QtWidgets.QAction(UniqueWindow)
        self.actionStep.setObjectName("actionStep")
        self.actionStep.setShortcut("Ctrl+T")

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
        self.menuGoMarcov.addAction(self.actionStep)
        self.menuHelp.addAction(self.actionAbout)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuGoMarcov.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

         #Pallete events:
        self.alfabtn.clicked.connect(self.putAlfa)
        self.betabtn.clicked.connect(self.putBeta)
        self.gammabtn.clicked.connect(self.putGamma)
        self.deltabtn.clicked.connect(self.putDelta)
        self.epsilonbtn.clicked.connect(self.putEpsilon)
        self.dsetabtn.clicked.connect(self.putDseta)
        self.etabtn.clicked.connect(self.putEta)
        self.thetabtn.clicked.connect(self.putTheta)
        self.iotabtn.clicked.connect(self.putIota)
        self.kappabtn.clicked.connect(self.putKappa)
        self.lambdaminbtn.clicked.connect(self.putLambdaMin)
        self.lambdamaybtn.clicked.connect(self.putLambdaMay)
        self.mybtn.clicked.connect(self.putMy)
        self.nybtn.clicked.connect(self.putNy)
        self.xibtn.clicked.connect(self.putXi)
        self.omicronbtn.clicked.connect(self.putOmicron)
        self.pibtn.clicked.connect(self.putPi)
        self.rhobtn.clicked.connect(self.putRho)
        self.sigmabtn.clicked.connect(self.putSigma)
        self.taubtn.clicked.connect(self.putTau)
        self.ypsilonbtn.clicked.connect(self.putYpsilon)
        self.fibtn.clicked.connect(self.putFi)
        self.jibtn.clicked.connect(self.putJi)
        self.psibtn.clicked.connect(self.putPsi)
        self.omegabtn.clicked.connect(self.putOmega)
        self.arrowbtn.clicked.connect(self.putArrow)

        self.retranslateUi(UniqueWindow)
        QtCore.QMetaObject.connectSlotsByName(UniqueWindow)

    def retranslateUi(self, UniqueWindow):
        _translate = QtCore.QCoreApplication.translate
        UniqueWindow.setWindowTitle(_translate("UniqueWindow", "GoMarkov"))
        UniqueWindow.setWindowIcon(QtGui.QIcon("icons/geek.png"))
        self.groupPalette.setTitle(_translate("UniqueWindow", "Symbols"))
        self.alfabtn.setText(_translate("UniqueWindow", "α"))
        self.dsetabtn.setText(_translate("UniqueWindow", "ζ"))
        self.omicronbtn.setText(_translate("UniqueWindow", "ο"))
        self.lambdaminbtn.setText(_translate("UniqueWindow", "λ"))
        self.etabtn.setText(_translate("UniqueWindow", "η"))
        self.ypsilonbtn.setText(_translate("UniqueWindow", "υ"))
        self.fibtn.setText(_translate("UniqueWindow", "φ"))
        self.pibtn.setText(_translate("UniqueWindow", "π"))
        self.lambdamaybtn.setText(_translate("UniqueWindow", "Λ"))
        self.rhobtn.setText(_translate("UniqueWindow", "ρ"))
        self.thetabtn.setText(_translate("UniqueWindow", "θ"))
        self.mybtn.setText(_translate("UniqueWindow", "μ"))
        self.betabtn.setText(_translate("UniqueWindow", "β"))
        self.jibtn.setText(_translate("UniqueWindow", "χ"))
        self.gammabtn.setText(_translate("UniqueWindow", "γ"))
        self.deltabtn.setText(_translate("UniqueWindow", "δ"))
        self.iotabtn.setText(_translate("UniqueWindow", "ι"))
        self.psibtn.setText(_translate("UniqueWindow", "ψ"))
        self.nybtn.setText(_translate("UniqueWindow", "ν"))
        self.sigmabtn.setText(_translate("UniqueWindow", "σ"))
        self.epsilonbtn.setText(_translate("UniqueWindow", "ε"))
        self.taubtn.setText(_translate("UniqueWindow", "τ"))
        self.omegabtn.setText(_translate("UniqueWindow", "ω"))
        self.kappabtn.setText(_translate("UniqueWindow", "κ"))
        self.xibtn.setText(_translate("UniqueWindow", "ξ"))
        self.arrowbtn.setText(_translate("UniqueWindow", "→"))
        self.Run.setText(_translate("UniqueWindow", "Run"))
        self.Stop.setText(_translate("UniqueWindow", "Step by step"))
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
        self.actionStep.setText(_translate("UniqueWindow", "StepByStep"))
        self.actionAbout.setText(_translate("UniqueWindow", "About"))
        self.actionCut.setText(_translate("UniqueWindow", "Cut"))
        self.actionSelect_all.setText(_translate("UniqueWindow", "Select all"))
        self.actionToolbar.setText(_translate("UniqueWindow", "Toolbar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UniqueWindow = QtWidgets.QMainWindow()
    ui = Ui_UniqueWindow()
    ui.setupUi(UniqueWindow)
    ui.defaultFormat()
    UniqueWindow.show()
    sys.exit(app.exec_())

