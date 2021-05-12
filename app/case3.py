import os
import easyocr
from gtts import gTTS
from ocr_util import read_ocr

DIRECTORY = 'case3/images'
IMAGE_NAME = 'announcement-letter-40.png'
OUTPUT_DIRECTORY = 'case3/audios'
OUTPUT_FILE = "audio.mp3"
LANGUAGES = ['en']


def generate_full_text(result):
    if len(result) == 0:
        return ''
    return '{0} {1}'.format(result[0][1], generate_full_text(result[1:]))


if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

reader = easyocr.Reader(LANGUAGES)

ocr_result = read_ocr(reader=reader, path="{0}/{1}".format(DIRECTORY, IMAGE_NAME))

full_text = generate_full_text(ocr_result)
tts_object = gTTS(text=full_text, lang=LANGUAGES[0], slow=False)
tts_object.save('{0}/{1}'.format(OUTPUT_DIRECTORY, OUTPUT_FILE))

directory_path = os.path.abspath(os.getcwd()).replace(os.sep, '/')
path = '{0}/{1}/{2}'.format(directory_path, OUTPUT_DIRECTORY, OUTPUT_FILE)

os.system("start {0}".format(path))
