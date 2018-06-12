#!/usr/bin/env python
#coding:utf-8
#Function: compare predict and validation_tag
#Author:Jingyi Li

if __name__ == '__main__':
	f_predict = open(r"/home/lijingyi/BTM/output_new/predict","r")
	f_tag = open(r"/home/lijingyi/BTM/sample-data/validation_tag.txt","r")
	f_wrong = open("/home/lijingyi/BTM/output_new/wrongnum","w")
	f_des = open(r"/home/lijingyi/BTM/sample-data/validation_rowdes.txt","r")
	line_predict = f_predict.readline()
	line_tag = f_tag.readline()
	line_des = f_des.readline()
	countCorrect = 0
	countFail = 0
	while line_predict:
		if line_predict == line_tag:
			countCorrect = countCorrect + 1
		else:
			countFail = countFail + 1
			f_wrong.write('预测:'+line_predict)
			f_wrong.write('标注:'+line_tag)
			f_wrong.write('描述:'+line_des)
			f_wrong.write("\n")
		line_predict = f_predict.readline()
		line_tag = f_tag.readline()
		line_des = f_des.readline()
	f_predict.close()
	f_tag.close()
	f_wrong.close()
	accuracy =float(countCorrect)/float(countCorrect+countFail)
	print("The number of correct prediction is %d" %countCorrect)
	print("The number of failure prediction is %d" %countFail)
	print("The accuracy is %.4f" %accuracy)

