#!/usr/bin/env python3

import os
import shutil
import sys

def check_reboot():
    '''Returns True if the computer has a pending reboot'''
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_gb,min_percent):
    '''return true if there is not enough disk space, False otherwsie'''
    du = shutil.disk_usage(disk)
    #calc the percent of free space
    percent_free = 100 * du.free / du.total
    #cal how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def main():

    allsgood = True

    if check_reboot():
        print("Pending reboot.")
        allsgood = False

    if check_disk_full(disk="F:\\",min_gb=2,min_percent=40):
        print("Disk full.")
        allsgood = False

    if not allsgood:
        sys.exit(1)

    print("Everything ok.")
    sys.exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

