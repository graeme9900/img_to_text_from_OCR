import pygame
import sys
import python_data
from PIL import Image

OCR_LANG_LIST = python_data.OCR_LANG_LIST
FONTS = python_data.FONTS


class MultiOption:
    def __init__(self):
        pygame.init()
        # 创建一个空白图像
        self.img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))

        # 将图像转换为Pygame图像
        self.pygame_img = pygame.image.fromstring(
            self.img.tobytes(), self.img.size, self.img.mode)

        self.WINDOW_SIZE = (400, 400)
        self.WINDOW_TITLE = '選擇語言'
        self.USE_LANG = FONTS
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(self.WINDOW_TITLE)
        pygame.display.set_icon(self.pygame_img)

        # 定义选项的大小、位置和颜色
        self.option_width = 100
        self.option_height = 50
        self.option_spacing = 10
        self.option_x = (
            self.WINDOW_SIZE[0] - self.option_width * 2 - self.option_spacing) / 2
        self.option_y = (
            self.WINDOW_SIZE[1] - self.option_height * 4 - self.option_spacing * 3) / 2
        self.options = []
        self.option_selected = []
        for i in range(10):
            x = self.option_x + (self.option_width +
                                 self.option_spacing) * (i % 2)
            y = self.option_y + (self.option_height +
                                 self.option_spacing) * (i // 2)
            self.options.append(pygame.Rect(
                x, y, self.option_width, self.option_height))
            self.option_selected.append(False)

        self.option_color = (200, 200, 200)
        self.option_hover_color = (255, 255, 255)
        self.option_selected_color = (63, 63, 63)

        self.screen_state = 0

    def draw_options(self):
        for i, option in enumerate(self.options):
            color = self.option_color
            if option.collidepoint(pygame.mouse.get_pos()):
                color = self.option_hover_color
            if self.option_selected[i]:
                color = self.option_selected_color
            pygame.draw.rect(self.screen, color, option)
            font = pygame.font.Font(self.USE_LANG, 24)
            option_text = font.render(OCR_LANG_LIST[i], True, (0, 0, 0))
            option_text_rect = option_text.get_rect(center=option.center)
            self.screen.blit(option_text, option_text_rect)

    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, option in enumerate(self.options):
                if option.collidepoint(event.pos):
                    if self.option_selected[i]:
                        self.option_selected[i] = False
                    else:
                        self.option_selected[i] = True
                    if self.option_selected[i] == True:
                        print(f'{OCR_LANG_LIST[i]} 被選擇了')
                    else:
                        print(f'{OCR_LANG_LIST[i]} 被取消了')
                    if OCR_LANG_LIST[i] == '確認':
                        self.screen_state = 1
                    elif OCR_LANG_LIST[i] == '退出':
                        self.screen_state = 2

    def hint_object(self):
        font = pygame.font.Font(self.USE_LANG, 24)
        text = font.render(
            '請選擇你圖中的語言(預設英文)', True, (0, 0, 0))
        text_rect = text.get_rect(
            center=(self.WINDOW_SIZE[0]/2, 40))
        return text, text_rect

    def run(self):
        running = True
        # 主循环
        while running:
            # 处理事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN]:
                    self.handle_mouse_event(event)
                elif self.screen_state != 0:
                    running = False

            # 绘制选项
            self.screen.fill((255, 255, 255))
            self.draw_options()

            # 說明
            text, text_rect = self.hint_object()
            self.screen.blit(text, text_rect)

            # 更新屏幕
            pygame.display.update()

    def output_lang_list(self):
        if self.screen_state == 1:
            lang_list = []
            for i in range(len(self.option_selected)-2):
                if self.option_selected[i] == True:
                    lang_list.append(OCR_LANG_LIST[i])
            return lang_list
        elif self.screen_state == 2:
            print('退出')
            sys.exit()
