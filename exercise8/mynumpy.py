import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("image.jpg")

red_channel = img[:, :, 0]  
green_channel = img[:, :, 1] 
blue_channel = img[:, :, 2] 
red_values = red_channel.flatten()
green_values = green_channel.flatten()
blue_values = blue_channel.flatten()
red_hist, _ = np.histogram(red_values, bins=256, range=(0, 256))
green_hist, _ = np.histogram(green_values, bins=256, range=(0, 256))
blue_hist, _ = np.histogram(blue_values, bins=256, range=(0, 256))

bins = np.arange(256) 
plt.figure(figsize=(10, 5))  # גודל הגרף

plt.plot(bins, red_hist, color='red', label='Red')
plt.plot(bins, green_hist, color='green', label='Green')
plt.plot(bins, blue_hist, color='blue', label='Blue')

plt.title("RGB Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Number of Pixels")
plt.legend()
plt.show()
