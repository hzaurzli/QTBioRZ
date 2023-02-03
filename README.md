# QTBioRZ
A user-friendly interface visualization software,the main functions are following:
1. Blastn and Blastp are for DNA or protein sequences searching
2. Counting microorganism colonies
3. Calculating anti-peptides activity
4. identifing phages lysogeny

## 1.Blastn and Blastp
![Blastn](https://user-images.githubusercontent.com/47686371/216488994-b80508aa-b561-4e52-af36-b58db029c012.png)

1. Reference file is for database fasta file
2. Query file is for your own fasta file,which is you want to search for
3. BLASTdb path is for reference database index
4. output file stores blast result
Click Run to start your program

![Blastp](https://user-images.githubusercontent.com/47686371/216489552-99e3828a-4c34-4dae-be8e-3c754e022a18.png)

1. Reference file is for database fasta file
2. Query file is for your own fasta file,which is you want to search for
3. BLASTdb path is for reference database index
4. output file stores blast result
Click Run to start your program

## 2.Counting microorganism dots
![](https://user-images.githubusercontent.com/47686371/216492340-41c8cbb7-4588-405f-962c-a8b7ab59bfa1.png)
Quick and accurate colony counting,different parameters please refer to [open-cv manual](https://docs.opencv.org/4.x/)

## 3.Calculating anti-peptides activity
![](https://user-images.githubusercontent.com/47686371/216491286-e1d215cd-88f2-4f93-b584-18405b684ae4.png)
Basic model refers to [manual](https://github.com/mayuefine/c_AMPs-prediction),please cite [Identification of antimicrobial peptides from the human gut microbiome using deep learning](https://www.nature.com/articles/s41587-022-01226-0)

1. Input file(Fa) is for input fasta file
2. Activity file is for result

Result:
![](https://user-images.githubusercontent.com/47686371/216492727-f3cf2a3c-d7b8-44c0-9d0c-8d648a9892de.png)
First column is for sequence name,second column is for sequence,third column is for activity score，more than 0.5 indicate active peptide,or non active

## 4.Phages lysogeny
![](https://user-images.githubusercontent.com/47686371/216493305-2bbc03e5-3198-47ea-8180-f06c9698274f.png)
Basic model refers to [manual]([https://github.com/mayuefine/c_AMPs-prediction](https://github.com/KennthShang/PhaTYP)),please cite [PhaTYP: Predicting lifestyle for bacteriophages using BERT](https://academic.oup.com/bib/article/24/1/bbac487/6842869?login=true)

1. Input file(Fa) is for input fasta file
2. Lysogen file is for result

Finally,lysogen_prediction.csv is your result:
Virulent is for virulent phage,temperate is for temperate phage


If this software is useful,please cite <https://github.com/hzaurzli/QTBioRZ/>
Links for Baidu：https://pan.baidu.com/s/1MGTAzY6d2AcUWZEL3QgvQA 
Password：0rka
