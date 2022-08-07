import numpy as np
from PIL import Image
import cv2


def correct_image(img: Image) -> Image:
    image = np.array(img)
    image = _set_grayscale(image)
    image = _equalization(image)
    image = _gaussian_blur(image)
    # image = _median_blur(image)

    return Image.fromarray(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))


def _set_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def _equalization(img):
    return cv2.equalizeHist(img)


def _gaussian_blur(img):
    return cv2.GaussianBlur(img, (5, 5), 1)


def _median_blur(img):
    return cv2.medianBlur(img, 5)


def _opening(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


def _dilate(img):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)
