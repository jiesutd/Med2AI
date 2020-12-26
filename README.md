# Med2AI: A Project-based Artificial Intelligence Training Course for Medical Students

* [0. Introduction](#0-Introduction)
* [1. Python Basic](#1-Python-Basic)
* [2. Linux Server Basic](#2-Linux-Server-Basic)
* [3. Statistical Machine Learning](#3-Statistical-Machine-Learning)
* [4. Deep Learning](#4-Deep-Learning)
* [5. Natural Language Processing](#5-Natural-Language-Processing)
* [6. Computer Vision](#6-Computer-Vision)
* [7. Comprehensive Project](#7-Comprehensive-Project)
* [8. Conclusion](#8-Conclusion)

## 0. Introduction

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

## 1. Python Basic

1.1 Familiar with `list`, `dict` and basic python skills.



1.2. File I/O. 

* 1.2.1 Text reorganize: folder [file_io](data/file_io) includes 28 text files with "messtext" as the prefix. Each file includes one or more sentences of the introduction of school of public health, Zhejiang University (in Chinese and English). Each sentence starts with a prefix "[ENx]" or "[CNx]", where "EN"/"CN" represent English and Chinese and "x" is the order number of the corresponding sentence. Please write a code to read those files and recover them in order and save the output in file "PHSZJU.txt". The output file should be the same with file [original.txt](data/file_io/original.txt)

* 1.2.2 Save the output file in 2.1 into a '.csv' file, store the ordered sentences by row (one sentence per row).


## 2. Linux Server Basic

* Use ssh to remote connect a linux server (I will provide the server ip and the user account/passwd)
* Change password 
* Basic commands: `cd`, `cp`,`mv`,`mkdir`, `rm` (careful)
* Upload/download files to/from the remote server (`scp #localfile #your_account@#server_ip:#directory`, `scp #your_account@#server_ip:#directory #localdirectory`)
* Run your python code through terminal: `python #your_code.py`
* Monitor the running processes in the server: `top` , `htop`
* Run code in the background of server (even when you are disconnected): `nohup python #your_code.py 1>#your_logfile 2>&1 &` 


## 3. Statistical Machine Learning

Build the heart failure prediction model using the statistical machine learning models (Logistic regression, SVM, random forest, XGBoost).  

Dataset: https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

Settings: 
* split the dataset into training/test dataset. 
* Training dataset: odd rows (line 1,3,5,7...); 
* Test dataset: even rows (line 2,4,6,8...) 

Requirements: 
* show the accuracy of the model on the test dataset.
* given a new example, predict the heart failure results
* show the predicted probability of each new example

Tips: 
* use package `sklearn` (except XGBoost)
* example https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

3.1 Logistic regression

3.2 Support vector machine (SVM)

3.3 Random forest

3.4 *XGBoost

## 4. Deep Learning

* Representations
* Feedforward Network
* CNN
* LSTM

## 5. Natural Language Processing

### 5.1 Spam email classification (TREC 2006 Spam Track)
Build a natural language processing model to identify spam emails automatically.

#### Data:

https://plg.uwaterloo.ca/~gvcormac/treccorpus06/, please use the English corpus first `trec06p.tgz`. It includes about 37822 emails, of which 24912 emails are spam (see `trec06p/full/index`). Please refer `trec06p/README.txt` for more details about the dataset.

#### Preprocessing:

* Extract all the emails from all the subfolders of `trec06p/data/`, and map the labels (in `trec06p/full/index`) with the emails.
* Remove format content of the email, e.g. `<tr>`, `<td width="100%">`,`<p align="center">`. Hint: remove any context between `<>` (be careful for the cases `<tr>  this is the email content <td width="100%">`, please keep `this is the email content` rather than remove all of them).
* Select the first 20000 emails as the training set, email from 20001-25000 as development dataset, emails from 25001-37822 as the test dataset. 

#### Methods:

* From text to numbers: use one-hot representation to convert each email as a binary vector. Reference: https://medium.com/zero-equals-false/one-hot-encoding-129ccc293cda
* Predictive model: logistic regression. 

#### Evaluation:

* Precision
* AUC

**------------------------------------------ Project 5.1 ends here.--------------------------------**


* Preprocessing
* TF-IDF
* Word embeddings
* Transformer/BERT

## 6. Computer Vision



## 7. Comprehensive Project


## 8. Conclusion