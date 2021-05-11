import easyocr

from ocr_util import show_image_ocr

DIRECTORY = 'case1/images'
LANGUAGES = ['en']

FILE_1 = 'surf.jpeg'
FILE_2 = 'quote.png'
FILE_3 = 'sign.png'

reader = easyocr.Reader(LANGUAGES)


def read_ocr_file(file_name, is_multiline=False):
    image_path = "{directory}/{file_name}".format(directory=DIRECTORY, file_name=file_name)
    show_image_ocr(reader=reader, path=image_path, is_multiline=is_multiline)


read_ocr_file(FILE_1)
read_ocr_file(FILE_2, is_multiline=True)
read_ocr_file(FILE_3, is_multiline=True)
