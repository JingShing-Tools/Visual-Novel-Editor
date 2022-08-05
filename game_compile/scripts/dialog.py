import pygame
from settings import *

class Dialog_box:
    def __init__(self):
        
        self.screen_width = screen.get_size()[0]
        self.screen_height = screen.get_size()[1]

        # self.font = pygame.font.SysFont('youyuan', 25)
        self.font = pygame.font.Font(dialogue_font, 25)
        self.textbox_surf = pygame.Surface((700,200), pygame.SRCALPHA)
        # self.textbox_rect = self.textbox_surf.get_rect(topleft=(150,200))
        self.textbox_rect = self.textbox_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 + 30))
        self.border_rect = self.textbox_surf.get_rect(topleft=(0, 0))

        # talker icon
        self.talker_image = pygame.transform.scale(pygame.image.load(resource_path('assets/graphics/characters/talker_1_face.png')), (152, 152))
        # self.talker_image_rect = self.talker_image.get_rect(bottomright = self.textbox_rect.topright)
        self.talker_image_rect = self.talker_image.get_rect(bottomleft = self.textbox_rect.topleft)

        # line progress
        self.text = 'Hello world!'
        self.multiline = []
        self.multi_label = []
        self.multiline_max_line = 4
        self.line_internal = 35

        self.show_textbox = False
        self.typing = False
        self.scrolling_text_time = 35
        self.bg_color = 'white'
        self.bg_alpha = 0

    def gradual_typing(self):
        # dialog box bg
        # screen.blit(self.textbox_surf, self.textbox_rect)
        if self.typing:
            line_num = len(self.multiline)
            self.multi_label.clear()

            rendering = ''
            # self.multi_label.clear()
            for rows, lines in enumerate(self.multiline):
                # print(str(rows) + ' ' + str(line_num) + ' ' + lines)
                self.textbox_surf.fill((255, 255, 255, 200))
                pygame.draw.rect(self.textbox_surf, "black", self.border_rect, 6)
                if line_num > 1 and rows < line_num - 1:
                # if line_num > 1 and rows == line_num - 2:
                    # full line part
                    row_text = self.font.render(lines, 1, 'black')
                    # row_text_rect = row_text.get_rect(topleft=(20, 30 + rows * 20))
                    # self.textbox_surf.blit(row_text, row_text_rect)
                    # screen.blit(self.textbox_surf, self.textbox_rect)
                    self.multi_label.append(row_text)
                    # self.multi_label[rows] = row_text
                    # print(lines)

                elif rows == line_num - 1:
                    # gradual type part
                    self.multi_label.append(self.text)
                    for char in lines:
                        pygame.time.delay(self.scrolling_text_time)
                        pygame.event.clear()

                        rendering = rendering + char
                        rendered_text = self.font.render(rendering, 1, 'black')
                        # text_rect = rendered_text.get_rect(topleft=(20, 30))

                        self.multi_label[-1] = rendered_text
                        # screen.fill(self.bg_color)
                        # screen.set_alpha(self.bg_alpha)
                        # self.textbox_surf.blit(rendered_text, text_rect)

                        for line in range(len(self.multi_label)):
                            self.textbox_surf.blit(self.multi_label[line], (20, 30 + line * self.line_internal))
                            crt_shader()
                        self.result_print()

        self.typing = False
    
    def add_line(self, text):
        self.text = text
        if len(self.multiline) <= self.multiline_max_line - 1:
            self.multiline.append(self.text)
        else:
            self.refresh_lines()
            self.multiline.append(self.text)

    def refresh_lines(self):
        self.multiline.clear()
        self.multi_label.clear()

    def result_print(self):
        pygame.draw.rect(self.textbox_surf, "black", self.border_rect, 6)
        screen.blit(self.textbox_surf, self.textbox_rect)
        screen.blit(self.talker_image, self.talker_image_rect)
        crt_shader()

    def blit_test(self):
        textbox_surf = pygame.Surface((700,200), pygame.SRCALPHA)
        textbox_surf.fill('black')
        textbox_rect = textbox_surf.get_rect(topleft=(150,200))
        screen.blit(textbox_surf, textbox_rect)

    def blit_press_hint(self):
        x = self.screen_width / 2
        y = self.screen_height - 100
        thickness = 2
        text = "press 'T' to talk" if (len(self.multiline) == 0 or not(self.show_textbox)) else "press 'enter' to continue"
        outline_color = 'black'
        fill_color = 'white'
        self.blit_text_with_outline(x, y, text, thickness, outline_color, fill_color)
    
    def blit_text_with_outline(self, x, y, text, thickness, outline_color, fill_color):
        # TEXT OUTLINE
        # top left
        self.draw_text(x + thickness, y- thickness , text, outline_color)
        # top right
        self.draw_text(x + thickness, y- thickness , text, outline_color)
        # btm left
        self.draw_text(x - thickness, y + thickness , text, outline_color)
        # btm right
        self.draw_text(x- thickness, y + thickness , text, outline_color) 

        # TEXT FILL
        self.draw_text(x, y, text, fill_color)

    def draw_text(self, x, y, text, color):
        text = self.font.render(text, True, color)
        text_rect = text.get_rect(center = (x, y))
        screen.blit(text, text_rect)

    def display(self):
        if self.show_textbox:
            if self.typing:
                self.gradual_typing()
            self.result_print()