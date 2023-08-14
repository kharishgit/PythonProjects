import cv2
import numpy as np

# Load the image
image = cv2.imread('marked.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blurring and circle detection function
def detect_circles(blur_x, blur_y):
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
    marked_bubbles = []
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

            # Filter marked bubbles based on additional conditions (if needed)
            # For example, you can use a separate condition to identify marked bubbles
            if area > threshold_area:
                marked_bubbles.append((center, radius))

    # Draw the detected circles on the image (in one color)
    for (center, radius) in detected_circles:
        cv2.circle(image, center, radius, (0, 255, 0), 2)

    # Draw the marked bubbles on the image (in another color)
    for (center, radius) in marked_bubbles:
        cv2.circle(image, center, radius, (0, 0, 255), 2)

    # Return the count of detected circles and marked bubbles
    return len(detected_circles), len(marked_bubbles)

# Specify the threshold area for identifying marked bubbles
threshold_area = 100

# Iterate over different blur parameters
detected_circles_count, marked_bubbles_count = detect_circles(5, 5)  # Specify the blur parameters you want to use
print("Detected Circles Count:", detected_circles_count)
print("Marked Bubbles Count:", marked_bubbles_count)

# Display the image with detected circles and marked bubbles
cv2.imshow("Detected Circles and Marked Bubbles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
