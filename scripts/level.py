import pygame
from settings import *
from menu import Menu
from dialog import Dialog_box
from save_and_load import found_save_or_not

class Level:
    def __init__(self):
        # get the display surface
        
        self.game_paused = False
        
        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # controls
        # key cooldown
        self.can_press_key = True
        self.press_key_time = None
        self.press_key_cd = 200

        # dialog lines
        self.line_index = 0
        self.language = 'english'
        self.languages = ['english', 'tchinese', 'schinese']
        self.language_index = 0
        self.lines = npc_lines_all
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # dialog
        self.dialog = Dialog_box()
        self.speak_sound = pygame.mixer.Sound(resource_path('assets/audio/menu4.wav'))
        self.speak_sound.set_volume(0.3)

        # create stage
        self.create_stage()

        # save
        self.has_save = False
        found_save_or_not(self)

        # user interface
        self.menu_state = 'none'
        self.menu = Menu(self)
        self.prev_menu_state = 'none'
        self.menu_list = self.menu.button_names

    def create_stage(self):
        self.bg = pygame.image.load(resource_path('assets/graphics/stages/bg.png')).convert()
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))

    def toggle_menu(self):
        self.game_paused = not(self.game_paused)

    def title_screen(self):
        self.prev_menu_state = self.menu_state
        if self.menu_state != 'menu' or self.menu_state != 'title' or self.menu_state != 'dead_screen':
            self.toggle_menu()
            self.menu_state = 'menu'
        elif self.menu_state == 'menu' or self.menu_state == 'title' or self.menu_state == 'dead_screen':
            self.toggle_menu()
            self.menu_state  = 'none'

    def run(self):
        screen.blit(self.bg, self.bg_rect)
        if self.game_paused:
            # menu system showed
            if self.menu_state == 'title' or self.menu_state == 'menu' or self.menu_state == 'dead_screen':
                self.menu.display()
        else:
            if self.menu_state != 'none':
                self.menu_state = 'none'
            # run the game
            # update and draw the game
            self.handle_control()
            self.cooldown()
            crt_shader()

    # player control section
    def import_lines(self, send_list, get_list):
        get_list.clear()
        for line in send_list:
            get_list.append(line)
    
    def language_change(self):
        if self.language == 'english':
            self.import_lines(npc_lines_en, npc_lines_all)
        elif self.language == 'tchinese':
            self.import_lines(npc_lines_tch, npc_lines_all)

    def handle_control(self):
        keys = pygame.key.get_pressed()
        if self.dialog.show_textbox:
            self.dialog.display()
        if self.can_press_key:
            self.dialog.blit_press_hint()
            if keys[pygame.K_t]:
                self.bg = pygame.image.load(resource_path('assets/graphics/stages/bg_2.png')).convert()
                self.bg_rect = self.bg.get_rect(topleft = (0, 0))
                self.press_key_time = pygame.time.get_ticks()
                self.can_press_key = False
                self.dialog.refresh_lines()
                self.dialog.show_textbox = True
                self.dialog.typing = True
                if len(self.lines)>0:
                    self.dialog.add_line(self.lines[self.line_index])
                    self.speak_sound.play()
            if keys[pygame.K_RETURN]:
                self.press_key_time = pygame.time.get_ticks()
                self.can_press_key = False
                if self.dialog.show_textbox and not(self.dialog.typing):
                    if self.line_index < len(self.lines) - 1:
                        self.line_index += 1
                        self.dialog.add_line(self.lines[self.line_index])
                        self.dialog.typing = True
                        self.speak_sound.play()
                    elif self.line_index == len(self.lines) - 1:
                        self.line_index = 0
                        self.dialog.show_textbox = False
                        self.status = 'idle'
            if keys[pygame.K_y]:
                self.press_key_time = pygame.time.get_ticks()
                self.can_press_key = False
                self.language_index = (self.language_index + 1)  % len(self.languages)
                self.language = self.languages[self.language_index]
                self.language_change()

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not(self.can_press_key):
            if current_time - self.press_key_time >= self.press_key_cd:
                self.can_press_key = True