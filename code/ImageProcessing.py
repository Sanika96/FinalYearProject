import cv2


class ImageProcessing:
    def read_image(self, image_path):
        image = cv2.imread(image_path)
        return image

    def to_grayscale(self, image, destination_path):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grayscale_image_path = destination_path + 'gray_image.png'
        cv2.imwrite(grayscale_image_path, gray_image)
        return gray_image
        os.path.join
        # cv2.imshow('gray_image',gray_image)

    def grayscale_to_blur(self, gray_image, destination_path):
        blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        blur_image_path = destination_path + 'blur_image.png'
        cv2.imwrite(blur_image_path, blur_image)
        return blur_image
        # cv2.imshow('blur_image',blur_image)

    def blur_to_edged(self, blur_image, destination_path):
        edged_image = cv2.Canny(blur_image, 75, 200)
        edged_image_path = destination_path + 'edged_image.png'
        cv2.imwrite(edged_image_path, edged_image)
        return edged_image
        # cv2.imshow('edged_image',edged_image)

    # cv2.imshow('color_image',image)
