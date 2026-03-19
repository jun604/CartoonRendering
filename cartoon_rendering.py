import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

sample_img = ('Sample.png')

# Read the given image as gray scale
img = cv.imread(sample_img, cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'

# Apply histogram equalization
img_tran = cv.equalizeHist(img)

# Initialize control parameters
threshold1 = 800
threshold2 = 2000
aperture_size = 5
img_select = -1


# Read the given image
img1 = img_tran
img2 = img
assert img1 is not None, 'Cannot read the given image, ' + img1[img_select]
assert img2 is not None, 'Cannot read the given image, ' + img2[img_select]

# Get the Canny edge image
edge1 = cv.Canny(img1, threshold1, threshold2, apertureSize=aperture_size)
edge2 = cv.Canny(img2, threshold1, threshold2, apertureSize=aperture_size)
edge = cv.bitwise_or(edge1, edge2)

# Show all images
info = f'Thresh1: {threshold1}, Thresh2: {threshold2}, KernelSize: {aperture_size}'
#cv.putText(edge1, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
#cv.putText(edge1, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
merge1 = np.hstack((img1, edge1, edge))
merge2 = np.hstack((img2, edge2, edge))
cv.imshow('Canny Edge1: Original | Result', merge1)
cv.imshow('Canny Edge2: Original | Result', merge2)


# Load the image
img = cv.imread(sample_img)
# Convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Apply median blur to reduce noise
#gray = cv.medianBlur(gray, 5)
# Detect edges using adaptive thresholding
#edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
# 색상 반전 (Bitwise NOT 연산)
edges = cv.bitwise_not(edge)
# Convert the image to color
color = cv.bilateralFilter(img, 9, 300, 300)
# Combine the color image with the edges mask
cartoon = cv.bitwise_and(color, color, mask=edges)
# Display the cartoon image
result = np.hstack((cv.imread(sample_img), cartoon))
cv.imshow('Cartoon Rendering: Original | Result', result)

cv.waitKey(0)
cv.destroyAllWindows()