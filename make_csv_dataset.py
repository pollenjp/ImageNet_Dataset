#!/bin/python3
import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--search_path', action='store', nargs=None, const=None, default=None, type=str,
                        choices=None, required=True,  help='search path')
    parser.add_argument('--output_file', action='store', nargs=None, const=None, default="dataset.csv", type=str,
                        choices=None, required=True,  help='search path')
    args = parser.parse_args()

    search_path = args.search_path
    output_file = args.output_file

    # WorldNet ID - label number (0-999)

    # search and append to CSV file
    for _dirpath, _, _filenames in os.walk(search_path):
        for _filename in _filenames:
            if re.search(r'.*\.JPEG', _filename):
                # CSVに追記
                #  - fullpath, label(0-999)






