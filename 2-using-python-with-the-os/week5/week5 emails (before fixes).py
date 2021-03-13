#!/usr/bin/env python3

import csv
import sys


def populate_dictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  email_dict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      email_dict[name] = row[1]
  return email_dict

def find_email(argv):
    """ Return an email address based on the username given."""
    # Create the username based on the command line input.
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    datadir = ""
    #datadir = "/home/{{ username }}/data/"
    email_dict = populate_dictionary(datadir + 'user_emails2.csv')
    # Find and print the email
    return email_dict.get(fullname.lower())

def main():
  print(find_email(sys.argv))

if __name__ == "__main__":
  main()