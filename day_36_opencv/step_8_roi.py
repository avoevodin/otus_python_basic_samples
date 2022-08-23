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


def add_selection(image: cv2.Mat, bbox):
    x, y, w, h = bbox
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    thickness = 2
    cv2.rectangle(image, pt1, pt2, color, thickness)


def process_image(image: cv2.Mat, bbox):
    add_selection(image, bbox)


def get_roi_frame(video_cap: cv2.VideoCapture):
    frame = None
    while True:
        success, frame = video_cap.read()
        if not success:
            print("capture error!")
            return frame

        cv2.imshow("image", frame)
        key = cv2.waitKey(100)

        if key == 27:
            break

    cv2.destroyAllWindows()
    return frame


def process_video(video_cap: cv2.VideoCapture) -> int:
    image = get_roi_frame(video_cap)
    if image is None:
        print("no image!")
        return 2

    target_selection_bbox = cv2.selectROI("Select object to follow", image)
    print(target_selection_bbox)

    # Kernelized Correlation filter
    tracker = cv2.TrackerKCF_create()
    tracker.init(image, target_selection_bbox)
    print(tracker)

    history = []
    cnt = 0
    rate = 1
    track_rate = 2
    track_cnt = 0
    while True:
        if track_cnt > 0:
            track_cnt -= 1
        cnt += 1
        success, frame = video_cap.read()
        if not success:
            print("capture error!")
            return 2
        track_status, bbox = tracker.update(frame)
        if not track_status and not track_cnt:
            print("tracking error!")
            track_cnt = track_rate
            continue

        process_image(frame, bbox)

        if cnt == rate:
            cnt = 0
            history.append(
                tuple(map(int, bbox)),
            )
        for x, y, w, h in history:
            x_center = x + w // 2
            y_center = y + h // 2
            # pt1 = (x_center, y_center)
            # pt2 = (x_center + 1, y_center + 1)
            process_image(frame, (x_center, y_center, 1, 1))

        cv2.imshow("image track", frame)
        key = cv2.waitKey(1)

        if key == 27:
            break

    return 0


def main():
    f_name = "pexels-alina-kurson-9842190.mp4"
    f_path = os.path.join(DATAROOT, f_name)
    # cap = cv2.VideoCapture(f_path)
    cap = cv2.VideoCapture(0)
    code = 1

    try:
        code = process_video(cap)
    finally:
        cap.release()

    cv2.destroyAllWindows()
    sys.exit(code)


if __name__ == "__main__":
    main()
