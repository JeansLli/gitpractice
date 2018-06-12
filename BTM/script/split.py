#!/usr/bin/env python
#coding:utf-8
#Function: split rowdata.txt
#Author: Jingyi Li

import codecs
import sys
if sys.getdefaultencoding() != 'utf-8':
	reload(sys)
	sys.setdefaultencoding('utf-8')


def save_to_file(list,filename):
	with codecs.open(filename, 'a', encoding='utf-8') as f:
		f.writelines(list)


if __name__=='__main__':
	f=open(r"/home/lijingyi/BTM/sample-data/rowdata.txt","r")
	line=f.readline()
	while line:
		if len(line.split())>0:
			tag = line.split()[0]
			if tag == '挂号咨询' or tag == '骨科' or tag == '眼科' or tag == '口腔科' or tag == '妇科' or tag == '产科' or tag == '儿科':
				describe = line.split()[1:]
				save_to_file(tag,'/home/lijingyi/BTM/sample-data/tag.txt')
				save_to_file('\n','/home/lijingyi/BTM/sample-data/tag.txt')
				save_to_file(describe,'/home/lijingyi/BTM/sample-data/describe.txt')
				save_to_file('\n','/home/lijingyi/BTM/sample-data/describe.txt')
			else:
				save_to_file(line,'/home/lijingyi/BTM/sample-data/notag.txt')
		line=f.readline()
	f.close()
