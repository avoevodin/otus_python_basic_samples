import cv2

f_name = "data/image-sm.jpeg"
image = cv2.imread(f_name)
image_h, image_w, _ = image.shape
print([image_h, image_w])

scale = 0.5
target_d = (int(image_w * scale), int(image_h * scale))
image_small = cv2.resize(image, target_d)

print(image_small.shape)
cv2.imshow("people", image_small)
cv2.waitKey()

cv2.imwrite("data/image-sm2.jpeg", image_small)
