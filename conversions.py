import cv2

# Read an image
image_rgb = cv2.imread('SPS_75Years.png')

# Convert to grayscale
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

print(image_rgb.shape)

# Display the grayscale image
cv2.imshow('Grayscale Image', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
