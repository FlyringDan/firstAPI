import pytesseract
from PIL import Image
import re
from ToJSON import convert_to_json
from FindSignature import find_signature

nameRegEx = r"[Оо]т\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+"
seriesRegEx = r"\d{4}"
numberRegEx = r"\d{6}"
codeRegEx = r"\d{3}-\d{3}"
path_to_image = ""


def recognize_the_text(path_to_dec_img):
    pytesseract.pytesseract.tesseract_cmd = "C:/MYPROGRAMS/Tesseract/tesseract"
    image = Image.open(path_to_dec_img)

    text = pytesseract.image_to_string(image, lang='rus')
    text = re.sub(r"\s+", " ", text)
    # print(text)
    try:
        name = re.sub(r"[Оо]т\s+", "", re.search(nameRegEx, text).group(0))
    except Exception:
        name = None
        print("Отсутствует ФИО или оно введено неккоректно")
    try:
        series = re.search(seriesRegEx, text).group(0)
    except Exception:
        series = None
        print("Отсутствует серия поспорта или она введена неккоректно")
    try:
        number = re.search(numberRegEx, text).group(0)
    except Exception:
        number = None
        print("Отсутствует номер паспорта или он введён неккоректно")
    try:
        code = re.sub(r"[\s+]", "", re.search(codeRegEx, text).group(0))
    except Exception:
        code = None
        print("Отсутствует код подразделения или он введён неккоректно")
    # print(name, series, number, code)
    convert_to_json(name, series, number, code, find_signature(path_to_dec_img))


#recognize_the_text("Files/png_folder/decoded_image.png")
#recognize_the_text('test1.jpg')
