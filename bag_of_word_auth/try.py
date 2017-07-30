#!/usr/bin/python
# -*- coding: utf8 -*-
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import math,os
import pandas as pd
import json
#define function tf
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

#define function idf
def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    #counts the number of documents that contain a word w
    idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] +=1
                
    #divide N by denominator above, take the log of that
    for word, val in idfDict.items():
        idfDict[word]= math.log(N / float(val)) 

    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf


def space(t,z):
    tu = 0
    mau1 = 0
    mau2 = 0
    mau = 0  
    Sum_1 = 0
    Sum_2 = 0
    for val in range(len(t)):
        for value in range(len(z)):
            if value == val :
                tu +=(t[val]*z[value])

    for val in t:
        Sum_1 += math.pow(val,2)
        mau1 = math.sqrt(Sum_1)

    for val in z:
        Sum_2 += math.pow(val,2)
        mau2 = math.sqrt(Sum_2)

    mau = mau1 * mau2
    total = tu/mau
    return total
    
def compare(a,b):
    if(a>b):
        return a;
    else:   
        return b;
# code main

# test open all file chi dc file .txt cac file .txt~ k luu dc
path_test = 'test/comment'
obj3=open(path_test,"r")
files_test = obj3.read()
obj3.close()
files = []
tfidf = []
wordDict = []
newA = []
tf =[]
q = []
z = []
u_neg = []
u_pos = []
u_test = []
count_neg = 0
count_pos = 0
    #task 1
path_neg = 'training/negative'
obj1=open(path_neg,"r")
str1 = obj1.read()
files_neg = str1.split("\n\n")
print len(files_neg)
obj1.close()

path_pos = 'training/positive'
obj2=open(path_pos,"r")
str2 = obj2.read()
files_pos = str2.split("\n\n")
print len(files_pos)
obj2.close()
files.append(files_test)
files.extend(files_neg)
files.extend(files_pos)
print len(files)
print files[0]
for value in range(len(files)):
	decode = files[value].decode('utf-8')
	tmp = ViTokenizer.tokenize(decode)
  	split = tmp.split(" ")
   	newA.append(split)
    # mang 2 chieu luu tach tu 
union = set.union(*(set(value) for value in newA))
for val in range(len(files)):
    wordDict.append(dict.fromkeys(union, 0))

for num in range(len(newA)):
    for word in newA[num]:
        wordDict[num][word]+=1

    #tf
for val in range(len(wordDict)):
    tfBow = computeTF(wordDict[val],newA[val])
    tf.append(tfBow)

    #idf
idfs = computeIDF(wordDict)

    #tfidf
for val in tf: 
    tfidfBow =  computeTFIDF(val, idfs)
    tfidf.append(tfidfBow)

print pd.DataFrame(tfidf)

x_neg = dict.fromkeys(tfidf[0].keys(),0)
x_pos = dict.fromkeys(tfidf[0].keys(),0)
x_test = tfidf[0]
longNum = len(newA)