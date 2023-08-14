import cv2
import pytesseract
# import os
# print(os.environ['PATH'])


# Load the image
img = cv2.imread('omr_sheet.jpg')

# Define the region of interest for questions 1 to 100
# x_start, y_start = 70, 880
# x_end, y_end = 2400, 2950
#
# Crop the image to the region of interest
# img = img[y_start:y_end, x_start:x_end]

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to binarize the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours of the bubbles
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort the contours from left to right
contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])

# Define the correct answers
correct_answers = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D',
                   'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D',
                   'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D',
                   'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D',
                   'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D',
                   ]

# Loop over the contours and extract the bubble regions
for i, c in enumerate(contours):
    # Extract the bubble region
    x, y, w, h = cv2.boundingRect(c)
    bubble = img[y:y+h, x:x+w]

    # Apply OCR to recognize the bubble mark
    bubble_gray = cv2.cvtColor(bubble, cv2.COLOR_BGR2GRAY)
    ret, bubble_thresh = cv2.threshold(bubble_gray, 127, 255, cv2.THRESH_BINARY_INV)
    text = pytesseract.image_to_string(bubble_thresh, config='--psm 10')

    # Match the bubble mark with the correct answer
    if text.upper() == correct_answers[i]:
        print(f"Question {i+1}: Correct answer is {text}")
    else:
        print(f"Question {i+1}: Incorrect answer, expected {correct_answers[i]}, but got {text}")
