import cv2
import os

FRONTAL_FACE_CASCADE = "haarcascade_frontalface_default.xml"
# FRONTAL_FACE_CASCADE = "haarcascade_frontalface_alt_tree.xml"

print("cv2.data.haarcascades", cv2.data.haarcascades)
detector = cv2.CascadeClassifier(
    os.path.join(cv2.data.haarcascades, FRONTAL_FACE_CASCADE)
)
f_name = "data/image-sm.jpeg"
image = cv2.imread(f_name)

faces: cv2.Mat = detector.detectMultiScale(image)
print(faces)
print(faces.shape)
print(faces.size)

print("found", len(faces), "faces")
for x, y, w, h in faces:
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    color = (102, 188, 196)
    thickness = 2
    cv2.rectangle(image, pt1, pt2, color, thickness)

# cv2.imshow("faces", image)
# cv2.waitKey()

cv2.imwrite("data/image-sm-faces.jpeg", image)
