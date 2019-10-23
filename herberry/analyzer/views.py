import os
from pathlib import Path
from flask import request
import pytesseract
from PIL import Image
import cv2


def extract_text(file_name):
    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 1)

    file_name = '{}.png'.format(os.getpid())
    cv2.imwrite(file_name, gray)

    result = pytesseract.image_to_string(Image.open(file_name), lang='eng')
    os.remove(file_name)
    return result


def analyze():
    #  just a stub for checking an image
    img = request.args.get('img')
    if img:
        img_path = Path(os.path.dirname(__file__)) / 'fixtures' / request.args.get('img')
        return extract_text(str(img_path))
