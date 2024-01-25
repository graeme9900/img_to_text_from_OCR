from PIL import ImageGrab
import pygame
import sys
import time
import os
import python_data

OCR_USE_FOLDER = python_data.OCR_USE_FOLDER


def full_screen_img():
    # 進行屏幕截圖
    screenshot = ImageGrab.grab()
    return screenshot


class Windows_pygame_img():
    '''顯示需要截圖與相應的動作'''

    def __init__(self, screenshot) -> None:
        # 設置圖片
        self.full_img = pygame.image.fromstring(
            screenshot.tobytes(), screenshot.size, screenshot.mode)

        # 設置窗口大小
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # 定義矩形
        self.rect = pygame.Rect(0, 0, 0, 0)

        # 矩形線框
        self.rectline = 2

        # 指定矩形顏色
        self.color = (255, 0, 0)

        # 指定矩形原點位置
        self.rectangle_origin = None, None

    def frist_windows(self):
        '''定義矩形初始位置'''
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.rect = pygame.Rect(
                        event.pos[0], event.pos[1], 0, 0)

                    pygame.draw.rect(self.screen, self.color,
                                     self.rect, self.rectline)
                    pygame.display.update()
                    running = False

            self.screen.blit(self.full_img, (0, 0))

            pygame.display.update()

    def check_moment_mouse(self):
        '''判斷滑鼠是鬆開的還是按下的'''
        running = True
        while running:
            for event in pygame.event.get():
                self.rectangle_origin = event.pos[0], event.pos[1]
                return [event.pos[0], event.pos[1]]

    def windows_pygame_main(self):
        '''確認'''
        # 運行游戲循環
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print('系統強制中斷')
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
                    event_pos_list = [event.pos[0], event.pos[1]]
                    pygame.quit()
                    return event_pos_list

                elif event.type == pygame.MOUSEMOTION:
                    # 获取当前鼠标位置
                    mouse_x, mouse_y = event.pos

                    # 根据鼠标位置和矩形原点位置的关系更新矩形的位置和大小
                    if mouse_x < self.rectangle_origin[0]:
                        self.rect.left = mouse_x
                        self.rect.width = self.rectangle_origin[0] - mouse_x
                    else:
                        self.rect.width = mouse_x - self.rectangle_origin[0]

                    if mouse_y < self.rectangle_origin[1]:
                        self.rect.top = mouse_y
                        self.rect.height = self.rectangle_origin[1] - mouse_y
                    else:
                        self.rect.height = mouse_y - self.rectangle_origin[1]

            self.screen.blit(self.full_img, (0, 0))

            # 繪製矩形
            pygame.draw.rect(self.screen, self.color, self.rect, self.rectline)

            # 更新窗口
            pygame.display.update()

    def organize_coordinates(self, frist_coordinate, last_coordinate):
        if frist_coordinate[0] > last_coordinate[0]:
            frist_coordinate[0], last_coordinate[0] = last_coordinate[0], frist_coordinate[0]
        if frist_coordinate[1] > last_coordinate[1]:
            frist_coordinate[1], last_coordinate[1] = last_coordinate[1], frist_coordinate[1]
        return frist_coordinate, last_coordinate
