

import changeImage
import pytest


@pytest.mark.order(1)
def test_convert_one_image():
    fn = "../supplier-data/images/001.tiff"
    assert (changeImage.convert_image(fn, "jpeg", (600, 400)) == True)


@pytest.mark.order(2)
def test_convert_many_images():
    fn = "../supplier-data/images/*.tiff"
    assert (changeImage.convert_image(fn, "jpeg", (600, 400)) == True)


