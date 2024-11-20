import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the images
image_paths = ["./images/bear_grayscale.jpg", "./images/golfer_grayscale.jpg", "./images/lions_grayscale.jpg"]
images = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in image_paths]





