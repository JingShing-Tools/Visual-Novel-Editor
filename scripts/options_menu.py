import pygame
from settings import *

class Option_menu:
    def __init__(self, dialog):
        # general setup        
        self.font = pygame.font.Font(dialogue_font, 25)
        self.dialog = dialog
        
        self.full_width = screen.get_size()[0]
        self.full_height = screen.get_size()[1]

        # selection system
        self.selection_time = None
        self.can_move = True
        self.alpha = 128
        self.bg_color = (255, 255, 255)

        self.button_nums = len(self.dialog.options)
        self.line_id = 0
        self.selection_index = 0
        self.selection_list = []
    
    def show_options(self, line_id):
        self.selection_index = 0
        self.button_nums = len(self.dialog.options)
        self.dialog.get_option_names()
        self.create_selections()
        self.line_id = line_id
        self.selection_list.clear()
        self.create_selections()

    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT] or keys[pygame.K_UP]:
                self.selection_index = (self.selection_index + 1) % self.button_nums
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] or keys[pygame.K_DOWN]:
                self.selection_index = (self.selection_index + self.button_nums - 1) % self.button_nums
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.dialog.multiline.insert(self.line_id, self.dialog.options[self.dialog.option_names[self.selection_index]]['command'])
                # self.dialog.options.clear()
                # to keep not over press
                self.dialog.select = False
            
    def selection_cooldown(self):
        if not(self.can_move):
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def create_selections(self):
        self.selection_list.clear()
        option_num = len(self.dialog.options)
        width = self.full_width // ((option_num + 1))
        height = self.full_height * 0.08
        for selection, index in enumerate(range(option_num)):
            # horizontal position
            increment = self.full_width // option_num
            left = (selection * increment) + (increment - width) // 2

            # vertical position
            top = self.full_height * 0.1

            # create the object
            selection = Selections(left, top, width, height, index, self.font)
            self.selection_list.append(selection)

    def show_selections(self):
        if self.dialog.options:
            for index, select in enumerate(self.selection_list):
                # get attributes
                name = self.dialog.options[self.dialog.option_names[index]]['text']
                select.display(screen, self.selection_index, name)

    def display(self):
        self.input()
        self.selection_cooldown()
        # selections
        self.show_selections()
        crt_shader()

class Selections:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font  = font

    def display_names(self, surface, name, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # button name
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(center = self.rect.center)

        # draw
        surface.blit(title_surf, title_rect)
        
    def display(self, surface, selection_num, name):
        if self.index == selection_num:
            pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_names(surface, name, self.index == selection_num)