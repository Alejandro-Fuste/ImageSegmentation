import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images
image_paths = ["./images/bear_grayscale.jpg", "./images/golfer_grayscale.jpg", "./images/lions_grayscale.jpg"]
images = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in image_paths]  # Convert to grayscale and NumPy array


# Function to plot histogram
def plot_histogram(image, title):
    plt.figure()
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='gray')
    plt.title(f"Histogram of {title}")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()


# Function to perform thresholding
def apply_threshold(image, threshold):
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return binary_image


# Iterate through images
for idx, image in enumerate(images):
    # Plot histogram
    plot_histogram(image, f"Image {idx + 1}")

    # Choose three thresholds manually based on the histogram
    thresholds = [50, 178, 60]  # Replace with actual thresholds based on the histograms
