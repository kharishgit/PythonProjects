# import cv2
# import numpy as np
#
# image = cv2.imread('omr1.jpeg')
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# max = 0
# mt1 = 0
# mt2 = 0
# mx = 0
# my = 0
#
# # Display the grayscale image
# def blurred(x, y):
#     blurred_image = cv2.GaussianBlur(gray_image, (x, y), 0)
#
#     # Perform edge detection using Canny
#     def detectcircle(t1=70, t2=70):
#         global max
#         global mt1
#         global mt2
#         global mx
#         global my
#
#         # Perform edge detection using Canny
#         edges = cv2.Canny(blurred_image, threshold1=t1, threshold2=t2)
#
#         # Find contours in the edge image
#         contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#         # Iterate over the contours and detect circles based on contour properties
#         detected_circles = []
#         for contour in contours:
#             area = cv2.contourArea(contour)
#             perimeter = cv2.arcLength(contour, True)
#
#             # Skip if the perimeter is zero
#             if perimeter == 0:
#                 continue
#
#             circularity = 4 * np.pi * area / (perimeter ** 2)
#
#             # Adjust the circularity threshold as needed
#             circularity_threshold = 0.8
#
#             # Detect circles based on circularity
#             if circularity > circularity_threshold:
#                 # Get the minimum enclosing circle of the contour
#                 (x, y), radius = cv2.minEnclosingCircle(contour)
#                 center = (int(x), int(y))
#                 radius = int(radius)
#
#                 # Define the region of interest (ROI) around the detected circle
#                 roi_x = int(x - radius)
#                 roi_y = int(y - radius)
#                 roi_width = int(2 * radius)
#                 roi_height = int(2 * radius)
#
#                 # Check if there are non-zero pixel values within the ROI
#                 roi_gray = gray_image[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]
#                 if cv2.countNonZero(roi_gray) > 0:
#                     # The circle overlaps with a marked bubble
#                     cv2.rectangle(image, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 0, 255), 2)
#                 else:
#                     # The circle does not overlap with a marked bubble
#                     cv2.circle(image, center, radius, (0, 255, 0), 2)
#
#                 detected_circles.append((center, radius))
#
#         if max < len(detected_circles):
#             max = len(detected_circles)
#             mt1 = t1
#             mt2 = t2
#             mx = x
#             my = y
#             print("YEsss", len(detected_circles), "t1=", t1, " t2=", t2, "mx=", mx, " my=", my)
#
#     # for i in range(0, 255):
#     #     for j in range(0, 255):
#     #         detectcircle(t1=j, t2=i)
#
#
# for j in range(3, 32, 2):
#     blurred(j, j)
# print(max, "-", mt1, "-", mt2, "-", mx, "-", my)
#
# cv2.imshow("Detected Circles", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imshow("hell",img)

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# # Load the image
# image = cv2.imread('omr1.jpeg')
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Blur the grayscale image
# blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#
# # Detect circles using the Hough transform
# circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=30)
#
# # If no circles were detected, exit
# if circles is None:
#     print("No circles found")
#     exit()
#
# # Convert the (x, y) coordinates and radius of the circles to integers
# circles = np.round(circles[0, :]).astype("int")
#
# # Define the colors for marking the circles
# green = (0, 255, 0)
# red = (0, 0, 255)
#
# # Loop over the detected circles
# for (x, y, r) in circles:
#     # Draw the circle in the original image
#     cv2.circle(image, (x, y), r, green, 2)
#
#     # Crop the circle from the grayscale and color images
#     circle_gray = gray_image[y - r:y + r, x - r:x + r]
#     circle_color = image[y - r:y + r, x - r:x + r]
#
#     # Compute the mean intensity of the circle in the grayscale image
#     mean_intensity = cv2.mean(circle_gray)[0]
#
#     # If the mean intensity is greater than 100, the bubble is marked
#     if mean_intensity > 100:
#         cv2.circle(image, (x, y), r, red, 2)
#
# # Display the image with the marked bubbles
# cv2.imshow("Marked Bubbles", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

image = cv2.imread('Latestcopy.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

max_count = 0
best_t1 = 0
best_t2 = 0
best_blur_x = 0
best_blur_y = 0

# Blurring and circle detection function
def detect_circles(blur_x, blur_y):
    global max_count, best_t1, best_t2, best_blur_x, best_blur_y

    # Apply Gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (blur_x, blur_y), 0)

    # Apply Otsu's thresholding to obtain a binary image
    _, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Perform edge detection using Canny on the binary image
    edges = cv2.Canny(binary_image, 30, 100)

    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate over the contours and detect circles based on contour properties
    detected_circles = []
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        # Skip if the perimeter is zero
        if perimeter == 0:
            continue

        circularity = 4 * np.pi * area / (perimeter ** 2)

        # Adjust the circularity threshold as needed
        circularity_threshold = 0.8

        # Detect circles based on circularity
        if circularity > circularity_threshold:
            # Get the minimum enclosing circle of the contour
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Filter circles based on radius, area, or aspect ratio
            min_radius = 5
            max_radius = 100
            if min_radius <= radius <= max_radius:
                detected_circles.append((center, radius))

    count = len(detected_circles)
    if count > max_count:
        max_count = count
        best_t1, best_t2 = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        best_blur_x = blur_x
        best_blur_y = blur_y
        print("Detected Circles:", count, "Blur X:", blur_x, "Blur Y:", blur_y)

    # Draw the detected circles on the image
    for (center, radius) in detected_circles:
        cv2.circle(image, center, radius, (0, 255, 0), 2)

# Iterate over different blur parameters
for blur_x in range(3, 32, 2):
    for blur_y in range(3, 32, 2):
        detect_circles(blur_x, blur_y)

print("Best Result: Detected Circles:", max_count, "Blur X:", best_blur_x, "Blur Y:", best_blur_y)

# Display the image with detected circles
cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()