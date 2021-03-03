#!/usr/bin/env python3


import csv
import datetime
from collections import defaultdict

import requests


FILE_URL = "https://raw.githubusercontent.com/google/it-cert-automation-practice/master/Course4/Lab4/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int( input('Enter a value for the year: '))
    month = int( input('Enter a value for the month: '))
    day = int( input('Enter a value for the day: '))
    print()

    #print("You selected: {}/{}/{}".format(month,day,year))
    target_date = datetime.datetime(year, month, day)
    return target_date

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()

    events = defaultdict(list) #dict of key and list of employees
    #min_date_employees = []

    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        #if row_date earlier or same as entered date, put in dict
        if row_date >= start_date:
            events[row_date].append("{} {}".format(row[0], row[1]))  #append the employee

    return events


def list_newer(start_date):

        events = get_same_or_newer(start_date)
        sorted_items = sorted(events.items())  # sort by date

        for start_date,employees in sorted_items:
            print("Started on {}: {}".format( start_date, employees))


def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()

