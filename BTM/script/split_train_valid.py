#!/usr/bin/env python
#coding:utf-8
#Function: data->training+validation
#Author: Jingyi Li

import codecs
import sys
if sys.getdefaultencoding() != 'utf-8':
	reload(sys)
	sys.setdefaultencoding('utf-8')

def save_to_file(list, filename):
	with codecs.open(filename, 'a', encoding='utf-8') as f:
		f.writelines(list)


if __name__=='__main__':
	f_tag = open(r"/home/lijingyi/BTM/sample-data/tag.txt")
	f_des = open(r"/home/lijingyi/BTM/sample-data/describe_seg.txt")
	line_tag = f_tag.readline()
	line_des = f_des.readline()
	i=1
	while i<=100000:
		save_to_file(line_tag, '/home/lijingyi/BTM/sample-data/train_tag.txt')
		save_to_file(line_des, '/home/lijingyi/BTM/sample-data/train_des.txt')
		i=i+1
		line_tag = f_tag.readline()
		line_des = f_des.readline()
	
	while i<=120000:
		save_to_file(line_tag, '/home/lijingyi/BTM/sample-data/validation_tag.txt')
		save_to_file(line_des, '/home/lijingyi/BTM/sample-data/validation_des.txt')
		i=i+1
		line_tag = f_tag.readline()
		line_des = f_des.readline()
	f_tag.close()
	f_des.close()
