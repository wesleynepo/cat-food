import numpy as np
import cv2 as cv


def openFile(image_filename):
    frame = cv.imread(image_filename)

    return cv.resize(frame, (1280, 720))


def save_image(image, file):
    cv.imwrite(file + '.jpg', image)


def draw_indicator(image, circle_origin, radius, percentage):
    left_corner = (circle_origin[0] - radius, circle_origin[1] - radius)
    right_corner = (circle_origin[0] + radius, circle_origin[1] + radius)
    green = (0, 255, 0)
    white = (255, 255, 255)

    cv.rectangle(image, left_corner, right_corner, green, 2)
    cv.putText(image, percentage, circle_origin, cv.FONT_HERSHEY_SIMPLEX, 1,
               white, 2)


def show(image):
    cv.imshow('RealTime', image)
    cv.waitKey(0)


def main():
    loaded_image = openFile('100.jpg')

    blured_image = cv.medianBlur(loaded_image, 5)

    bg_blured_image = cv.cvtColor(blured_image, cv.COLOR_BGR2GRAY)

    circles = cv.HoughCircles(bg_blured_image, cv.HOUGH_GRADIENT, 1, bg_blured_image.shape[0] / 64, param1=100, param2=100, minRadius=0,
                              maxRadius=0)
    circles = np.uint16(np.around(circles))

    circle_mask = np.zeros(bg_blured_image.shape[:2], dtype="uint8")

    for i in circles[0, :]:
        org = (i[0], i[1])
        radius = i[2]
        cv.circle(circle_mask, (i[0], i[1]), i[2], 255, -1)
        total_area = i[2] ** 2 * np.pi

    masked_image = cv.bitwise_and(loaded_image, loaded_image, mask=circle_mask)

    masked_image_hsv = cv.cvtColor(masked_image, cv.COLOR_RGB2HSV)

    masked_image_hsv_gray = cv.cvtColor(masked_image_hsv, cv.COLOR_RGB2GRAY)

    _, threshold_image = cv.threshold(masked_image_hsv_gray, 100, 255, cv.THRESH_BINARY)

    total_food = cv.countNonZero(threshold_image)

    draw_indicator(loaded_image, org, radius, "{0:.0f}%".format(total_food / total_area * 100))

    save_image(loaded_image, 'final')

if __name__ == "__main__":
    main()
