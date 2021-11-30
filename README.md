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

This repository is under development and confidential. We will make it public once it is well .

xxxx

#### Target learners:
* Medical students with limited programming background
* Clinical researchers who want to understand/use clinical big data

#### System requirement:
* MacOS/Linux/Windows
* Python 3.7+
* Memory >= 4G

#### Books:
* 统计学习方法 李航 清华大学出版社
* 机器学习  周志华  清华大学出版社

## 1. Python Skills

### 1.1 Basic Python
Get familiar with:
* Python installment (if necessary)
* `for` loop, `if`-`else`, `print`
* `list`
* `dict` 


### 1.2. File I/O. 
#### 1.2.1 Text re-organize: 
* Folder [file_io](data/file_io) includes 28 text files with "messtext" as the prefix. Each file includes one or more sentences of the introduction of school of public health, Zhejiang University (in Chinese and English). Each sentence starts with a prefix "[ENx]" or "[CNx]", where "EN" and "CN" represent English and Chinese, respectively, and "x" is the order number of the corresponding sentence. Please write a code to read those files and recover them in order and save the output in file "PHSZJU.txt". The output file should be the same with file [original.txt](data/file_io/original.txt)

#### 1.2.2 Format convert
* Save the output file in 2.1 into a '.csv' file, store the ordered sentences by row (one sentence per row).

### 1.3. Common Packages
Get familiar with packages:
* `pandas`
* `nltk`
* `sklearn`


## 2. Linux Server Basic
* Use ssh to remote connect a linux server (I will provide the server ip and the user account/passwd)
* Change password 
* Basic commands: `cd`, `cp`,`mv`,`mkdir`, `rm` (be careful!)
* Upload/download files to/from the remote server (`scp #localfile #your_account@#server_ip:#directory`, `scp #your_account@#server_ip:#directory #localdirectory`)
* Run your python code through terminal: `python #your_code.py`
* Monitor the running processes in the server: `top` , `htop`
* Run code in the background of server (even when you are disconnected): `nohup python #your_code.py 1>#your_logfile 2>&1 &` 


## 3. Statistical Machine Learning
Build a heart failure prediction model using statistical machine learning algorithms (Logistic regression, SVM, random forest, XGBoost).  

#### Dataset: 
* https://www.kaggle.com/andrewmvd/heart-failure-clinical-data

#### Settings: 
* split the dataset into training/test dataset. 
* Training dataset: odd rows (line 1,3,5,7...); 
* Test dataset: even rows (line 2,4,6,8...) 

#### Models to be tested:
* Logistic regression
* Support vector machine (SVM)
* Random forest
* XGBoost

#### Requirements: 
* Show the accuracy of the model on the test dataset.
* Given a new example, predict the heart failure results
* Generate the predicted probability of each new example
* Compare the performance of the above four models

#### Evaluation:
* Precision
* Receiver Operating Characteristic (ROC) curve and Precision-Recall Curve (PRC)
* AUROC and AUPRC

#### Tips: 
* Use package `sklearn` 
* Example https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html


## 4. Deep Learning
Statistical machine machine models require various features (defined by human e.g. one-hot, tf-idf) to represent the input data. Deep learning model utilize the neural network structure to extract features automatically. It learns the features from the data based on the target labels. 

### Tools

#### GPU support
As the deep neural network structures requires large scale matrix calculation, it is ideal to use GPU to conduct the matrix calculation in parallel. If you want to train complex deep learning models or on large training dataset, if is necessary to experiment on server with GPU. YLab has two servers with GPU support:

* Ylab1: Nvidia 2080TI x 2 
* Ylab2: Nvidia 3090 x 1

#### PyTorch
`PyTorch` is one of the most popular deep learning packages (others include `tensorflow`, `mxnet` .etc.). It is the most popular development package in academia. 

#### NCRF++ for NLP
[NCRF++](https://github.com/jiesutd/NCRFpp) is developed by Jie Yang for text representation with various neural network structures. This framework supports sequence labeling and text classification tasks with a flexible, hierarchial, and configurable way. Currently, it supports:

* Feedforward Network
* Convolutional Neural Network (CNN)
* Recurrent Neural Networks (RNN), including GRU, LSTM
* Transformer, including pretrained models BERT, RoBERTa, .etc.
* User-defined neural features

## 5. Natural Language Processing
Natural language processing(NLP) is to analyze texts with information technology, especially the artificial intelligence technology. 
### 5.1 Spam email classification (TREC 2006 Spam Track)
Build a natural language processing model to identify spam emails automatically.

#### Data:
https://plg.uwaterloo.ca/~gvcormac/treccorpus06/, please use the English corpus first `trec06p.tgz`. It includes about 37822 emails, of which 24912 emails are spam (see `trec06p/full/index`). Please refer `trec06p/README.txt` for more details about the dataset.

#### Preprocessing:
* Extract all the emails from all the subfolders of `trec06p/data/`, and map the labels (in `trec06p/full/index`) with the emails.
* Remove format content of the email, e.g. `<tr>`, `<td width="100%">`,`<p align="center">`. Hint: remove any context between `<>` (be careful for the cases `<tr>  this is the email content <td width="100%">`, please keep `this is the email content` rather than remove all of them).
* Select the first 20000 emails as the training set, email from 20001-25000 as development dataset, emails from 25001-37822 as the test dataset. 

#### Methods:
* From text to numbers: use one-hot representation to convert each email to a binary vector. Reference: https://medium.com/zero-equals-false/one-hot-encoding-129ccc293cda
* Predict model: logistic regression. 

#### Evaluation:
* Precision
* Receiver Operating Characteristic (ROC) curve and Precision-Recall Curve (PRC)
* AUROC and AUPRC


### Model Improvement
Using following steps or advanced feature extraction methods to improve model performance:

* Preprocessing: data filtering, text cleaning, word normalization, etc.
* TF-IDF
* Word embeddings
* Transformer/BERT

## 6. Computer Vision



## 7. Comprehensive Project


## 8. Conclusion