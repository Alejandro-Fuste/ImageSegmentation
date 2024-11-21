from utils.image_utils import plot_histogram, load_image
from thresholding.binarization import process_binary_threshold
from thresholding.otsu import process_otsu_threshold


# function to apply both binarization and Otsu thresholding
def process_images(image_paths):
    # Three thresholds chosen manually based on the histogram
    thresholds = [70, 148, 100]

    for idx, image_path in enumerate(image_paths):
        try:
            # Load the image
            image = load_image(image_path)

            # Plot the histogram
            plot_histogram(image, f"Histogram for Image {idx + 1}")

            # Perform Binarization Thresholding
            process_binary_threshold(image, thresholds, idx + 1)

            # Perform Otsu's Thresholding
            process_otsu_threshold(image, idx + 1)

        except FileNotFoundError as e:
            print(e)


if __name__ == "__main__":
    image_paths = ["./images/bear_grayscale.jpg", "./images/golfer_grayscale.jpg", "./images/lions_grayscale.jpg"]
    process_images(image_paths)
