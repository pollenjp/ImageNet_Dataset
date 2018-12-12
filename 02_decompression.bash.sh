#!/bin/sh

# cite: https://qiita.com/htsst/items/2d69428cc538b5fa7497#%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E5%B1%95%E9%96%8B

readonly DIR_PATH=$(realpath $1)

files="${DIR_PATH}/n*.tar"
for filepath in ${files}
do
  filename=$(basename ${filepath} .tar)
  dirpath="$(dirname ${filepath})/${filename}"
  mkdir ${dirpath}
  tar -xvf ${filepath} -C ${dirpath}
  rm ${filepath}
done

