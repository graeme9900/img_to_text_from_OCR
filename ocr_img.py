import pytesseract
import python_data

LANGUAGE_CODE = python_data.LANGUAGE_CODE
DEFAULT_LANG_CODE = python_data.DEFAULT_LANG_CODE


def ocr_lang_code(ocr_lang):
    '''轉換成翻譯代碼'''
    ocr_plus_text = ''
    if ocr_lang == []:
        return DEFAULT_LANG_CODE
    for i in ocr_lang:
        ocr_plus_text = ocr_plus_text+'+'+LANGUAGE_CODE[i]
    return ocr_plus_text[1:]


def ocr_img_output(img, directory_name, ocr_plus_text):
    '''圖片文字辨識'''
    img = img.convert('L')
    text = pytesseract.image_to_string(img, lang=ocr_plus_text)
    return text
