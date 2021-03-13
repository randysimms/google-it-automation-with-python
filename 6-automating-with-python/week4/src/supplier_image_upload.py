#!/usr/bin/env python3

import requests
import socket
import os
import glob
import sys


# process images
def upload_images(fn_pattern,endpoint):
    for fn in glob.glob(fn_pattern):
        fn_norm = os.path.normpath(fn)
        print("uploading {}...".format(fn_norm))
        with open(fn_norm, 'rb') as opened:
            response = requests.post(endpoint, files={'file': opened})
        print("reponse is: {} \n\t with reason: {}".format(response.status_code,response.reason))

        if response.status_code != 201:
            return False
    return True

def main():
    endpoint = "http://" + socket.gethostname() + "/upload/"
    upload_images("supplier-data/images/*.jpeg", endpoint)


if __name__ == "__main__":
    main()