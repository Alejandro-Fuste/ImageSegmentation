import matplotlib.pyplot as plt
import cv2


# Function to plot histogram
def plot_histogram(image, title):
    plt.figure()
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='gray')
    plt.title(f"Histogram of {title}")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()


# Function to load image
def load_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Image at {image_path} could not be loaded.")
    return image


# Function to display image
def display_image(image, title):
    plt.figure()
    plt.title(title)
    plt.imshow(image, cmap='gray')
    plt.show()
