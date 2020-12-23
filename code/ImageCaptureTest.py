import unittest
import os.path as osp

from Services.ImageCapture import ImageCapture



class ImageCaptureTest(unittest.TestCase):
    def test_image_is_stored(self):
        # Arrange
        image_capture = ImageCapture()
        path = "/home/apekksha/SLC/data/"
        limit = 10

        # Act
        image_capture.save_image(path, limit)

        # Assert
        self.assertTrue(all(osp.exists(path + str(i) + '.png') for i in range(limit)), "Images are not stored")


if __name__ == '__main__':
    unittest.main()
