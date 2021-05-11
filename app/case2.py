import easyocr
import json
import uuid
import re
import os

from ocr_util import read_ocr

LANGUAGES = ['en']

IMAGE_DIRECTORY = 'case2/images'
DATA_DIRECTORY = 'case2/data'

reader = easyocr.Reader(LANGUAGES)

if not os.path.exists(DATA_DIRECTORY):
    os.makedirs(DATA_DIRECTORY)


def write_data(file_name):
    image_path = "{directory}/{file_name}".format(directory=IMAGE_DIRECTORY, file_name=file_name)
    file_id = uuid.uuid4()
    data_file = '{0}.json'.format(file_name)
    completed_file_name = "{file_id}_{file_name}".format(file_id=file_id, file_name=data_file)
    data_path = "{directory}/{file_name}".format(directory=DATA_DIRECTORY, file_name=completed_file_name)

    # Declare base data
    data = {}

    # Read ocr result for prepare to write to json file
    ocr_result = read_ocr(reader, image_path)
    previous_text = ''

    for detection in ocr_result:
        text = detection[1]
        is_number = False
        number = 0
        # If text is empty
        if not text:
            continue

        used_text = text

        # If text contain any number
        if re.search(r'\d', used_text):
            # If prefix of number start with S or $
            if used_text.startswith("S") or used_text.startswith("$"):
                used_text = used_text[1:]
            # Clean data
            used_text = re.sub('[^A-Za-z0-9_-]', '', used_text)

            try:
                number = float(used_text)
                is_number = True
            except ValueError:
                if len(text) == 1 and (not text.startswith("S") or not text.startswith("$")):
                    previous_text = text
                continue

        if is_number:
            data[previous_text] = number
        else:
            previous_text = text

    # After prepare json file
    # Then write json file to data path
    with open(data_path, 'w') as outfile:
        json.dump(data, outfile)

    print("Completed save json file with with file_id: {0}".format(completed_file_name))


file_list = [f for f in os.listdir(IMAGE_DIRECTORY) if os.path.isfile(os.path.join(IMAGE_DIRECTORY, f))]
for file in file_list:
    write_data(file_name=file)
