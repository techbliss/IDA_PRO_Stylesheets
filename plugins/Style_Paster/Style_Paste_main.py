__author__ = 'Storm Shadow'

import sys
import re
import os
mypath = os.path.dirname(__file__)
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel, QSizePolicy
from PyQt5.QtCore import QFile, QIODevice, Qt, QTextStream, QUrl,  QCoreApplication, QFileInfo
from PyQt5.QtCore import *
import iconss
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_StyleSheetEditor(object):
    def setupUi(self, StyleSheetEditor):
        # set app icon
        app_icon = QtGui.QIcon()
        self.filename = ""
        app_icon.addFile(':/iconsstyle/iconss.png', QtCore.QSize(16,16))
        StyleSheetEditor.setWindowIcon( app_icon)
        self.ui = Ui_StyleSheetEditor()
        StyleSheetEditor.setObjectName(_fromUtf8("StyleSheetEditor"))
        StyleSheetEditor.resize(445, 289)
        self.gridlayout = QGridLayout(StyleSheetEditor)
#        self.gridlayout.setMargin(9)
 #       self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
#        self.hboxlayout.setMargin(0)
 #       self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
   #    spacerItem = QtWidgets.QSpacerItem(321, 20, QtWidgets.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
#        self.hboxlayout.addItem(spacerItem)
        self.saveButton = QtWidgets.QPushButton(StyleSheetEditor)
        self.saveButton.setEnabled(True)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.hboxlayout.addWidget(self.saveButton)
        self.applyButton = QtWidgets.QPushButton(StyleSheetEditor)
        self.applyButton.setEnabled(True)
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.openButton = QtWidgets.QPushButton(StyleSheetEditor)
        self.openButton.setEnabled(True)
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.hboxlayout.addWidget(self.openButton)
        self.hboxlayout.addWidget(self.applyButton)
        self.gridlayout.addLayout(self.hboxlayout, 2, 0, 1, 5)

        self.styleTextEdit = QtWidgets.QTextEdit(StyleSheetEditor)
        self.styleTextEdit.setObjectName(_fromUtf8("styleTextEdit"))
        self.gridlayout.addWidget(self.styleTextEdit, 1, 0, 1, 5)
        self.label_8 = QtWidgets.QLabel(StyleSheetEditor)

        self.gridlayout.addWidget(self.label_8, 0, 1, 1, 1)
        self.filename = ""

        self.retranslateUi(StyleSheetEditor)
        QtCore.QMetaObject.connectSlotsByName(StyleSheetEditor)

    def retranslateUi(self, StyleSheetEditor):
        StyleSheetEditor.setWindowTitle(_translate("StyleSheetEditor", "StyleSheet Paster", None))
        self.saveButton.setText(_translate("StyleSheetEditor", "&Save", None))
        self.applyButton.setText(_translate("StyleSheetEditor", "&Apply", None))
        self.openButton.setText(_translate("StyleSheetEditor", "&Open", None))
       # self.label_8.setText(_translate("StyleSheetEditor", "By Zadow", None))
        self.applyButton.clicked.connect(self.apply)
        self.saveButton.clicked.connect(self.savefile)
        self.openButton.clicked.connect(self.open)




    def apply(self):
        QtWidgets.qApp.setStyleSheet(ui.styleTextEdit.toPlainText())

    def open(self):
        self.path = QtCore.QFileInfo(self.filename).path()

        # Get filename and show only .writer files
        (self.filename, _) = \
            QtWidgets.QFileDialog.getOpenFileName(self.styleTextEdit,
                                                  'Open File', self.path,
                                                  'Python Files (*.css *.qss))', '')

        if self.filename:
            with open(self.filename, 'r') as self.file:
                self.styleTextEdit.setText(self.file.read())
        os.chdir(str(self.path))




    def savefile(self):
        self.path = QtCore.QFileInfo(self.filename).path()
        (self.filename, _) = \
            QtWidgets.QFileDialog.getSaveFileName(self.styleTextEdit, 'Save as'
                , self.path, 'Python Files (*.css *.qss)')
        if self.filename:
            self.savetext(self.filename)
        os.chdir(str(self.path))

    def savetext(self, fileName):
        textout = self.styleTextEdit.toPlainText()
        file = QtCore.QFile(fileName)
        if file.open(QtCore.QIODevice.WriteOnly):
            QtCore.QTextStream(file) << textout
        else:
            QtWidgets.QMessageBox.information(self.vindu,
                    'Unable to open file', file.errorString())
        os.chdir(str(self.path))

import sys
#app = QtWidgets.QApplication.instance()
#if not app:
    #app = QtWidgets.QApplication([])
StyleSheetEditor = QtWidgets.QWidget()
ui = Ui_StyleSheetEditor()
ui.setupUi(StyleSheetEditor)
StyleSheetEditor.show()
print "helllllllllllllllllllllllooooooooooooooooooooo"
#app.exec_()

