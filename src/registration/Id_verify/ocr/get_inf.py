from __future__ import print_function
import os
import glob
import json

from lib.fast_rcnn.config import cfg, cfg_from_file

from details_extract import DetailsExtracter

def writeToJson(path, data):
	""" 
	Write JSON file
	"""
	with open(path, 'w', encoding='utf-8') as outfile:
		json_data = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
		outfile.write(str(json_data))

def arr2str(arr):
	string = ''
	for element in arr:
		string = string + ' ' + element
	return string.strip()

def getContent(boxes):

	path = cur_dir +'/Id_result/text/' + 'ocr_res_{}.txt'.format(base_name.split('.')[0])

	prev_y = 0

	content = ""
	for box in boxes:
		text = arr2str(box[4:])
		if prev_y != box[3]:
			content += '\n' + text
		else:
			content += '    ' + text 
		prev_y = box[3]

	return content


if __name__ == "__main__":
	
	# Initialise Details Extractor Class
	details_extractor = DetailsExtracter()

	cur_dir = os.getcwd()

	images = []

	# Get images Only
	EXTENSIONS = ['png', 'jpg']
	for extension in  EXTENSIONS:
		path = os.path.join(cfg.DATA_DIR, 'demo', '*.{}'.format(extension))
		images += glob.glob(path)
 

	for image in images:
		base_name = image.split('/')[-1]

		path = cur_dir +'/ocr/results/' + 'ocr_res_{}.txt'.format(base_name.split('.')[0])
		with open( path, 'r') as f:
			boxes = f.read()

		# Remove Boxes without keys
		boxes = boxes.split('\n')[:-1]
		boxes = [ box.split(',') for box in boxes if len(box.split(','))>4 ]
		boxes.sort( key = lambda x : ( int(x[3]), int(x[0]) ) )

		content = getContent(boxes)

		with open( path, 'w') as f:
			f.write(content)

		# Search Details
		text = []
		lines = content.split('\n')
		for line in lines:
			s = line.replace('\n','')
			s = s.strip()
			text.append(s)
		text = list(filter(None, text))

		# Extract Details
		details_extractor.reset()
		data = details_extractor.extractDetails(text)

		# Write Output as JSON
		path = cur_dir + '/Id_result/json/' +'res_{}.json'.format(base_name.split('.')[0])
		writeToJson(data,path)
