import os
import time
from PIL import Image
import python_data

OCR_USE_FOLDER = python_data.OCR_USE_FOLDER


def create_object_folder():
    # 獲取當前時間
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S")  # 格林威治標準時間 time.gmtime()

    # 用時間創建目錄
    directory_name = "time_directory_" + current_time
    os.makedirs(OCR_USE_FOLDER+directory_name)
    return directory_name


def img_save(full_img, frist_coordinate, last_coordinate, directory_name):
    img = full_img.crop(
        (frist_coordinate[0], frist_coordinate[1], last_coordinate[0], last_coordinate[1]))
    img_file_path = OCR_USE_FOLDER+directory_name+'\\'+directory_name+'.png'
    img.save(img_file_path)
    return img, img_file_path


def text_save(text, directory_name):
    text_file_path = OCR_USE_FOLDER+directory_name+'\\'+directory_name+".txt"
    with open(text_file_path, "w", encoding='utf-8') as file:
        file.write(text)
    return text_file_path


def img_open(img_file_path):
    # 打開圖片文件
    img = Image.open(img_file_path)
    # 展示圖片
    img.show()


def text_open(text_file_path):
    filepath = os.path.dirname(os.path.abspath(__file__))

    # # 拼接文件的完整路径
    full_path = os.path.join(filepath, text_file_path)

    # 打开文件
    os.startfile(full_path)
