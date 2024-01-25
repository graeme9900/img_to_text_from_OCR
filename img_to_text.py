#!/usr/bin/env python
# 將圖片轉文本

import cat_screen
import ocr_img
import choice_lang
import file_control


def main():
    # 截下全螢幕
    full_img = cat_screen.full_screen_img()

    # 截下要辨識的部分
    wpi = cat_screen.Windows_pygame_img(full_img)
    wpi.frist_windows()
    frist_coordinate = wpi.check_moment_mouse()
    last_coordinate = wpi.windows_pygame_main()
    frist_coordinate, last_coordinate = wpi.organize_coordinates(
        frist_coordinate, last_coordinate)

    # 建立資料夾和儲存檔案
    directory_name = file_control.create_object_folder()
    img, img_file_path = file_control.img_save(full_img, frist_coordinate,
                                               last_coordinate, directory_name)

    # 選擇辨識的語言
    option = choice_lang.MultiOption()
    option.run()
    ocr_lang = option.output_lang_list()
    if ocr_lang != None:
        # 轉換成代碼
        ocr_plus_text = ocr_img.ocr_lang_code(ocr_lang)
        print(ocr_plus_text)

        print('-------------------------')
        # 轉換成文字和文本儲存
        text = ocr_img.ocr_img_output(
            img, directory_name, ocr_plus_text)
        text_file_path = file_control.text_save(text, directory_name)

        print(text)

        # 開啟文本
        file_control.text_open(text_file_path)
        file_control.img_open(img_file_path)


if __name__ == '__main__':
    main()
