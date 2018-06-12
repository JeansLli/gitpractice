#!/usr/bin/env python
#coding:utf-8
#Function: determine the topic of a sentence
#Input:
#	mat/k__.pz_d

import sys
import codecs
if sys.getdefaultencoding() != 'utf-8':
import sys
	reload(sys)
	sys.setdefaultencoding('utf-8')

def save_to_file(list, filename):
    with codecs.open(filename, 'a', encoding='utf-8') as f:
	        f.writelines(list)
			

if __name__=='__main__':
	model_dir = sys.argv[1]
	K = int(sys.argv[3])
	output_dir = sys.argv[2]
	rowsentence= sys.argv[4]
	pz_d=model_dir+'k%d.pz_d' % K
	doc_topic=[]
	doc_index=0
	for l in open(pz_d):
		vs=[float(v) for v in l.split()]
		k = 0
		maxv = 0
		index_topic= 0
		for k in range(K):
			if vs[k]>maxv:
				maxv= vs[k]
				index_topic = k
		doc_topic.append(index_topic)
		doc_index=doc_index+1
	i=0
	for l in open(rowsentence):
		topic=doc_topic[i]
		filename=output_dir+'topic'+str(topic)+'.txt'
		save_to_file(l,filename)
		i=i+1
