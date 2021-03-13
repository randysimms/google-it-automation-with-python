import pytest
from health_check import *

sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."


@pytest.mark.order(1)
def test_check_disk():
    if check_disk(disk="F:\\", min_gb=10, min_percent=20) is False:
        send_email(generate_email(sender, recipient, "Error - Available disk space is less than 20%", body, ""))


def test_check_memory():
    if check_memory(min_available=500000000) is False:
        send_email(generate_email(sender, recipient, "Error - Available memory is less than 500MB", body, ""))


def test_check_cpu():
    if check_cpu(max_percent=80) is False:
        send_email(generate_email(sender, recipient, "Error - CPU usage is over 80%", body, ""))


def test_check_resolve_hostname():
    if check_resolve_hostname('localhost', '127.0.0.1') is False:
        send_email(generate_email(sender, recipient, "Error - localhost cannot be resolved to 127.0.0.1", body, ""))
