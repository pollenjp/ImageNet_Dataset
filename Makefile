SHELL := /usr/bash


all :
	./01_ILSVRC2012_untar.bash.sh ILSVRC2012/ILSVRC2012_img_train
	./02_decompression.bash.sh    ILSVRC2012/ILSVRC2012_img_train
	ls -1 ILSVRC2012/ILSVRC2012_img_train > wnid.csv
	python3 wnid_label.py
	python3 make_csv_dataset.py \
		--search_path=./ILSVRC2012/ILSVRC2012_img_train \
		--wnid_label_filepath=./wnid_label.csv \
		--output_filepath=./train_dataset.csv
	python3 resize_image.py \
		--imagepath_filepath=train_dataset.csv