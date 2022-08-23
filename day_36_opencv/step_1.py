import cv2

f_name = "data/image-sm.jpeg"
image = cv2.imread(f_name)
print(type(image))
print(image)

print(image.shape, image.nbytes)

cv2.imshow("people", image)

key = cv2.waitKey()
print("exit by key", key)
