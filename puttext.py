import cv2

# Read an image
image = cv2.imread('SPS_75Years.png')

# Add text to the image
text = 'Pixel Power!'
position = (50, 50)  # (x, y) coordinates for text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 0, 0)  # BGR color
thickness = 2

cv2.putText(image, text, position, font, font_scale, color, thickness)

# Display the image with text
cv2.imshow('Image with Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
