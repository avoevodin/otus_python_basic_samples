import random
import sys

import cv2
import os

DATAROOT = "data"
# FRONTAL_FACE_CASCADE = "haarcascade_frontalface_default.xml"
# FRONTAL_FACE_CASCADE = "haarcascade_frontalface_alt_tree.xml"
FRONTAL_FACE_CASCADE = "haarcascade_frontalface_alt.xml"

print("cv2.data.haarcascades", cv2.data.haarcascades)
detector = cv2.CascadeClassifier(
    os.path.join(cv2.data.haarcascades, FRONTAL_FACE_CASCADE)
)


def detect_faces(image: cv2.Mat):
    faces: cv2.Mat = detector.detectMultiScale(image)
    print("found", len(faces), "faces")
    for x, y, w, h in faces:
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        thickness = 2
        cv2.rectangle(image, pt1, pt2, color, thickness)


def process_image(image: cv2.Mat):
    detect_faces(image)


def process_video(video_cap: cv2.VideoCapture) -> int:
    while True:
        success, frame = video_cap.read()
        if not success:
            print("capture error!")
            return 2

        process_image(frame)
        cv2.imshow("detected face!", frame)
        key = cv2.waitKey(0)

        if key == 27:
            break

    return 0


def show_frame(video_cap: cv2.VideoCapture):
    success, image = video_cap.read()
    if not success:
        print("capture error!")
        return

    cv2.imshow("frame", image)
    cv2.waitKey()


def main():
    f_name = "pexels-alina-kurson-9842190.mp4"
    f_path = os.path.join(DATAROOT, f_name)
    cap = cv2.VideoCapture(f_path)
    code = 1

    try:
        code = process_video(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
    sys.exit(code)


def web_cam():
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)

    while cap.isOpened():
        success, img = cap.read()
        if success:
            cv2.imshow("Result", img)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break


if __name__ == "__main__":
    main()
    # web_cam()
