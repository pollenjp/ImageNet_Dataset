#!/bin/bash

#  Training images (Task 3). 728MB. MD5: ccaf1013018ac1037801578038d370da
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train_t3.tar --output-file=ILSVRC2012_img_train_t3/ILSVRC2012_img_train_t3.tar
#  Validation images (all tasks). 6.3GB. MD5: 29b22e2961454d5413ddabcf34fc5622
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_val.tar      --output-file=ILSVRC2012_img_train/ILSVRC2012_img_train.tar
#  Test images (all tasks). 13GB. MD5: fe64ceb247e473635708aed23ab6d839
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_test.tar     --output-file=ILSVRC2012_img_train/ILSVRC2012_img_train.tar

# Training images (Task 1 & 2). 138GB. MD5: 1d675b47d978889d74fa0da5fadfb00e
wget http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train.tar    --output-file=ILSVRC2012_img_train/ILSVRC2012_img_train.tar
