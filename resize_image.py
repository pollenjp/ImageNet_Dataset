import argparse
import csv
import cv2


def resize256x256(img_path):
    im = cv2.imread(img_path)
    assert im is not None
    im = cv2.resize(im, (256, 256))
    cv2.imwrite(img_path, im)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--imagepath_filepath', action='store', nargs=None, const=None, default="",
                        type=str, choices=None, required=True,  help='')
    args = parser.parse_args()

    imagepath_filepath = args.imagepath_filepath

    with open(file=imagepath_filepath, mode="rt") as f:
        reader = csv.reader(f, delimiter=" ")
        for rows in reader:
            print(rows[0])
            resize256x256(img_path=rows[0])

