from __future__ import print_function
import glob
import os
import sys
import numpy as np
import cv2
sys.path.append(os.getcwd())

from lib.fast_rcnn.config import cfg, cfg_from_file
from lib.fast_rcnn.test import _get_blobs
from lib.text_connector.text_connect_cfg import Config as TextLineCfg
from PIL import Image
import pytesseract
import argparse
import ftfy

###### Section 1: Initiate the command line interface ###

## Section 2: Load the image -- Preprocess it -- Write it to disk

def ocr_extract_text(image):
	pass

def resize_im(im, scale, max_scale=None):
	pass
def crop(image, coords, saved_location,image_name,image_no):
	pass


############ Getting the data from results, obtained from Ctcn################
im_names = glob.glob(os.path.join(cfg.DATA_DIR, 'demo', '*.png')) + glob.glob(os.path.join(cfg.DATA_DIR, 'demo', '*.jpg'))
for im_name in im_names:
	img = cv2.imread(im_name)
	img, scale = resize_im(img, scale=TextLineCfg.SCALE, max_scale=TextLineCfg.MAX_SCALE)
	base_name = im_name.split('/')[-1]
	#print (base_name)
	line = ""
	with open(cfg.DATA_DIR +'/results/' + 'res_{}.txt'.format(base_name.split('.')[0]), 'r') as f:
		i = 0
		boxes = f.readlines()
		for box in boxes:
			i = i + 1
			box = box.strip('\n')
			co_ords = box.split(',')
			min_x = int(co_ords[0])
			min_y = int(co_ords[1])
			max_x = int(co_ords[2])
			max_y = int(co_ords[3])
			text = crop(img, (min_x,min_y,max_x,max_y),'data/temp/',im_name,i)
			line += ','.join([str(min_x), str(min_y), str(max_x), str(max_y),str(text)]) + '\r\n'
		f.close()
	cur_dir = os.getcwd()
	with open( cur_dir +'/ocr/results/' + 'ocr_res_{}.txt'.format(base_name.split('.')[0]), 'w') as f:
		f.write(line)
		f.close()

