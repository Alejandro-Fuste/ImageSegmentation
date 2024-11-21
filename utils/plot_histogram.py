import matplotlib.pyplot as plt


# Function to plot histogram
def plot_histogram(image, title):
    plt.figure()
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='gray')
    plt.title(f"Histogram of {title}")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.show()
