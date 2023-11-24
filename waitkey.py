import cv2

# Read an image
image = cv2.imread('SPS_75Years.png')

# Display the image
cv2.imshow('Image', image)



# Wait for a key event for 3000 milliseconds (3 seconds)
cv2.waitKey(3000)

# Close all OpenCV windows
cv2.destroyAllWindows()
