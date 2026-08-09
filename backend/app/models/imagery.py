"""class SatelliteImage:
    def __init__(self, source, cloud_coverage, date):
        self.source = source,
        self.cloud_covergae = cloud_coverage,
        self.date = date"""

import cv2
import numpy as np

def calculate_brightness(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(
        image, 
        cv2.COLOR_BGR2GRAY
    )
    brightness = np.mean(gray)
    return float(brightness)

def calculate_edge_density(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )
    edges = cv2.Canny(
        gray,
        100,
        200
    )
    edge_pixels = np.sum(edges > 0)
    total_pixels = edges.shape[0] * edges.shape[1]
    density = edge_pixels / total_pixels
    return float(density)

def analyze_image(image_path):
    brightness = calculate_brightness(image_path)
    edge_density = calculate_edge_density(image_path)
    return {
        "brightness": brightness,
        "edge_density": edge_density
    }