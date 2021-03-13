

from run import uploadTexts
import pytest


@pytest.mark.order(5)
def test_upload_text():
    fn = "../supplier-data/descriptions/001.txt"
    endpoint = "https://my-json-server.typicode.com/randysimms/mockend-randy/fruit/"
    assert ( uploadTexts(fn, endpoint) == True)


@pytest.mark.order(6)
def test_upload_texts():
    fn = "../supplier-data/descriptions/*"
    endpoint = "https://my-json-server.typicode.com/randysimms/mockend-randy/fruit/"
    assert (uploadTexts(fn, endpoint) == True)