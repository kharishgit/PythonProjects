import cv2 as cv
imgread = cv.imread('candid.jpeg')
cv.imshow("Image",imgread)
cv.waitKey(0)
cv.destroyAllWindows()