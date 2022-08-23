import cv2
import os

RUSSIAN_PLATE_NUMBER = "haarcascade_russian_plate_number.xml"


def main():
    print("cv2.data.haarcascades", cv2.data.haarcascades)
    detector = cv2.CascadeClassifier(
        os.path.join(cv2.data.haarcascades, RUSSIAN_PLATE_NUMBER)
    )
    f_name = "data/cars-plates.jpeg"
    image = cv2.imread(f_name)

    plates: cv2.Mat = detector.detectMultiScale(image)
    if isinstance(plates, tuple):
        return

    print("plates", plates)
    print(plates.shape)
    print(plates.size)
    print("found", len(plates), "plates")

    for x, y, w, h in plates:
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        color = (102, 188, 196)
        # thickness = 2
        thickness = -1
        cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("plates", image)
    cv2.waitKey()


if __name__ == "__main__":
    main()
