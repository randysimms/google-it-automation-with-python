
import pytest
from supplier_image_upload import upload_images


@pytest.mark.order(3)
def test_upload_one_image():
    fn = "../supplier-data/images/001.jpeg"
    endpoint = "https://my-json-server.typicode.com/randysimms/mockend-randy/upload"
    assert( upload_images(fn,endpoint) == True )


@pytest.mark.order(4)
def test_upload_many_images():
    pattern = "../supplier-data/images/*.jpeg"
    endpoint = "https://my-json-server.typicode.com/randysimms/mockend-randy/upload"
    assert( upload_images(pattern,endpoint) == True )

