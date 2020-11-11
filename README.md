# Med2AI: A Project-based Artificial Intelligence Training for Medical Students

* [0. Introduction](#Introduction)
* [1. Python Basic](#Python-Basic)
* [2. Linux Server Basic](#Linux-Server-Basic)
* [3. Statistical Machine Learning](#Statistical-Machine-Learning)
* [4. Deep Learning](#Deep-Learning)
* [5. Natural Language Processing](#Natural-Language-Processing)
* [6. Computer Vision](#Computer-Vision)
* [7. Comprehensive Project](#Comprehensive-Project)
* [8. Conclusion](#Conclusion)

## Introduction

This repository is under development and confidential. We will open it to public once it is finished.

xxxx

Target learners:

* Medical students with limited programming background
* Clinical researchers who want to understand/use clinical big data
* xxxx

System requirement:

* MacOS/Linux/Windows
* Python 3.7+
* Memory >= 4G

Books:

* 统计学习方法 李航 清华大学出版社
* 机器学习  周志华  清华大学出版社

## Python Basic

1. [Use of list/dict]



2. File I/O. 

* 2.1 Text reorganize: folder [file_io](data/file_io) includes 28 text files with "messtext" as the prefix. Each file includes one or more sentences of the introduction of school of public health, Zhejiang University (in Chinese and English). Each sentence starts with a prefix "[ENx]" or "[CNx]", where "EN"/"CN" represent English and Chinese and "x" is the order number of the corresponding sentence. Please write a code to read those files and recover them in order and save the output in file "PHSZJU.txt". The output file should be the same with file [original.txt](data/file_io/original.txt)

* 2.2 Save the output file in 2.1 into a '.csv' file, store the ordered sentences by row (one sentence per row).


## Linux Server Basic

* Use ssh to remote connect a linux server (I will provide the server ip and the user account/passwd)
* Change password 
* Basic commands: `cd`, `cp`, `rm` (careful)
* Upload/download files to/from the remote server (`scp #localfile #your_account@#server_ip:#directory`, `scp #your_account@#server_ip:#directory #localdirectory`)
* Run your python code through terminal: `python #your_code.py`
* Monitor the running processes in the server: `top` , `htop`
* Run code in the background of server (even when you are disconnected): `nohup python #your_code.py 1>#your_logfile 2>&1 &` 


## Statistical Machine Learning


* Logistic regression
* Support vector machine
* Random forest
* XGBoost

## Deep Learning

* Representations
* Feedforward Network
* CNN
* LSTM

## Natural Language Processing

* Preprocessing
* TF-IDF
* Transformer/BERT

## Computer Vision



## Comprehensive Project


## Conclusion