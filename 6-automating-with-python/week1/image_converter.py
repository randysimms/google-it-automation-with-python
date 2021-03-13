
import PIL
from PIL import Image
import os
import sys
import imghdr

"""
Randy Simms 2021/3/5

The images received are in the wrong format:
  .tiff format
  Image resolution 192x192 pixel (too large)
  Rotated 90° anti-clockwise

The images required for the launch should be in this format:
  .jpeg format
  Image resolution 128x128 pixel
  Should be straight


get the images for testing from:

   https://drive.google.com/file/d/11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF/view
"""

def main():
    source_dir = "."
    save_dir = "/opt/icons/"


    if len(sys.argv) == 2:
        source_dir = sys.argv[1]
    elif len(sys.argv) > 2 :
        source_dir = sys.argv[1]
        save_dir = sys.argv[2]

    #print(PIL.PILLOW_VERSION)
    #print( "features: {}".format(Image.features.pilinfo(out=None, supported_formats=True)))

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    #process each file in source directory
    for dirName, subdirList, fileList in os.walk(source_dir):
        print('Found directory: %s' % dirName)

        for fname in fileList:
            sourcepath = os.path.join(dirName, fname)
            fmt = imghdr.what(sourcepath)
            if fmt == "tiff":

                im = Image.open(sourcepath)

                sourcefmt = im.format
                savefmt = "JPEG"
                print("Converting {} from {} to {}...".format(sourcepath,sourcefmt,savefmt))

                rgb_im = im.convert('RGB')
                rgb_im = rgb_im.rotate(-90)
                rgb_im = rgb_im.resize((128, 128))

                #suffix = '.jpg'
                destpath = os.path.join(save_dir, fname )
                rgb_im.save(destpath, savefmt)  # this converts png image as jpeg

    print("DONE!")

if __name__ == "__main__":
    main()

