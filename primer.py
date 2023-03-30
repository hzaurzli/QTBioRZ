# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'primer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Bio import SeqIO

class Primer_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 614)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(390, 560, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculation)

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(310, 100, 231, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 20, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 310, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 450, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(450, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(350, 370, 191, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("Maximum amplicon length (bp): 0")

        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(310, 490, 101, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setPlaceholderText("Mismatch base (bp): 0")

        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(440, 490, 101, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setPlaceholderText("Indel base (bp): 0")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(390, 60, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 70, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit_4 = QtWidgets.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 120, 261, 51))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 230, 261, 51))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 290, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 340, 251, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 490, 251, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 400, 131, 41))
        self.pushButton_2.clicked.connect(self.read_file1)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 560, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.read_file2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Run"))
        self.label.setText(_translate("Form", "In silico PCR"))
        self.label_2.setText(_translate("Form", "Maximum \"amplicon\" length"))
        self.label_3.setText(_translate("Form", "Mismatch base"))
        self.label_4.setText(_translate("Form", "Indel base"))
        self.label_5.setText(_translate("Form", "Status"))
        self.label_6.setText(_translate("Form", "Forward primer, 5\' → 3\'"))
        self.label_7.setText(_translate("Form", "Reverse primer, 5\' → 3\'"))
        self.label_8.setText(_translate("Form", "Query fa (Genome fasta)"))
        self.label_9.setText(_translate("Form", "Result file"))
        self.pushButton_2.setText(_translate("Form", "Choose"))
        self.pushButton_3.setText(_translate("Form", "Choose"))


    def read_file1(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose file', '')[0]
        print(openfile_name)
        self.textBrowser_2.setText(openfile_name)

    def read_file2(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose file", "./")[0]
        print(openfile_name)
        self.textBrowser_3.setText(openfile_name)

    def calculation(self):
        try:
            fasta = self.textBrowser_2.toPlainText()
            out = self.textBrowser_3.toPlainText()
            forward = self.textEdit_4.toPlainText()
            reverse = self.textEdit_5.toPlainText()
            length = self.textEdit.toPlainText()
            mismatch = self.textEdit_2.toPlainText()
            indel = self.textEdit_3.toPlainText()

            path = os.path.dirname(out)
            file = os.path.basename(out)
            print(fasta, out, forward, reverse,length,mismatch,indel,path,file)

            def is_fasta(filename):
                with open(filename, "r") as handle:
                    fasta = SeqIO.parse(handle, "fasta")
                    return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file

            if any([len(fasta), len(out), len(forward), len(reverse)]) == False:
                QMessageBox.warning(self, "warning", "Please add correct file path or correct parameters!", QMessageBox.Cancel)
            else:
                if is_fasta(fasta) == False:
                    QMessageBox.critical(self, "error", "check fasta file format!")
                else:
                    if len(length) == 0:
                        length = 0
                    else:
                        length = length

                    if len(mismatch) == 0:
                        mismatch = 0
                    else:
                        mismatch = mismatch

                    if len(indel) == 0:
                        indel = 0
                    else:
                        indel = indel

                    self.textBrowser.setText('Running! please wait')
                    QApplication.processEvents()  # 逐条打印状态

                    os.popen(r".\perl\bin\perl.exe .\perl\in_silico_PCR.pl -s %s -a %s -b %s -l %s -m %s -i %s > %s 2> %s"
                             % (fasta, forward, reverse, length, mismatch, indel, path + "/position-" + file, out))

                    self.textBrowser.setText('Finished!!!')

        except:
            QMessageBox.critical(self, "error", "check fasta file format!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Primer_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
