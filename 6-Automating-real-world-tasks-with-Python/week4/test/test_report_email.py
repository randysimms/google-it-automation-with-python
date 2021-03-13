from report_email import main
import pytest


@pytest.mark.order(7)
def test_send_report():
    assert (main("..\\src\\processed.pdf") == True)
