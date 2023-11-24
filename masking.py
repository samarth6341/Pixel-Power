import cv2
import numpy as np

# Read the image
image = cv2.imread("SPS_75Years.png")

# Convert BGR image to HSV (Hue, Saturation, Value) color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the blue color range in HSV
lower_blue = np.array([100, 50, 50])  # Lower bounds for blue in HSV
upper_blue = np.array([140, 255, 255])  # Upper bounds for blue in HSV

# Create a mask to identify blue pixels
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply the mask to the original image to extract blue regions
result = cv2.bitwise_and(image, image, mask=mask)

# Display the resulting image with only blue areas
cv2.imshow('Blue Only', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
