# ImageNet Dataset

- http://image-net.org/download-imageurls
- BoundingBox : http://image-net.org/download-bboxes.php

```
mkdir ILSVRC2012
```

## download
- http://www.image-net.org/challenges/LSVRC/2012/nonpub-downloads
- こちらから`Training images (Task 1 & 2). 138GB`をダウンロード

# Training images (Task 1 & 2). 138GB. MD5: 1d675b47d978889d74fa0da5fadfb00e

```
$ mkdir ILSVRC2012/ILSVRC2012_img_train
$ wget ¥
    http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train.tar ¥
    --output-file=ILSVRC2012/ILSVRC2012_img_train/ILSVRC2012_img_train.tar
$ md5sum ILSVRC2012_img_train.tar
1d675b47d978889d74fa0da5fadfb00e  ILSVRC2012_img_train.tar
```

`md5sum`も意外と時間がかかる

## 展開

```
./01_ILSVRC2012_untar.bash.sh ILSVRC2012/ILSVRC2012_img_train
./02_decompression.bash.sh    ILSVRC2012/ILSVRC2012_img_train
```


## make dataset

```
ls -1 ILSVRC2012/ILSVRC2012_img_train > wnid.csv
```

```
python3 wnid_label.py
```

```
python3 make_csv_dataset.py \
  --search_path=./ILSVRC2012/ILSVRC2012_img_train \
  --wnid_label_filepath=./wnid_label.csv \
  --output_filepath=./train_dataset.csv
```


## resize

```
python3 resize_image.py \
  --imagepath_filepath=train_dataset.csv
```


## Bounding Box

```
mkdir Annotation
wget http://image-net.org/Annotation/Annotation.tar.gz --output-file=Annotation/Annotation.tar.gz
cd Annotation
tar -zxvf Annotation.tar.gz 
rm Annotation.tar.gz
ls -1 | xargs -I{} tar -zxvf {}
```

するとさらに下の`Annotation/`に展開される.


## 参考
- http://www.image-net.org/challenges/LSVRC/2012/nonpub-downloads
- [CaffeによるILSVRC2012の実行 - Qiita](https://qiita.com/htsst/items/2d69428cc538b5fa7497)
- https://gist.github.com/aaronpolhamus/964a4411c0906315deb9f4a3723aac57



