
- http://www.image-net.org/challenges/LSVRC/2012/nonpub-downloads
- [CaffeによるILSVRC2012の実行 - Qiita](https://qiita.com/htsst/items/2d69428cc538b5fa7497)

```
mkdir ILSVRC2012
```


## Development Kit

```
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_devkit_t12.tar.gz -O ILSVRC2012/ILSVRC2012_devkit_t12.tar.gz
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_devkit_t3.tar.gz  -O ILSVRC2012/ILSVRC2012_devkit_t3.tar.gz
```

```
tar -zxvf ILSVRC2012/ILSVRC2012_devkit_t12.tar.gz
tar -zxvf ILSVRC2012/ILSVRC2012_devkit_t3.tar.gz
```


## Images

```
# Training images (Task 1 & 2). 138GB. MD5: 1d675b47d978889d74fa0da5fadfb00e
mkdir ILSVRC2012/ILSVRC2012_img_train
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train.tar    --output-file=ILSVRC2012/ILSVRC2012_img_train/ILSVRC2012_img_train.tar
#  Training images (Task 3). 728MB. MD5: ccaf1013018ac1037801578038d370da
mkdir ILSVRC2012/ILSVRC2012_img_train_t3
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train_t3.tar --output-file=ILSVRC2012/ILSVRC2012_img_train_t3/ILSVRC2012_img_train_t3.tar
#  Validation images (all tasks). 6.3GB. MD5: 29b22e2961454d5413ddabcf34fc5622
mkdir ILSVRC2012/ILSVRC2012_img_val
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_val.tar      --output-file=ILSVRC2012/ILSVRC2012_img_val/ILSVRC2012_img_val.tar
#  Test images (all tasks). 13GB. MD5: fe64ceb247e473635708aed23ab6d839
mkdir ILSVRC2012/ILSVRC2012_img_train
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_test.tar     --output-file=ILSVRC2012/ILSVRC2012_img_test/ILSVRC2012_img_test.tar
```


## 展開

```
./01_ILSVRC2012_untar.bash.sh ILSVRC2012/ILSVRC2012_img_train
./02_decompression.bash.sh    ILSVRC2012/ILSVRC2012_img_train
```


