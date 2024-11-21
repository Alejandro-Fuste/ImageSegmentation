import cv2
from utils.image_utils import display_image


# Function to perform binary thresholding
def binary_threshold(image, thresholds):
    results = []
    for threshold in thresholds:
        _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        results.append((binary_image, threshold))
    return results


def process_binary_threshold(image, thresholds, image_index):
    results = binary_threshold(image, thresholds)
    for binary_image, threshold in results:
        display_image(binary_image, f"Simple Threshold {threshold} - Image {image_index}")


