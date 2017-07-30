#!/usr/bin/python
# -*- coding: utf8 -*-
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import math,os
import pandas as pd
import json
from cassandra.io.libevreactor import LibevConnection
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import facebook
import time

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
def alt(array):
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

    path_neg = '/home/rindem/Desktop/bag_of_word_auth/training/negative'
    obj1=open(path_neg,"r")
    str1 = obj1.read()
    files_neg = str1.split("\n\n")
   # print len(files_neg)
    obj1.close()

    path_pos = '/home/rindem/Desktop/bag_of_word_auth/training/positive'
    obj2=open(path_pos,"r")
    str2 = obj2.read()
    files_pos = str2.split("\n\n")
   # print len(files_pos)
    obj2.close()
    files.append(array)
    files.extend(files_neg)
    files.extend(files_pos)
  #  print len(files)


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

    x_neg = dict.fromkeys(tfidf[0].keys(),0)
    x_pos = dict.fromkeys(tfidf[0].keys(),0)
    x_test = tfidf[0]
    longNum = len(newA)
    for num in range(1,((longNum-1)/2)+1):
        for word in newA[num]:
            x_neg[word]+=tfidf[num][word]

    for num in range(((longNum-1)/2)+1,longNum):
        for word in newA[num]:
            x_pos[word]+=tfidf[num][word]



    for word,val in x_neg.items():
        u_neg.append(x_neg[word])
        

    for word,val in x_pos.items():
        u_pos.append(x_pos[word])
        

    for word,val in x_test.items():
        u_test.append(x_test[word])
   # print "\n"
   # print "Compare test vs neg: ", space(u_test,u_neg)
    tmp = space(u_test,u_neg)
   # print "Compare test vs pos", space(u_test,u_pos)
   # print "\n"
    temp = space(u_test,u_pos)
    if(compare(tmp,temp)==tmp):
        return 1
    else:
        return 2

'''path_test = 'test/negative_Test'
obj3=open(path_test,"r")
str3 = obj3.read()
files_test = str3.split("\n\n")
obj3.close()
print files_test'''
start_time = time.time()
data_test = []
data_dict = {}
data_neg = []
result = []
cluster = Cluster()
cluster.connection_class = LibevConnection
session = cluster.connect('getfb')
rows = session.execute('SELECT * FROM getdata')

for row in rows:
    data_test.append(row.comment.encode('utf8'))
    id_comment = row.id_comment
    comment = row.comment
    tmp_dict ={id_comment.encode('utf8'):comment.encode('utf8')}
    data_dict.update(tmp_dict)

count_neg = 0 
count_pos = 0
if(data_test):
    for val in data_test:
       # print val
        if (alt(val)==1):
            data_neg.append(val)
            count_neg+=1
        else:
            count_pos+=1
       # print "////////"

'''if(count_pos & count_pos):
    print '\n'
    print "tổng giá trị positive:", count_pos, "\ttổng giá trị negative:", count_neg
    print'\n'
    print "tỉ lệ positive:",((count_pos)/float(count_pos+count_neg))*100," %\n"
    print "tỉ lệ negative:",((count_neg)/float(count_pos+count_neg))*100," %"
'''

for key,value in data_dict.items():
    for val in data_neg:
        if(val==value):
            result.append(key)
        else:
            query_del = "DELETE from getdata WHERE id_comment='"+ key + "'"
            session.execute(query_del) 

#query_truncate = "TRUNCATE TABLE add_neg"
#session.execute(query_truncate)
graph = facebook.GraphAPI(access_token='EAAUq7vkspMMBAKI2thvq7QVXsxNwleAfNvYT4S9bK1FLZArIDk1Kv507YhxYrNSfHKHqkwdfPCRUeqZCFmlmdj2dgYlFcPAD5gxWdIhiLT7s8UoutmPE8LjVZAyBTiqAVZBadzGfMcUPiEvqYx4TKg4WwU3UdWAbF5tTib0prwZDZD', version='2.7')

for val in result:
    x = graph.delete_object(id = val)
    if(x!="None"):
        print "done"
    else:
        print "error"

end_time = time.time()
print 'total run-time: %f ms' % ((end_time - start_time) * 1000)