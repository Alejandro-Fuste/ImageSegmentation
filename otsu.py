import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu


# Helper function for Otsu's thresholding
def otsu_threshold(image):
    threshold_value = threshold_otsu(image)
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image, threshold_value


