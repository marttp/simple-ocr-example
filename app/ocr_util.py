import cv2
from matplotlib import pyplot as plt


def read_ocr(reader, path):
    return reader.readtext(path)


def show_image_ocr(reader, path, is_multiline=False):
    result = read_ocr(reader, path)
    if is_multiline:
        multi_line_util(ocr_result=result, path=path)
    else:
        single_line_util(ocr_result=result, path=path)


def single_line_util(ocr_result, path):
    top_left = tuple(ocr_result[0][0][0])
    bottom_right = tuple(ocr_result[0][0][2])
    text = ocr_result[0][1]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imread(path)
    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
    img = cv2.putText(img, text, top_left, font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    plt.imshow(img)
    plt.show()


def multi_line_util(ocr_result, path):
    img = cv2.imread(path)
    font = cv2.FONT_HERSHEY_SIMPLEX
    spacer = 100
    for detection in ocr_result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        spacer += 15
    plt.imshow(img)
    plt.show()
