
import cv2 as cv
import numpy as np

sample_img = ['Sample.png','cityB.jpg','cityD.webp','cloud.jpg','refl.jpg','sea.jpg','winter.png','yellow.jpg','aladdin.jpg','hitman.jpg']

#이미지 선택
img_select = 0

img = cv.imread(sample_img[img_select])
assert img is not None, 'Cannot read the given image, ' + sample_img[img_select]

# 가로를 600px로 고정하고 세로 비율 유지
target_width = 600
aspect_ratio = img.shape[0] / img.shape[1] # 세로/가로 비율
target_height = int(target_width * aspect_ratio)

dim = (target_width, target_height)
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)


    #이미지 전처리
# Convert the image to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Apply histogram equalization
img_tran = cv.equalizeHist(img_gray)

# Initialize control parameters
#히스토그램 평활화된 이미지의 스레드
threshold11 = 800
threshold12 = 1700
#원본의 스레드
threshold21 = 600
threshold22 = 1000

aperture_size = 5

# Read the given image
img1 = img_tran
img2 = img_gray


#엣지 검출
# Get the Canny edge image
edge1 = cv.Canny(img1, threshold11, threshold12, apertureSize=aperture_size)
edge2 = cv.Canny(img2, threshold21, threshold22, apertureSize=aperture_size)
edge = cv.bitwise_or(edge1, edge2)

# Show all images
info = f'Thresh1: {threshold11}, Thresh2: {threshold12}, KernelSize: {aperture_size}'
merge1 = np.hstack((img1, edge1, edge))
merge2 = np.hstack((img2, edge2, edge))
cv.imshow('Canny Edge1: hist', merge1)
cv.imshow('Canny Edge2: origin', merge2)


#이미지 합성
# 색상 반전 (Bitwise NOT 연산)
edges = cv.bitwise_not(edge)
# 이미지 색감 뭉개지게 하기 (Bilateral Filter)
color = cv.bilateralFilter(img, 9, 10, 10)
# Combine the color image with the edges mask
cartoon = cv.bitwise_and(color, color, mask=edges)


# Display the cartoon image
result = np.hstack((img, cartoon))

cv.imshow('Cartoon Rendering: Original | Result', result)

# 파일 결과 저장
save_name = sample_img[img_select].split('.')[0] + '_result.jpg'
cv.imwrite(save_name, result)

cv.waitKey(0)
cv.destroyAllWindows()