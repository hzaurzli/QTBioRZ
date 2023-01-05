import time,os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import delect_phage_dots
import smallrunze
from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio.Blast.Applications import NcbiblastnCommandline


class pages(smallrunze.Ui_MainWindow,QMainWindow):
    def __init__(self, parent=None):
        super(pages, self).__init__()
        self.setupUi(self)

        self.actionCount_dots.triggered.connect(self.dots)

        self.textEdit_13.setPlaceholderText("E value: 0.000001")
        self.textEdit_10.setPlaceholderText("Format: 6")

        self.textEdit_8.setPlaceholderText("E value: 0.000001")
        self.textEdit_7.setPlaceholderText("Format: 6")

        self.actionBLASTn.triggered.connect(self.display1)
        self.actionBLASTp.triggered.connect(self.display2)

        self.pushButton.clicked.connect(self.read_file1)
        self.pushButton_5.clicked.connect(self.read_file2)
        self.pushButton_6.clicked.connect(self.read_file3)
        self.pushButton_11.clicked.connect(self.read_file7)

        self.pushButton_7.clicked.connect(self.read_file4)
        self.pushButton_8.clicked.connect(self.read_file5)
        self.pushButton_9.clicked.connect(self.read_file6)
        self.pushButton_10.clicked.connect(self.read_file8)

        self.pushButton_3.clicked.connect(self.blastn)
        self.pushButton_4.clicked.connect(self.blastp)


    def dots(self):
        self.winTable = delect_phage_dots.MyClass()
        self.winTable.show()


    def display1(self):
        self.stackedWidget.setCurrentIndex(0)

    def display2(self):
        self.stackedWidget.setCurrentIndex(1)

    def read_file1(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose figures', '')[0]
        print(openfile_name)
        self.textBrowser_3.setText(openfile_name)

    def read_file2(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose figures', '')[0]
        print(openfile_name)
        self.textBrowser_2.setText(openfile_name)

    def read_file3(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose figures", "./")[0]
        print(openfile_name)
        self.textBrowser.setText(openfile_name)

    def read_file7(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose figures", "./")[0]
        print(openfile_name)
        self.textBrowser_10.setText(openfile_name)


    def read_file4(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose figures', '')[0]
        print(openfile_name)
        self.textBrowser_4.setText(openfile_name)

    def read_file5(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose figures', '')[0]
        print(openfile_name)
        self.textBrowser_5.setText(openfile_name)

    def read_file6(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose figures","./")[0]
        print(openfile_name)
        self.textBrowser_6.setText(openfile_name)

    def read_file8(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose figures", "./")[0]
        print(openfile_name)
        self.textBrowser_9.setText(openfile_name)

    def blastn(self):
        self.textBrowser_7.setText('Running! please wait')
        QApplication.processEvents()  # 逐条打印状态

        ref = self.textBrowser_4.toPlainText()
        query = self.textBrowser_5.toPlainText()
        blastdb = self.textBrowser_9.toPlainText()
        out = self.textBrowser_6.toPlainText()
        evalue = self.textEdit_8.toPlainText()
        format = self.textEdit_7.toPlainText()
        print(ref,query,blastdb,out,evalue,format)

        path = os.getcwd()
        path = '/'.join(path.split('\\'))

        if len(evalue) == 0:
            evalue = 0.000001
        else:
            evalue = evalue

        if len(format) == 0:
            format = 6
        else:
            format = format

        makedb = NcbimakeblastdbCommandline(path + "/blast-BLAST_VERSION+/bin/makeblastdb.exe",
                                            dbtype = 'nucl',
                                            input_file = ref,
                                            out = blastdb)
        stdout,stderr = makedb()

        blastn = NcbiblastnCommandline(path + "/blast-BLAST_VERSION+/bin/blastn.exe",
                                       query = query,
                                       db = blastdb,
                                       outfmt = format,
                                       evalue= float(evalue),
                                       out = out)

        stdout,stderr = blastn()
        self.textBrowser_7.setText('Finished!!!')


    def blastp(self):
        self.textBrowser_8.setText('Running! please wait')
        QApplication.processEvents()  # 逐条打印状态

        ref = self.textBrowser_3.toPlainText()
        query = self.textBrowser_2.toPlainText()
        blastdb = self.textBrowser.toPlainText()
        out = self.textBrowser_10.toPlainText()
        evalue = self.textEdit_13.toPlainText()
        format = self.textEdit_10.toPlainText()
        print(ref,query,blastdb,out,evalue,format)

        path = os.getcwd()
        path = '/'.join(path.split('\\'))

        if len(evalue) == 0:
            evalue = 0.000001
        else:
            evalue = evalue

        if len(format) == 0:
            format = 6
        else:
            format = format

        makedb = NcbimakeblastdbCommandline(path + "/blast-BLAST_VERSION+/bin/makeblastdb.exe",
                                            dbtype = 'prot',
                                            input_file = ref,
                                            out = blastdb)
        stdout,stderr = makedb()

        blastn = NcbiblastnCommandline(path + "/blast-BLAST_VERSION+/bin/blastp.exe",
                                       query = query,
                                       db = blastdb,
                                       outfmt = format,
                                       evalue= float(evalue),
                                       out = out)

        stdout,stderr = blastp()
        self.textBrowser_8.setText('Finished!!!')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = pages()
    Main_Window.show()
    sys.exit(app.exec_())

