import pygame, sys
from settings import *
from save_and_load import save_config
from music_player import sound_dict

class Menu:
    def __init__(self, level):
        # general setup
        
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        # self.button_names = ['New game', 'Continue', 'option', 'Exit', 'save', 'load']
        # self.button_names = ['Continue','Exit']
        self.button_names = ['New game','Continue','option','Exit']
        self.option_button_names = ['language','render','Back']
        self.language_names = ['english','schinese','tchinese','Back']
        self.render_names = ['gpu+cpu', 'cpu_only', 'Back']
        self.button_nums = len(self.button_names)
        self.level = level
        self.bg = level.bg_img[config['title_cover_img']]
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))
        
        # menu title names setup
        self.menu_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE * 3)
        # self.menu_font = pygame.font.Font(dialogue_font, UI_FONT_SIZE * 3)
        self.title_names = [config['title_screen_text'], 'Menu']
        self.menu_index = 0
        self.menu_state = self.level.menu_state
        self.menu_color = TEXT_COLOR_SELECTED
        self.full_width = screen.get_size()[0]
        self.full_height = screen.get_size()[1]

        # button dimensions and creation
            # button width and button height
        self.width = self.full_width // ((self.button_nums + 1))
        self.height = self.full_height * 0.08
        self.button_list = []
        self.create_button()

        # selection system
        self.selection_index = 0
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
                self.button_list[self.selection_index].trigger(self.level, self)
                # to keep not over press
                self.level.can_press_key=False
                self.level.press_key_time=pygame.time.get_ticks()
                if self.level.dialog.option_menu:
                    self.level.dialog.option_menu.can_move = False
                    self.level.dialog.option_menu.selection_time = pygame.time.get_ticks()

            if keys[pygame.K_ESCAPE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                if self.menu_state == 'option':
                    self.menu_state = self.level.menu_state
                    self.selection_index = 0
                    self.button_nums = len(self.button_names)
                    if len(self.button_list) != self.button_nums:
                        self.create_button()
                elif self.menu_state == 'language' or self.menu_state == 'render':
                    self.menu_state = 'option'
                    self.selection_index = 0
                    self.button_nums = len(self.option_button_names)
                    if len(self.button_list) != self.button_nums:
                        self.create_button()

    def selection_cooldown(self):
        if not(self.can_move):
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def create_button(self):
        self.button_list.clear()

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

        # maker info
        maker_name = self.font.render('Made by:JingShing', False, self.menu_color)
        maker_name_rect = title_surf.get_rect(center = (self.full_width/2, self.full_height/2) + pygame.math.Vector2(0, 20))
        screen.blit(maker_name, maker_name_rect)

        self.show_buttons()

    def show_buttons(self):
        if self.menu_state == 'option':
            for index, name in enumerate(self.option_button_names):
                self.button_list[index].display(screen, self.selection_index, name)
        elif self.menu_state == 'language':
            for index, name in enumerate(self.language_names):
                self.button_list[index].display(screen, self.selection_index, name, name==config['default_lang'])
        elif self.menu_state == 'render':
            for index, name in enumerate(self.render_names):
                if name == 'cpu_only' and config['cpu_only']:
                    self.button_list[index].display(screen, self.selection_index, name, True)
                elif name == 'gpu+cpu' and not config['cpu_only']:
                    self.button_list[index].display(screen, self.selection_index, name, True)
                else:
                    self.button_list[index].display(screen, self.selection_index, name)
        else:
            # buttons
            for index, name in enumerate(self.button_names):
                # get attributes
                self.button_list[index].display(screen, self.selection_index, name)

    def update(self):
        self.input()
        self.selection_cooldown()
        self.display()

class Button:
    def __init__(self, left, top, width, height, index, font):
        self.rect = pygame.Rect(left, top, width, height)
        self.index = index
        self.font  = font

    def display_names(self, surface, name, selected, config=False):
        if config:
            color = 'green'
        else:
            color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # button name
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 20))

        # draw
        surface.blit(title_surf, title_rect)

    def trigger(self, level, menu):
        sound_dict['talk'].play()
        option = menu.button_names[self.index]
        # for option menu
        if menu.menu_state == 'option':
            option = menu.option_button_names[self.index]
            if option == 'Back':
                menu.selection_index = 0
                menu.menu_state = level.menu_state
                menu.button_nums = len(menu.button_names)
            else:
                menu.menu_state = option
                if option == 'language':
                    menu.button_nums = len(menu.language_names)
                elif option == 'render':
                    menu.button_nums = len(menu.render_names)
        elif menu.menu_state == 'language':
            option = menu.language_names[self.index]
            if option == 'Back':
                menu.menu_state = 'option'
                menu.selection_index = 0
                menu.button_nums = len(menu.option_button_names)
            else:
                config['default_lang']=option
                level.language = config['default_lang']
                level.language_change()
        elif menu.menu_state == 'render':
            option = menu.render_names[self.index]
            if option == 'Back':
                menu.menu_state = 'option'
                menu.selection_index = 0
                menu.button_nums = len(menu.option_button_names)
            else:
                if option == 'cpu_only':
                    config['cpu_only'] = True
                else:
                    config['cpu_only'] = False
            
            if config['cpu_only']:
                pygame.display.set_mode(VIRTUAL_RES)
            else:
                pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)
            crt_shader.__init__(crt_shader.screen,VIRTUAL_RES=VIRTUAL_RES, cpu_only=config['cpu_only'])

        # for normal menu
        elif level.menu_state == 'title':
            if option == 'New game':
                # level.__init__()
                level.toggle_menu()
            elif option == 'Continue':
                if level.has_save:
                    pass
                else:
                    level.toggle_menu()
            elif option == 'Exit':
                save_config(config=config)
                pygame.quit()
                sys.exit()
        elif level.menu_state == 'menu':
            if option == 'New game':
                level.__init__()
                level.dialogue_init()
            elif option == 'Continue':
                level.title_screen()
            elif option == 'Exit':
                save_config(config=config)
                pygame.quit()
                sys.exit()

        if option == 'option':
            menu.menu_state = 'option'
            menu.button_nums = len(menu.option_button_names)
            menu.selection_index = 0

        if menu.button_nums != len(menu.button_list):
            menu.create_button()
        
    def display(self, surface, selection_num, name, config=False):
        if self.index == selection_num:
            pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_names(surface, name, self.index == selection_num, config)

