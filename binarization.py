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
    thresholds = [70, 148, 100]  # Replace with actual thresholds based on the histograms

    # Display original image
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 4, 1)
    plt.imshow(image, cmap='gray')
    plt.title("Original")
    plt.axis('off')

    # Apply thresholds and display results
    for i, t in enumerate(thresholds):
        binary_image = apply_threshold(image, t)
        plt.subplot(1, 4, i + 2)
        plt.imshow(binary_image, cmap='gray')
        plt.title(f"Threshold {t}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

