#!/bin/python3
import os

if __name__ == "__main__":
    outfile = "./wnid_label.csv"
    if os.path.exists(outfile):
        os.remove(outfile)
    in_file = open(file="./wnid.csv", mode="rt")
    out_file = open(file=outfile, mode="a+")

    label_number = 0
    for line in in_file:
        newline = line.rstrip("\n") + "," + str(label_number) + "\n"
        out_file.write(newline)
        label_number += 1

