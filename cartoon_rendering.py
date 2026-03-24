import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

sample_img = ('Sample.png')

# Read the given image as gray scale
img_gray = cv.imread(sample_img, cv.IMREAD_GRAYSCALE)
assert img_gray is not None, 'Cannot read the given image'

# Apply histogram equalization
img_tran = cv.equalizeHist(img_gray)

# Initialize control parameters
threshold1 = 800
threshold2 = 1500
aperture_size = 5
img_select = -1


# Read the given image
img1 = img_tran
img2 = img_gray
assert img1 is not None, 'Cannot read the given image, ' + img1[img_select]
assert img2 is not None, 'Cannot read the given image, ' + img2[img_select]

# Get the Canny edge image
edge1 = cv.Canny(img1, threshold1, threshold2, apertureSize=aperture_size)
edge2 = cv.Canny(img2, threshold1, threshold2, apertureSize=aperture_size)
edge = cv.bitwise_or(edge1, edge2)

# Show all images
info = f'Thresh1: {threshold1}, Thresh2: {threshold2}, KernelSize: {aperture_size}'
cv.putText(edge1, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
cv.putText(edge1, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
merge1 = np.hstack((img1, edge1, edge))
merge2 = np.hstack((img2, edge2, edge))
cv.imshow('Canny Edge1: Original | Result', merge1)
cv.imshow('Canny Edge2: Original | Result', merge2)


# Load the image
img = cv.imread(sample_img)
# 색상 반전 (Bitwise NOT 연산)
edges = cv.bitwise_not(edge)
# Convert the image to color
color = cv.bilateralFilter(img, 9, 300, 300)
# Combine the color image with the edges mask
cartoon = cv.bitwise_and(color, color, mask=edges)

# 가로를 800px로 고정하고 세로 비율 유지
target_width = 800
aspect_ratio = cartoon.shape[0] / cartoon.shape[1] # 세로/가로 비율
target_height = int(target_width * aspect_ratio)

dim = (target_width, target_height)
cartoon = cv.resize(cartoon, dim, interpolation=cv.INTER_AREA)
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

# Display the cartoon image
result = np.hstack((img, cartoon))

cv.imshow('Cartoon Rendering: Original | Result', result)

cv.waitKey(0)
cv.destroyAllWindows()