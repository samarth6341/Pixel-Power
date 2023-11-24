import cv2

# Read an image in color
image = cv2.imread('SPS_75Years.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow('Binary Image', binary_image)

# Display the original and grayscale images
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
