from __future__ import print_function
import os
import sys
import re
import glob
import json
from lib.fast_rcnn.config import cfg, cfg_from_file

def arr_to_str(arr):
	string = ''
	for element in arr:
		string = string + ' ' + element
	return string.strip()

cur_dir = os.getcwd()
im_names = glob.glob(os.path.join(cfg.DATA_DIR, 'demo', '*.png')) + glob.glob(os.path.join(cfg.DATA_DIR, 'demo', '*.jpg'))
for im_name in im_names:
	base_name = im_name.split('/')[-1]
	#print (base_name)
	with open( cur_dir +'/ocr/results/' + 'ocr_res_{}.txt'.format(base_name.split('.')[0]), 'r') as f:
		boxes = f.read()
		boxes = boxes.split('\n')
		boxes = boxes[:-1]

		sort_boxes = []
		#### Making dictonary for sorting #####
		for box in boxes:
			co_ord = box.split(',')
			if len(co_ord) >= 5:
				sort_boxes.append(co_ord)

		sort_boxes.sort(key=lambda x: (int(x[3]),int(x[0])))
		
	with open( cur_dir +'/Id_result/text/' + 'ocr_res_{}.txt'.format(base_name.split('.')[0]), 'w') as f:
		prev_y = 0
		content = ""
		for box in sort_boxes:
			text_arr = box[4:]
			text = arr_to_str(text_arr)
			if prev_y != box[3]:
				content += '\n' + text
			else:
				content += '    ' + text 
			prev_y = box[3]
		f.write(content)

	#print (content)
############################################################################################################
###################################### Section 4: Extract relevant information #############################
############################################################################################################
	text = content
	# Initializing data variable
	name = None
	email =None
	mob = None
	address = None 
	dob = None 

	nameline = []
	dobline = []
	text0 = []
	text1 = []
	text2 = []

	# Searching for Detail
	lines = text.split('\n')
	for lin in lines:
	    s = lin.strip()
	    s = lin.replace('\n','')
	    s = s.rstrip()
	    s = s.lstrip()
	    text1.append(s)

	text1 = list(filter(None, text1))
	#print(text1)

	#### Regex for extracting all email and Mobile or Phone number on id card#####
	emails = []
	phones = [] 
	dates = []
	c_name = []
	address = []
	name = []
	flag,count = 0,0
	for line in text1:
		temp = line.lower()
		wordss = temp.split(' ')

		words = []
		for word in wordss:
			word = word.replace(';',':')
			words.append(word)
		#print(words)
		

