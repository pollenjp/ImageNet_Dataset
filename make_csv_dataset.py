#!/bin/python3
import os
import argparse
import csv
import re


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--search_path', action='store', nargs=None, const=None, default=None, type=str,
                        choices=None, required=True,  help='search path')
    parser.add_argument('--wnid_label_filepath', action='store', nargs=None, const=None, default="dataset.csv",
                        type=str, choices=None, required=True,  help='')
    parser.add_argument('--output_filepath', action='store', nargs=None, const=None, default="dataset.csv", type=str,
                        choices=None, required=True,  help='')
    args = parser.parse_args()

    search_path         = args.search_path
    wnid_label_filepath = args.wnid_label_filepath
    output_file         = args.output_filepath

    # dict : WorldNet ID - label number (0-999)
    with open(file=wnid_label_filepath, mode="rt") as f:
        lines = csv.reader(f)
        wnid_label_dict = {rows[0]:rows[1] for rows in lines}
        #label_wnid_dict = {rows[1]:rows[0] for rows in lines}

    # search and append to CSV file
    if os.path.exists(output_file):
        os.remove(output_file)
    out_f = open(file=output_file, mode="a+")
    for _dirpath, _, _filenames in os.walk(search_path):
        for _filename in _filenames:
            if re.search(r'.*\.JPEG', _filename):
                print(_filename)
                # CSVに追記
                #  - fullpath, label(0-999)
                wnid = os.path.basename(_dirpath)
                fullpath = os.path.abspath(_dirpath) + "/" + _filename
                out_f.write(fullpath + " " + wnid_label_dict[wnid] + "\n")
    out_f.close()


