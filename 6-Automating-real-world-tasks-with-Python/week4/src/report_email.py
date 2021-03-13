#!/usr/bin/env python3

from emails import generate_email, send_email
from reports import generate_report
import glob
import datetime
import email
import os
import sys

"""
    * process descriptions
    * make pdf
"""


def process_descriptions(path):
    body = ""
    print("")
    for filename in glob.glob(path, recursive=True):
        norm_fn = os.path.normpath(filename)
        with open(norm_fn, "r") as file:
            contents_split = file.read().splitlines()
        name = contents_split[0]
        weight = contents_split[1]
        body += "<br />" + "name: " + name + "<br />" + "weight: " + weight +  "<br />"

    print("Processed {}...".format(norm_fn))

    return body


def main(fn_report):
    pathtotxt = "../supplier-data/descriptions/*.txt"
    body = process_descriptions(pathtotxt)
    generate_report(attachment=fn_report,
                    title="Processed Update on {}".format(datetime.date.today().strftime("%m/%d/%y")), paragraph=body)
    body =  "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = generate_email(sender="automation@example.com", recipient="{}@example.com".format(os.environ.get('USER')),
                   subject="Upload Completed - Online Fruit Store", body=body, attachment_path=fn_report)
    send_email(message)

    return True


if __name__ == '__main__':
    main()