#!/bin/bash  
mkdir Working
python3 -W ignore select_files.py
shopt -s nullglob dotglob     # To include hidden files
files=(./Working/*)
if [ ${#files[@]} -gt 0 ];
	then 
	echo "Cleaning and Coping the Temporary Files"
	echo "Extracting Faces from ID card";
	python3 crop_face.py
	rm -rf ./Id_verify/data/demo
	rm -rf ./Id_verify/data/results/*
	rm -rf ./Id_verify/data/temp/*
	rm -rf ./Id_verify/ocr/results/*
	rm -rf ./Id_verify/Id_reults/*
	mv ./Working ./Id_verify/data/demo
	echo "Done"

	cd Id_verify
	echo "Tensorflow Server Starting"
	python3 -W ignore ./ctpn/demo_pb.py
	echo "Text Boxes Detected"
	echo "Tensorflow Server Stopped"

	echo "OCR Extracting Text for Each Text Box"
	python3 -W ignore ./ocr/ocr.py
	echo "Done"

	echo "NLP Techniques for Extracting the Valid Information"
	python3 -W ignore ./ocr/get_inf.py
	echo "DONE"
	cd ..

	cp -r ./Id_verify/Id_result/json ./Output
	cp -r ./Id_verify/Id_result/text ./Output
	rm -rf ./Id_verify/Id_result/text/*
	rm -rf ./Id_verify/Id_result/json/*
	rm -rf ./Id_verify/data/demo
	rm -rf ./Id_verify/data/results/*
	rm -rf ./Id_verify/data/temp/*
	rm -rf ./Id_verify/ocr/results/*
	
	echo "Go To Id Result Folder for Extracting more Text Inf.";
	python3 change_name.py
else
	echo "Already Up-to_date";
fi
