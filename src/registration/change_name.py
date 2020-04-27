import os
import json 
import shutil
for filename in os.listdir('Output/json'):
	f = open("Output/json/" + filename, "r")
	a = f.read()
	y = json.loads(a) 
	roll_number = y['roll_no']
	# print(roll_number)
	name = filename.split('.')[0]
	name = name.split('_')[1]
	# print (name)
	original = 'Output/json/' + filename
	target = '../../static/json/' + roll_number + '.json'
	shutil.copyfile(original,target)

	original = 'Source/' + name + '.jpg'
	target = '../../static/cards/' + roll_number + '.jpg'
	shutil.copyfile(original,target)

	original = 'Faces/' + name + '.jpg'
	target = '../../static/faces/' + roll_number + '.jpg'
	shutil.copyfile(original,target)
