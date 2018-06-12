#!/usr/bin/env python
#coding:utf-8
#Function: data->training+validation
#Author: Jingyi Li

if __name__=='__main__':
	f_vec = open(r"/home/lijingyi/BTM/output_new/model/k40.pz_d","r")
	f_train = open("/home/lijingyi/BTM/output_new/model/k40_train.pz_d","w")
	f_valid = open("/home/lijingyi/BTM/output_new/model/k40_valid.pz_d","w")
	i=1
	line_vec = f_vec.readline()
	while i<=100000:
		f_train.write(line_vec)
		
		i=i+1
		line_vec = f_vec.readline()
	
	while i<=120000:
		f_valid.write(line_vec)
		i=i+1
		line_vec = f_vec.readline()

	f_vec.close()
	f_train.close()
	f_valid.close()
