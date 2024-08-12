import cv2
import numpy as np
# widthImg = 700
# heightImg = 700
image = cv2.imread('Latestcopy.png')
# image =cv2.resize(image,500,500)
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
    # a, binary_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # print(a)

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