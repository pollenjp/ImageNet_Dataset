#!/bin/bash -eux

# ILSVRC2012のDatasetを展開するshellscript
# Download                    : http://www.image-net.org/challenges/LSVRC/2012/nonpub-downloads
# Label (WNID, label name)    : https://gist.github.com/aaronpolhamus/964a4411c0906315deb9f4a3723aac57
# Label (ja)                  : https://github.com/starpentagon/python_scripts/blob/44a2840aa5bcbcafb5d71d8c9dcc14ee028b7cb9/dataset/ILSVRC2012_class_name/ILSVRC2012_class_name.csv


# 第一引数にtarファイル
readonly TAR_FILEPATH=$*
for filepath in ${TAR_FILEPATH}
do
  filepath=$(realpath ${filepath})
  echo "tar file path : ${filepath}"
  filename=$(basename ${filepath} .tar)
  dirpath="$(dirname ${filepath})/${filename}"
  mkdir "${dirpath}"
  tar -xvf ${filepath} -C "${dirpath}"
done


