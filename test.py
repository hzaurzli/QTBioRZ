from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio import SeqIO


path = 'D:/tools/Pycharm/pyqt'
makedb = NcbimakeblastdbCommandline(path + "/blast-BLAST_VERSION+/bin/makeblastdb.exe",
                                                    dbtype='prot',
                                                    input_file='D:/S.suis/metadata/card/protein_ARGs.fa.txt',
                                                    out='D:/Documents/Desktop/db/lssp')
makedb()

blastp = NcbiblastpCommandline(path + "/blast-BLAST_VERSION+/bin/blastp.exe",
                               query='D:/S.suis/metadata/card/lssp270.faa.txt',
                               db='D:/Documents/Desktop/db/lssp',
                               outfmt=6,
                               evalue=float(0.00001),
                               out='D:/Documents/Desktop/result.txt')

stdout, stderr = blastp()
print(stderr)