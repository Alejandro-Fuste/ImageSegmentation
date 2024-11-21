import cv2
from skimage.filters import threshold_otsu
from utils.image_utils import display_image


# Function to apply Otsu's thresholding on a grayscale image
def otsu_threshold(image):
    # Compute the Otsu's threshold value using scikit-image
    threshold_value = threshold_otsu(image)

    # Apply the threshold using OpenCV's cv2.threshold function
    # Pixels below the threshold are set to 0 (black), above are set to 255 (white)
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Return the binary image and the computed threshold value
    return binary_image, threshold_value


# Function to process an image using Otsu's thresholding and display the results
def process_otsu_threshold(image, image_index):
    # Apply Otsu's thresholding to the input image
    binary_image, threshold_value = otsu_threshold(image)

    # Print the threshold value to the console
    print(f"Otsu's Threshold Value for Image {image_index}: {threshold_value}")

    # Display the binary image with a title indicating Otsu's thresholding result
    display_image(binary_image, f"Otsu's Thresholding - Image {image_index}")
