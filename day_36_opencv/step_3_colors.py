import cv2

f_name = "data/image-sm.jpeg"
image = cv2.imread(f_name)

print("cv2.COLOR_BGR2RGB", cv2.COLOR_BGR2RGB)
print("cv2.COLOR_BGR2GRAY", cv2.COLOR_BGR2GRAY)
# image_new = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_new = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# print(image)
print(image[0])
print(image.shape)
# print(image_new)
print(image_new[0])
print(image_new.shape)
# print(image - image_new)
# cv2.imshow("new image", image_new)
# cv2.waitKey(0)

cv2.imwrite("data/image-sm-gray.jpeg", image_new)
