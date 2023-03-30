import time,os
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import delect_phage_dots
import activity
import lysogen
import smallrunze
from primer import Primer_Form
from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio import SeqIO

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)

    def load_data(self, sp):
        for i in range(1, 11):              #模拟主程序加载过程
            time.sleep(2)                   # 加载数据
            sp.showMessage("loading... {0}%".format(i * 10), QtCore.Qt.AlignHCenter |QtCore.Qt.AlignBottom, QtCore.Qt.black)
            QtWidgets.qApp.processEvents()  # 允许主进程处理事件


class pages(smallrunze.Ui_MainWindow,QMainWindow):
    def __init__(self, parent=None):
        super(pages, self).__init__()
        self.setupUi(self)

        self.actionCount_dots.triggered.connect(self.dots)
        self.actionPeptideActivity.triggered.connect(self.activity)
        self.actionLysogen.triggered.connect(self.lysogen)
        self.actionPrimer.triggered.connect(self.primer)

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

    ## click to new window delect_phage_dots,MyClass() is object in delect_phage_dots.py
    def dots(self):
        self.winTable = delect_phage_dots.MyClass()
        self.winTable.show()


    ## click to new window activity,Activity_Form() is object in activity.py
    def activity(self):
        self.winTable = activity.Activity_Form()
        self.winTable.show()


    ## click to new window lysogen,Lysogen_Form() is object in lysogen.py
    def lysogen(self):
        self.winTable = lysogen.Lysogen_Form()
        self.winTable.show()

    ## click to new window primer,Primer_Form() is object in primer.py
    def primer(self):
        self.form = QtWidgets.QMainWindow()
        self.ui = Primer_Form()
        self.ui.setupUi(self.form)
        self.form.show()


        # stacked widget page position
    def display1(self):
        self.stackedWidget.setCurrentIndex(0)

    # stacked widget page position
    def display2(self):
        self.stackedWidget.setCurrentIndex(1)

    def read_file1(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose file', '')[0]
        print(openfile_name)
        self.textBrowser_3.setText(openfile_name)

    def read_file2(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose file', '')[0]
        print(openfile_name)
        self.textBrowser_2.setText(openfile_name)

    def read_file3(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose file", "./")[0]
        print(openfile_name)
        self.textBrowser.setText(openfile_name)

    def read_file7(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose file", "./")[0]
        print(openfile_name)
        self.textBrowser_10.setText(openfile_name)


    def read_file4(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose file', '')[0]
        print(openfile_name)
        self.textBrowser_4.setText(openfile_name)

    def read_file5(self):
        openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, 'choose file', '')[0]
        print(openfile_name)
        self.textBrowser_5.setText(openfile_name)

    def read_file6(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose file","./")[0]
        print(openfile_name)
        self.textBrowser_6.setText(openfile_name)

    def read_file8(self):
        openfile_name = QtWidgets.QFileDialog.getSaveFileName(self, "choose file", "./")[0]
        print(openfile_name)
        self.textBrowser_9.setText(openfile_name)


    def blastn(self):
        ## toPlainText read path of files
        ref = self.textBrowser_4.toPlainText()
        query = self.textBrowser_5.toPlainText()
        blastdb = self.textBrowser_9.toPlainText()
        out = self.textBrowser_6.toPlainText()
        evalue = self.textEdit_8.toPlainText()
        format = self.textEdit_7.toPlainText()
        print(ref,query,blastdb,out,evalue,format)

        path = os.getcwd()
        path = '/'.join(path.split('\\'))

        def is_fasta(filename):
            with open(filename, "r") as handle:
                fasta = SeqIO.parse(handle, "fasta")
                return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file


        if any([len(ref),len(query),len(blastdb),len(format)]) == False:
            QMessageBox.warning(self, "warning", "Please add correct file path!", QMessageBox.Cancel)
        else:
            if is_fasta(ref) == False or is_fasta(query) == False:
                QMessageBox.critical(self, "error", "check fasta file format!")
            else:
                if len(evalue) == 0:
                    evalue = 0.000001
                else:
                    evalue = evalue

                if len(format) == 0:
                    format = 6
                else:
                    format = format

                self.textBrowser_7.setText('Running! please wait')
                QApplication.processEvents()  # 逐条打印状态

                makedb = NcbimakeblastdbCommandline(path + "/blast-BLAST_VERSION+/bin/makeblastdb.exe",
                                                    dbtype='nucl',
                                                    input_file=ref,
                                                    out=blastdb)
                makedb()

                blastn = NcbiblastnCommandline(path + "/blast-BLAST_VERSION+/bin/blastn.exe",
                                               query=query,
                                               db=blastdb,
                                               outfmt=format,
                                               evalue=float(evalue),
                                               out=out)

                blastn()
                self.textBrowser_7.setText('Finished!!!')


    def blastp(self):
        ref = self.textBrowser_3.toPlainText()
        query = self.textBrowser_2.toPlainText()
        blastdb = self.textBrowser.toPlainText()
        out = self.textBrowser_10.toPlainText()
        evalue = self.textEdit_13.toPlainText()
        format = self.textEdit_10.toPlainText()
        print(ref,query,blastdb,out,evalue,format)

        path = os.getcwd()
        path = '/'.join(path.split('\\'))

        print(len(ref),len(query),len(blastdb),len(out))

        def is_fasta(filename):
            with open(filename, "r") as handle:
                fasta = SeqIO.parse(handle, "fasta")
                return any(fasta)  # False when `fasta` is empty, i.e. wasn't a FASTA file

        if any([len(ref),len(query),len(blastdb),len(format)]) == False:
            QMessageBox.warning(self, "warning", "Please add correct file path!", QMessageBox.Cancel)
        else:
            if is_fasta(ref) == False or is_fasta(query) == False:
                QMessageBox.critical(self, "error", "check fasta file format!")
            else:
                if len(evalue) == 0:
                    evalue = 0.000001
                else:
                    evalue = evalue

                if len(format) == 0:
                    format = 6
                else:
                    format = format

                self.textBrowser_7.setText('Running! please wait')
                QApplication.processEvents()  # 逐条打印状态

                makedb = NcbimakeblastdbCommandline(path + "/blast-BLAST_VERSION+/bin/makeblastdb.exe",
                                                    dbtype='nucl',
                                                    input_file=ref,
                                                    out=blastdb)
                makedb()

                blastp = NcbiblastpCommandline(path + "/blast-BLAST_VERSION+/bin/blastn.exe",
                                               query=query,
                                               db=blastdb,
                                               outfmt=format,
                                               evalue=float(evalue),
                                               out=out)

                blastp()
                self.textBrowser_7.setText('Finished!!!')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # 启动预加载
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("logo.png"))
    splash.setFont(QFont('微软雅黑', 30))
    splash.showMessage("loading... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.show()  # 显示启动界面
    QtWidgets.qApp.processEvents()  # 处理主进程事件
    window = MyWindow()
    window.setWindowTitle("QSplashScreen类使用")
    window.resize(500, 50)
    window.load_data(splash)  # 加载数据
    splash.finish(window)  # 隐藏启动界面

    Main_Window = pages()
    Main_Window.show()
    sys.exit(app.exec_())

