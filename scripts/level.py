import pygame
from settings import *
from menu import Menu
from dialog import Dialog_box
from save_and_load import found_asset_imgs, found_max_scene
from music_player import bgm_pause, set_bgm, sound_dict

class Level:
    def __init__(self):
        # get the display surface
        self.game_paused = False
        bgm_pause(self.game_paused)
        
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
        # record how many times dialogue done
        self.dialogue_done_times = 0
        self.line_index = 0
        self.languages = ['english', 'tchinese', 'schinese']
        if config['default_lang'] in self.languages:
            self.language = config['default_lang']
        else:
            self.language = 'english'
        self.language_index = 0
        self.lines = lines_acts_all
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # dialog
        self.dialog = Dialog_box(self)

        # create stage
        # bgs
        self.bg_img = {
            'none': pygame.transform.scale(pygame.image.load(resource_path('assets/graphics/characters/none.png')), (152, 152)),
        }
        found_asset_imgs(folder_path='assets/graphics/stages/', img_dict=self.bg_img, allow_img_format=config['allow_img_format'])
        self.change_bg('bg')
        self.scene = 'bg'

        # save
        self.max_scene = found_max_scene('dialogues/'+ self.dialog.now_script_file_name +'.txt')
        self.has_save = False

        # user interface
        self.menu_state = 'none'
        self.menu = Menu(self)
        self.prev_menu_state = 'none'
        self.menu_list = self.menu.button_names

    def change_bg(self, bg_name=None, scale=True):
        if bg_name==None or bg_name=='none':
            bg_name = self.scene
        # scale bg background
        if scale:
            self.bg = pygame.transform.scale(self.bg_img[bg_name].copy(), REAL_RES)
        else:
            self.bg = self.bg_img[bg_name].copy()
        self.bg_rect = self.bg.get_rect(topleft = (0, 0))
        screen.blit(self.bg, self.bg_rect)

    def toggle_menu(self):
        self.game_paused = not(self.game_paused)
        if self.game_paused:
            if self.menu_state != 'title':
                bgm_pause(self.game_paused)
        else:
            if not(pygame.mixer.music.get_busy()):
                bgm_pause(self.game_paused)


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
            self.import_lines(all_lines_en, lines_acts_all)
        elif self.language == 'tchinese':
            self.import_lines(all_lines_tch, lines_acts_all)
        elif self.language == 'schinese':
            self.import_lines(all_lines_sch, lines_acts_all)

    def handle_control(self):
        keys = pygame.key.get_pressed()
        if self.dialog.show_textbox:
            self.dialog.display()
        if self.can_press_key:
            self.dialog.blit_press_hint()
            if keys[pygame.K_t] and not(self.dialog.select):
                self.dialog.refresh_lines()
                # this will clear text box
                self.dialog.show_textbox = True
                self.dialog.typing = True
                if self.dialogue_done_times == 0:
                    pass
                elif self.dialogue_done_times <= self.max_scene:
                    self.dialog.first_talk=True
                    # self.change_line_script(config['dialogue_file_name'], '@scene' + str(self.dialogue_done_times))
                    self.change_line_script(self.dialog.now_script_file_name, '@scene' + str(self.dialogue_done_times))
                else:
                    self.dialog.show_textbox = False
                    self.dialog.typing = False
                    self.dialog.ending = True
                    set_bgm(config['ending_bgm'])
                    self.change_bg(config['ending_bg'])
                    lines_acts_all.clear()
                if self.dialogue_done_times != 0:
                    self.language_change()
                self.press_key_time = pygame.time.get_ticks()
                self.can_press_key = False
                if len(self.lines)>0:
                    self.next_line_add(True)
            if keys[pygame.K_RETURN] and not(self.dialog.select):
                self.press_key_time = pygame.time.get_ticks()
                self.can_press_key = False
                if self.dialog.show_textbox and not(self.dialog.typing):
                    self.next_line_add()
            if keys[pygame.K_y]:
                self.press_key_time = pygame.time.get_ticks()
                self.can_press_key = False
                self.language_index = (self.language_index + 1)  % len(self.languages)
                self.language = self.languages[self.language_index]
                self.language_change()

    def change_line_script(self, script_name, flag=None, jump=False):
        # if you want to use '@jump' you need to make line_index = -1
        now_dia_file = script_name
        path = dia_fore_path + now_dia_file + now_dia_file_format
        if found_dialogue_or_not(now_dia_file+now_dia_file_format):
            load_dialogue(path, lines_acts_all, flag)
            if '_' in now_dia_file:
                now_dia_file = now_dia_file.split('_')[0]
            change_lines_all_langs(now_dia_file, flag)
            if jump:
                # I know this line is kinda weird but it work
                # also this line caused next line add need to add some if
                # like if line index < 0: line index = 0
                self.line_index = -1
                # self.dialog.multiline.append(self.lines[self.line_index])
                self.next_line_add()
    
    def next_line_add(self, using_talk_key = False):
        if using_talk_key:
            if self.line_index < len(self.lines):
                if self.line_index < 0:
                    self.line_index = 0
                self.dialog.add_line(self.lines[self.line_index])
                self.detect_command_lines()
            sound_dict['talk'].play()
        elif self.line_index < len(self.lines) - 1:
            self.line_index += 1
            self.dialog.add_line(self.lines[self.line_index])
            self.dialog.typing = True
            self.detect_command_lines()
            sound_dict['talk'].play()
        elif self.line_index == len(self.lines) - 1:
            self.line_index = 0
            self.dialog.show_textbox = False
            self.dialogue_done_times+=1

    def detect_command_lines(self):
        if self.lines[self.line_index][0] == '#':
                self.next_line_add()
        elif '@jump' in self.lines[self.line_index]:
            pass
        elif '@' in self.lines[self.line_index] and not(':' in self.lines[self.line_index]):
            self.next_line_add()

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not(self.can_press_key):
            if current_time - self.press_key_time >= self.press_key_cd:
                self.can_press_key = True