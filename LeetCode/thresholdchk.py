import cv2
import numpy as np

# Load the image of the OMR sheet
img = cv2.imread('Latest.jpg')

# Preprocess the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

equalized = clahe.apply(gray)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Variables to store the total and marked bubble counts
total_bubbles = 0
marked_bubbles = 0
# block_size = 11
# c_value = 2
# Try out different values for blockSize and C parameters
for block_size in range(3, 16, 2):
    for c_value in range(-3, 4):
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, blockSize=block_size, C=c_value)
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        dilation = cv2.dilate(opening, kernel, iterations=1)

# Locate the bubbles in the image
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
bubble_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if 100 < area < 1000:
        bubble_contours.append(contour)
        total_bubbles += 1

# Count the number of marked bubbles
num_marked = 0
for i, bubble_contour in enumerate(bubble_contours):
    (x, y, w, h) = cv2.boundingRect(bubble_contour)
    roi = dilation[y:y+h, x:x+w]
    circles = cv2.HoughCircles(roi, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    if circles is not None:
        num_marked += 1
        marked_bubbles += 1

# Draw contours of marked bubbles on the image
marked_img = img.copy()
cv2.drawContours(marked_img, bubble_contours, -1, (0, 255, 0), 2)

# Display the image with marked bubbles and counts
cv2.putText(marked_img, f"Total Bubbles: {total_bubbles}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
cv2.putText(marked_img, f"Marked Bubbles: {num_marked}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
cv2.imshow(f"Block size: {block_size}, C value: {c_value}", marked_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Print the total and marked bubble counts after the loop finishes
print("Total Bubbles:", total_bubbles)
print("Marked Bubbles:", marked_bubbles)

# import cv2
# import numpy as np
#
# # Load the image of the OMR sheet
# img = cv2.imread('Latest.jpg')
#
# # Preprocess the image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print("Original image shape:", gray.shape)
#
# # Apply adaptive histogram equalization
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# equalized = clahe.apply(gray)
# print("Equalized image shape:", equalized.shape)
#
# blur = cv2.GaussianBlur(equalized, (5, 5), 0)
#
# # Variables to store the total and marked bubble counts
# total_bubbles = 0
# marked_bubbles = 0
# block_size = 11
# c_value = 2
#
# thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, blockSize=block_size, C=c_value)
# kernel = np.ones((3, 3), np.uint8)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
# dilation = cv2.dilate(opening, kernel, iterations=1)
#
# # Locate the bubbles in the image
# contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print("Number of contours found:", len(contours))
#
# bubble_contours = []
# for i, contour in enumerate(contours):
#     area = cv2.contourArea(contour)
#     print("Area of contour", i+1, ":", area)
#     if 100 < area < 1000:
#         bubble_contours.append(contour)
#         total_bubbles += 1
#
#
# # Count the number of marked bubbles
# num_marked = 0
# for i, bubble_contour in enumerate(bubble_contours):
#     (x, y, w, h) = cv2.boundingRect(bubble_contour)
#     roi = dilation[y:y+h, x:x+w]
#     circles = cv2.HoughCircles(roi, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
#     if circles is not None:
#         num_marked += 1
#         marked_bubbles += 1
#
#         # Print the number of circles detected in each contour
#         print("Number of circles in contour", i+1, ":", len(circles))
#
# # Draw contours of marked bubbles on the image
# marked_img = img.copy()
# cv2.drawContours(marked_img, bubble_contours, -1, (0, 255, 0), 2)
#
# # Display the image with marked bubbles and counts
# cv2.putText(marked_img, f"Total Bubbles: {total_bubbles}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
# cv2.putText(marked_img, f"Marked Bubbles: {num_marked}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
# cv2.imshow(f"Block size: {block_size}, C value: {c_value}", marked_img)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()
#
# # Print the total and marked bubble counts after the loop finishes
# print("Total Bubbles:", total_bubbles)
# print("Marked Bubbles:", marked_bubbles)
