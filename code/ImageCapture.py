import cv2


class ImageCapture:
    def __init__(self):
        # Camera 0 is the integrated web cam on my netbook
        self.camera_port = 0

        # Number of frames to throw away while the camera adjusts to light levels
        self.ramp_frames = 30

        # Now we can initialize the camera capture object with the cv2.VideoCapture class.
        # All it needs is the index to a camera port.
        self.camera = cv2.VideoCapture(self.camera_port)

    # Captures a single image from the camera and returns it in PIL format
    def get_image(self):
        # read is the easiest way to get a full image out of a VideoCapture object.
        retval, im = self.camera.read()
        return im

    def save_image(self, path, limit):
        for j in range(limit):
            # Ramp the camera - these frames will be discarded and are only used to allow v4l2
            # to adjust light levels, if necessary
            for i in range(self.ramp_frames):
                temp = self.get_image()
            print("Taking image...")
            # Take the actual image we want to keep
            camera_capture = self.get_image()
            file = path + str(j) + ".png"
            # A nice feature of the imwrite method is that it will automatically choose the
            # correct format based on the file extension you provide. Convenient!
            cv2.imwrite(file, camera_capture)

        # release the camera
        del (self.camera)
