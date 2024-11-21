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

# Iterate through images
# for idx, image in enumerate(images):
#     # Plot histogram
#     plot_histogram(image, f"Image {idx + 1}")
#
#     # Choose three thresholds manually based on the histogram
#     thresholds = [70, 148, 100]  # Replace with actual thresholds based on the histograms
#
#     # Display original image
#     plt.figure(figsize=(10, 5))
#     plt.subplot(1, 4, 1)
#     plt.imshow(image, cmap='gray')
#     plt.title("Original")
#     plt.axis('off')
#
#     # Apply thresholds and display results
#     for i, t in enumerate(thresholds):
#         binary_image = apply_threshold(image, t)
#         plt.subplot(1, 4, i + 2)
#         plt.imshow(binary_image, cmap='gray')
#         plt.title(f"Threshold {t}")
#         plt.axis('off')
#
#     plt.tight_layout()
#     plt.show()
