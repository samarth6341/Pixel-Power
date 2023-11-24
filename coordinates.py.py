import cv2

# Mouse callback function
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button clicked
        print(f"Coordinates: ({x}, {y})")

# Read an image
image = cv2.imread('SPS_75Years.png')

# Display the image and set the mouse callback
cv2.imshow('Image', image)
cv2.setMouseCallback('Image', get_coordinates)

# Wait for a user to press any key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()