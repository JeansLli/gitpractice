#!/usr/bin/env python
#Function: knn
#Author: Jingyi Li

from numpy import *
import operator


def trans2numvec(string):
	mylist=string.split()   #transform the string to a list
	k = len(mylist)
	vec=[]
	for i in range(k):
		vec.append(float(mylist[i]))   #transform a substring to float
	return array(vec)
		
def knn_predict(newInput, dataSet, labels, k):
	numSample = dataSet.shape[0]
	##step1: calculate Eucliean distance
	diff = tile(newInput,(numSample,1))-dataSet
	squaredDiff = diff ** 2
	squaredDist = sum(squaredDiff, axis=1)
	distance = squaredDist ** 0.5

	##step2: sort the distance
	sortedDistIndices = argsort(distance)
	classCount={}
	for i in xrange(k):
		voteLabel = labels[sortedDistIndices[i]]
		classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
	
	maxCount = 0
	for key, value in classCount.items():
		if value > maxCount:
			maxCount = value
			maxIndex = key
	return maxIndex
	

if __name__ == '__main__':
#transform the training data to a big matrix
	f_train = open(r"/home/lijingyi/BTM/output_new/model/k40_train.pz_d","r")
	line_train_vec = f_train.readline()
	datamatrix=[]
	while line_train_vec:
		trainvec = trans2numvec(line_train_vec)
		datamatrix.append(trainvec)
		line_train_vec = f_train.readline()
	f_train.close()
	
	traindata=array(datamatrix)

#transform tags to a vector
	f_tag = open(r"/home/lijingyi/BTM/sample-data/train_tag.txt")
	line_tag=f_tag.readline()
	tagvec=[]
	while line_tag:
		tagvec.append(line_tag)
		line_tag = f_tag.readline()
	f_tag.close()

#transform the test string to a number vector and predict
	f_valid_vec = open(r"/home/lijingyi/BTM/output_new/model/k40_valid.pz_d","r")
	line_valid_vec = f_valid_vec.readline()


	f_predict = open('/home/lijingyi/BTM/output_new/predict','w')
	while line_valid_vec:
		testvec = trans2numvec(line_valid_vec)
		tag = knn_predict(testvec,traindata,tagvec,1000)
		f_predict.write(tag)   #!!!!!!!!!!!!!!may need to change the form of the file
		line_valid_vec = f_valid_vec.readline()
	f_valid_vec.close()
	f_predict.close()

