#!/usr/bin/env python3

import os
import sys

from PIL import Image
import glob

"""
  From images and descriptions of new products, you’ll:

  * Convert .TIF 3000x2000 images to smaller JPG 600x400 pixels.
  * Convert .TXT and the JPG into HTML file.
  * Upload the new products to your online store. Images and descriptions should use independent web endpoints.
  * Create a PDF report of uploads with the name of each fruit and its total weight (in lbs). 
  * Email PDF to supplier with the total uploaded weight in lbs.
  * Run a script on your web server to monitor system health, send email to alert problems.

    supplier data at:  https://drive.google.com/file/d/1LePo57dJcgzoK4uiI_48S01Etck7w_5f


"""


def convert_image(fn_pattern,dest_format,sizes):
    print("")
    for fn in glob.glob(fn_pattern):
        fn_norm = os.path.normpath(fn)
        im = Image.open(fn_norm)
        source_format = im.format
        print("Converting {} from {} to {}...".format(fn_norm, source_format, dest_format))
        rgb_im = im.convert('RGB')
        rgb_im = rgb_im.resize((sizes[0], sizes[1]))
        destpath = os.path.splitext(fn_norm)[0]+"."+dest_format
        rgb_im.save(destpath)

        #verify
        im = Image.open(destpath)
        assert( im.format == "JPEG")
        assert( im.size == (600,400) )

    return True


def main(argv):
    fn = "../supplier-data/images/*.tiff"


if __name__ == "__main__":
    main(sys.argv)