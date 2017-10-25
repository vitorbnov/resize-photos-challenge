import os
import sys
import unittest
import PIL

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import photos_resizer


class PhotosResizerTest(unittest.TestCase):

    def test_image_opening_from_url(self):
        image_url = "https://www.python.org/static/opengraph-icon-200x200.png"
        image = photos_resizer.open_image_from_url(image_url)

        self.assertEqual(type(image), PIL.PngImagePlugin.PngImageFile)

    def test_image_resizing(self):
        image = PIL.Image.open("static/images/Foo_was_here.jpg")
        new_size = (100, 100)
        new_image = photos_resizer.resize_image(image, new_size)

        self.assertEqual(new_image.size, new_size)

    def test_suffix_appending_to_filename(self):
        filename = "name.format"
        suffix = "_suffix"
        new_filename = photos_resizer.append_suffix_to_filename(filename, suffix)

        self.assertEqual(new_filename, "name_suffix.format")


if __name__ == "__main__":
    unittest.main()
