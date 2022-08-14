import pygame, sys
from settings import *

class Menu:
    def __init__(self, level):
        # general setup
        
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        # self.button_names = ['New game', 'Continue', 'option', 'Exit', 'save', 'load']
        # self.button_names = ['Continue','Exit']
        self.button_names = ['New game', 'Continue','Exit']
        self.button_nums = len(self.button_names)
        self.level = level
        self.bg = level.bg_img[config['title_cover_img']]
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))
        
        # menu title names setup
        self.menu_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE * 3)
        # self.menu_font = pygame.font.Font(dialogue_font, UI_FONT_SIZE * 3)
        self.menu_state = ['title', 'menu']
        self.title_names = [config['title_screen_text'], 'Menu']
        self.menu_index = 0
        self.menu_color = TEXT_COLOR_SELECTED
        self.full_width = screen.get_size()[0]
        self.full_height = screen.get_size()[1]

        # button dimensions and creation
            # button width and button height
        self.width = self.full_width // ((self.button_nums + 1))
        self.height = self.full_height * 0.08
        self.create_button()

        # selection system
        self.selection_index = 0
        if self.level.menu_state == 'dead_screen' or self.level.has_save:
            self.selection_index = 1
        self.selection_time = None
        self.can_move = True
        self.alpha = 128
        self.bg_color = (255, 255, 255)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT]:
                self.selection_index = (self.selection_index + 1) % self.button_nums
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT]:
                self.selection_index = (self.selection_index + self.button_nums - 1) % self.button_nums
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                self.button_list[self.selection_index].trigger(self.level)
                # to keep not over press
                self.level.can_press_key=False
                self.level.press_key_time=pygame.time.get_ticks()
                if self.level.dialog.option_menu:
                    self.level.dialog.option_menu.can_move = False
                    self.level.dialog.option_menu.selection_time = pygame.time.get_ticks()
            
    def selection_cooldown(self):
        if not(self.can_move):
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def create_button(self):
        self.button_list = []

        for button, index in enumerate(range(self.button_nums)):
            if index < 4: # for upper button
                # horizontal position
                increment = self.full_width // self.button_nums
                left = (button * increment) + (increment - self.width) // 2

                # vertical position
                top = self.full_height * 0.1

                # create the object
                button = Button(left, top, self.width, self.height, index, self.font)
                self.button_list.append(button)
            else:
                increment = self.full_width // self.button_nums
                left = (button * increment) + (increment - self.width) // 2

                # vertical position
                top = self.full_height * 0.2

                # create the object
                button = Button(left, top, self.width, self.height, index, self.font)
                self.button_list.append(button)

    def display(self):
        self.input()
        self.selection_cooldown()
        if self.level.menu_state == 'title':
            self.alpha = 128
            self.bg_color = (255, 255, 255)
            self.menu_index = 0
        elif self.level.menu_state == 'menu':
            self.bg_color = (255, 255, 255)
            self.alpha = 128
            self.menu_index = 1

        # blit bg
        screen.blit(self.bg, self.bg_rect)
        # tranparent white bg
        bg_surface = pygame.Surface((self.full_width, self.full_height))
        bg_surface.set_alpha(self.alpha)
        bg_surface.fill(self.bg_color)
        screen.blit(bg_surface, (0, 0))

        # title name
        title_surf = self.menu_font.render(self.title_names[self.menu_index], False, self.menu_color)
        title_rect = title_surf.get_rect(midtop = (self.full_width/2, self.full_height/2) + pygame.math.Vector2(0, 20))
        screen.blit(title_surf, title_rect)

        # buttons
        for index, button in enumerate(self.button_list):
            # get attributes
            name = self.button_names[index]
            button.display(screen, self.selection_index, name)

class Button:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font  = font

    def display_names(self, surface, name, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # button name
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 20))

        # draw
        surface.blit(title_surf, title_rect)

    def trigger(self, level):
        menu = level.menu_list[self.index]
        if level.menu_state == 'title':
            if menu == 'New game':
                # level.__init__()
                level.toggle_menu()
            elif menu == 'Continue':
                if level.has_save:
                    pass
                else:
                    level.toggle_menu()
            elif menu == 'Exit':
                # save_file(level)
                pygame.quit()
                sys.exit()
        elif level.menu_state == 'menu':
            if menu == 'New game':
                level.__init__()
                level.dialogue_init()
                # level.dialogue_done_times=0
                # level.dialog.first_talk=True
                # self.dialog.ending = False
            elif menu == 'Continue':
                level.title_screen()
            elif menu == 'Exit':
                pygame.quit()
                sys.exit()

        # save button
        if menu == 'save':
            # save_file(level)
            pass
        elif menu == 'load' and level.has_save:
            level.__init__()
            # load_file(level)
        
    def display(self, surface, selection_num, name):
        if self.index == selection_num:
            pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_names(surface, name, self.index == selection_num)

