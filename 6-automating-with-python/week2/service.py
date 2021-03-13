#!/usr/bin/env python3

import requests
import sys
import os
import json

'''
What you’ll do
Use the Python OS module to process a directory of text files 
Manage information stored in Python dictionaries
Use the Python requests module to upload content to a running Web service
Understand basic operations for Python requests like GET and POST methods 
    
The reviews are stored in text files in the local disk.
Your script should open those files, process the information to turn it into the format expected by the web service,
then send it to the web service to get stored.

The whole website is stored in /projects/corpweb.
reviews are at:  /data/feedback
'''


def get_review(fn):
    '''
    Traverse over each file and, from the contents of these text files, create a dictionary with keys of:
      title, name, date, and feedback (respectively)
    '''
    review = {}
    with open(fn, "r") as file:
        contents_split = file.read().splitlines()
    if len(contents_split) == 4:
        #review["id"] = os.path.splitext(fn)[0].split("/",1)[1]
        review["title"] = contents_split[0]
        review["name"] = contents_split[1]
        review["date"] = contents_split[2]
        review["feedback"] = contents_split[3]

    return review


def main():
    sourcedir = "."
    server_ip = "localhost"

    if len(sys.argv) == 2:
        sourcedir = sys.argv[1]
    elif len(sys.argv) > 2:
        sourcedir = sys.argv[1]
        server_ip = sys.argv[2]

    # gather text files and convert to JSON
    for entry in os.listdir(sourcedir):
        print(entry)

        review = get_review(os.path.join(sourcedir,entry))
        # send to Django
        #jsonData = json.dumps(review)
        response = requests.post("http://" + server_ip + "/feedback/", json=review)
        #  .format(IP_ADDRESS)
        print("Status code: ", response.status_code)

    #print(review)

print("DONE!")

if __name__ == "__main__":
    main()
