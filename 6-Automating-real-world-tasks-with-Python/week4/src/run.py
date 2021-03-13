#!/usr/bin/env python3

import json
import requests
import socket
import os
import sys
import datetime
import glob

def uploadTexts(paths, endpoint):
   #for root, directories, files in os.walk(paths, topdown=False):
    print("")
    noerrors = False
    for filename in glob.glob(paths,recursive=True):
        norm_fn = os.path.normpath(filename)
        #full_fn = os.path.join(os.path.abspath(root),fn)
        print("uploading {}...".format(norm_fn))
        #For each file, create a dictionary of:  name, weight, description, and image_name
        fruit = {}
        with open(norm_fn, "r") as file:
            contents_split = file.read().splitlines()
        if len(contents_split) >= 3:
            fruit["id"] = datetime.datetime.now().strftime('%Y%m-%d%H-%M%S')
            fruit["name"] = contents_split[0]
            fruit["weight"] = contents_split[1].split(" ")[0]  #only return the integer portion
            fruit["description"] = contents_split[2]
            fruit["image_name"] = os.path.splitext(norm_fn)[0] + ".jpg"
            response = requests.post(endpoint, json=fruit)
        else:
            print("ERROR: not enough data in description for {}".format(norm_fn))
            noerrors = False
        print("reponse is: {} \n\t with reason: {}".format(response.status_code,response.reason))
        if ( response.status_code != 201 ):
            return False
        noerrors = True

    return noerrors

def main():
    response = uploadTexts("../supplier-data/descriptions", "http://" + socket.gethostname() + "/fruits/")


if __name__ == "__main__":
    main(sys.argv)