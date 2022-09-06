import numpy as np
from PIL import Image
import cv2


def correct_image(img: Image, equalization: bool = False,
                  gaussian_blur: bool = False, median_blur: bool = False) -> Image:
    image = np.array(img)
    image = __set_grayscale(image)
    if equalization:
        image = __equalization(image)
    if gaussian_blur:
        image = __gaussian_blur(image)
    if median_blur:
        image = __median_blur(image)

    return Image.fromarray(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))


def __set_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def __equalization(img):
    return cv2.equalizeHist(img)


def __gaussian_blur(img):
    return cv2.GaussianBlur(img, (5, 5), 1)


def __median_blur(img):
    return cv2.medianBlur(img, 5)


def __opening(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


def __dilate(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)
