#!/usr/bin/env python3

import os
import shutil
import psutil
import sys
import socket

from emails import generate_email, send_email


def check_reboot():
    '''Returns True if the computer has a pending reboot'''
    return os.path.exists("/run/reboot-required")


def check_disk(disk,min_gb,min_percent):
    '''return False if there is not enough disk space, True otherwsie'''
    du = shutil.disk_usage(disk)
    #calc the percent of free space
    percent_free = 100 * du.free / du.total
    #cal how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return False
    return True


def check_memory(min_available):
    available = psutil.virtual_memory().available
    return ( available > min_available)


def check_cpu(max_percent):
    cpu_percent = psutil.cpu_percent(interval=1)
    return (cpu_percent < max_percent)


def check_resolve_hostname(hostname, ip):
    resolved_ip = socket.gethostbyname(hostname)
    return (ip == resolved_ip)


def main():
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    if check_cpu(max_percent=80) is False:
        send_email(generate_email(sender,recipient,"Error - CPU usage is over 80%", body,""))
    if check_disk(disk="F:\\", min_gb=0, min_percent=20) is False:
        send_email(generate_email(sender,recipient,"Error - Available disk space is less than 20%",body,""))
    if check_memory(min_available=500000000) is False:
        send_email(generate_email(sender, recipient, "Error - Available memory is less than 500MB", body,""))
    if check_resolve_hostname('localhost', '127.0.0.1') is False:
        send_email(generate_email(sender, recipient, "Error - localhost cannot be resolved to 127.0.0.1", body,""))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


