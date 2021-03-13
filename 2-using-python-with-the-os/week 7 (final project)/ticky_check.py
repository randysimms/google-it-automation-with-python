#!/usr/bin/env python3

import csv
import operator
import re
import sys
import csv_to_html

errmsg = {}     # error message dictionary
userstats = {}  #user stats dictionary

errmsg_csv = "error_message.csv"
userstats_csv = "user_statistics.csv"

errmsg_html = "error_message.html"
userstats_html = "user_statistics.html"

# load file
def read_log(log):
    try:
        with open(log) as file:
            for line in file:
                result = re.search(r"ticky: ([A-Z]{4,}) (.*) \(([\w]*)\)", line)
                if result != None:
                    level = result.group(1)  #error level; INFO or ERROR
                    msg = result.group(2)  #msg
                    user = result.group(3)  #username

                    if user not in userstats:
                        userstats[user] = {"INFO": 0, "ERROR": 0}

                    if level == "ERROR":
                        #errmsg[user] = errmsg.get(user, 0) + 1
                        # Error Message report: find ERROR messages and count them
                        errmsg[msg] = errmsg.get(msg, 0) + 1
                        #User stats report: add to error count for user
                        userstats[user][level] += 1
                    elif level == "INFO":
                        #User stats report: find username, INFO msg count, and ERROR message counts for each user
                        userstats[user][level] += 1

        #print(errmsg)
        #print(userstats)
    except:
        print("ERROR: Exiting...")
        raise

#end read_log

#Here, the dictionaries will be sorted
def sort_dicts():
    sorted(userstats.items())
    sorted(errmsg.items(), key = operator.itemgetter(1), reverse = True)
#end def

def list_to_csv(report_list, filename):
    try:
        with open( filename, "w") as file:
            writer = csv.writer(file)
            writer.writerows(report_list)
    except IOError:
        print("I/O error")


if __name__ == "__main__":
    read_log(sys.argv[1])

    # create report 1 in csv file
    print("create report 1...")
    #sort from dict to list, using field 2
    errmsg_sorted = sorted(errmsg.items(), key=operator.itemgetter(1), reverse=True)
    # header row
    errmsg_sorted.insert(0, ("Error","Count") )
    print(errmsg_sorted)
    #write to csv
    list_to_csv(errmsg_sorted,errmsg_csv)  #list of lists


    # create report 2 in csv file
    print("create report 2...")
    #sort from dict to list, using field 1
    userstats_sorted = sorted(userstats.items(), key=operator.itemgetter(0), reverse=False)
    #untangle (geez!) the list of tuples(with string and dict inside), convert to straight list
    for i in range(len(userstats_sorted)):
        user = userstats_sorted[i][0]
        info_count = userstats_sorted[i][1]["INFO"]
        err_count = userstats_sorted[i][1]["ERROR"]
        userstats_sorted[i] = [user,info_count,err_count]
    #write to csv
    userstats_sorted.insert(0,("Username","INFO","ERROR") )  #header row
    print(userstats_sorted)
    list_to_csv(userstats_sorted,userstats_csv)


 # Process the data and turn it into an HTML
    csv_to_html.convert(userstats_csv, userstats_html)
    csv_to_html.convert(errmsg_csv, errmsg_html)





