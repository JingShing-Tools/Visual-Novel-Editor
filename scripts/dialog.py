import pygame
from settings import *
import re
from music_player import *
from save_and_load import found_asset_imgs
from options_menu import Option_menu

class Dialog_box:
    def __init__(self, level):
        self.level = level
        self.language = self.level.language
        
        self.screen_width = screen.get_size()[0]
        self.screen_height = screen.get_size()[1]
        self.now_script_file_name = config['dialogue_file_name']
        if self.language == 'english':
            pass
        elif self.language == 'schinese':
            self.now_script_file_name += '_sch'
        elif self.language == 'tchinese':
            self.now_script_file_name += '_tch'

        self.font = pygame.font.Font(dialogue_font, 25)
        self.font_AA = False
        # textbox_size = (700,200)
        textbox_size = (WIDTH/1.2,HEIGHT/3)
        self.textbox_surf = pygame.Surface(textbox_size, pygame.SRCALPHA)
        self.textbox_bg_surf = pygame.Surface(textbox_size, pygame.SRCALPHA)
        self.textbox_rect = self.textbox_surf.get_rect(center=(self.screen_width/2, self.screen_height/2 + 30))
        # self.textbox_bg_rect = self.textbox_rect
        self.border_rect = self.textbox_surf.get_rect(topleft=(0, 0))

        # talker icon
        self.talker_image_or = {
            'none': pygame.transform.scale(pygame.image.load(resource_path('assets/graphics/characters/none.png')), (152, 152)),
        }
        # auto load imgs
        found_asset_imgs(folder_path='assets/graphics/characters/', img_dict=self.talker_image_or, transform=True, allow_img_format=config['allow_img_format'],scale=(WIDTH/4, WIDTH/4))
        self.talker_img_name = {
            'none':'none',
            'Unknown':'none',
            'player': 'player',
            'npc' : 'npc',
            }
        self.talker_image = self.talker_image_or['none'].copy()
        self.talker_image_rect = self.talker_image.get_rect(bottomleft = self.textbox_rect.topleft)

        # line progress
        self.text = 'Hello world!'
        # all line and command
        self.multiline = []
        # only line need to print
        self.multi_label = []
        self.multiline_max_line = 4
        self.line_internal = 35
        self.text_frame_alpha = config['text_frame_alpha']
        self.text_frame_color_value = config['text_frame_color']
        self.text_frame_color = (self.text_frame_color_value[0], self.text_frame_color_value[1], self.text_frame_color_value[2], self.text_frame_alpha)

        self.show_textbox = False
        self.typing = False
        self.or_delay = 35
        self.scrolling_text_time = self.or_delay

        self.ending = False
        # self.bg_color = 'white'
        # self.bg_alpha = 0

        # npc and player name
        self.npcs_list = ['npc']
        self.player_list = ['player']
        self.text_color_dict = {
            'npc':'black',
            'player':'red'
        }
        self.talker_type = 'none'
        self.talker_name = 'Unknown'
        self.talker_name_surf = self.font.render(self.talker_name, self.font_AA, TEXT_COLOR)
        self.talker_name_rect = self.talker_name_surf.get_rect()
        self.talker_name_frame_extend = (10, 10)

        # options
        self.options = {}
        self.option_names = []
        self.select  = False
        self.option_menu = Option_menu(self)

    def gradual_typing(self):
        if self.typing:
            line_num = len(self.multiline)
            self.multi_label.clear()
            rendering = ''
            for line_id, lines in enumerate(self.multiline):
                print(self.multiline)
                print(self.options)
                self.textbox_surf.fill(color=(0,0,0,0))
                self.textbox_bg_surf.fill(self.text_frame_color)
                pygame.draw.rect(self.textbox_bg_surf, "black", self.border_rect, 6)
                if lines[0]=='#':
                    pass
                elif '@' in lines and not(':' in lines):
                    if '=' in lines:
                        info_act = re.split('@|=| ', lines)
                        # get 'talker.img'
                        talker = info_act[1]
                        if '.img' in talker:
                            talker_img_name = info_act[-1]
                            talker = talker.split('.')[0]
                            if talker_img_name == 'p':
                                talker_img_name = 'player'
                            elif talker_img_name == 'n':
                                talker_img_name = 'npc'
                            if talker == 'p':
                                talker = 'player'
                            elif talker == 'n':
                                talker = 'npc'
                            self.talker_img_name[talker] = talker_img_name
                            if not(talker in self.npcs_list) and not(talker in self.player_list):
                                self.npcs_list.append(talker)
                            # only do once and delete from cache
                            # self.multiline.pop(line_id)
                            # change to no meaning command
                        elif '.color' in talker:
                            color_name = info_act[-1]
                            talker = talker.split('.')[0]
                            if talker == 'textbox':
                                self.text_frame_color_value = list(map(int, color_name.split(',')))
                                self.text_frame_color = (self.text_frame_color_value[0], self.text_frame_color_value[1], self.text_frame_color_value[2], self.text_frame_alpha)
                            else:
                                if talker == 'p':
                                    talker = 'player'
                                elif talker == 'n':
                                    talker = 'npc'
                            if ',' in color_name:
                                color_name = list(map(int, color_name.split(',')))
                                self.text_color_dict[talker] = color_name
                        elif '.alpha' in talker:
                            alpha_value = int(info_act[-1])
                            object = talker.split('.')[0]
                            if object == 'textbox':
                                self.text_frame_alpha = alpha_value
                                self.text_frame_color = (self.text_frame_color_value[0], self.text_frame_color_value[1], self.text_frame_color_value[2], self.text_frame_alpha)
                        elif 'bgm' in talker:
                            bgm_name = info_act[-1]
                            set_bgm(bgm_name, True)
                        elif 'bg' in talker:
                            bg_img_name = info_act[-1]
                            self.level.scene = bg_img_name
                            self.level.change_bg()
                        elif 'delay' in talker:
                            delay = info_act[-1]
                            self.or_delay = int(delay)
                            self.scrolling_text_time = self.or_delay
                        elif 'option' in lines:
                            if '.clear' in lines:
                                self.options.clear()
                            elif '.text' in lines:
                                info_act = re.split('@|=|\.', lines)
                                option = info_act[1]
                                text = info_act[-1]
                                self.options[option]['text']=text
                            elif '.com' in lines or '.command' in lines:
                                info_act = re.split('@|=|\.', lines)
                                option = info_act[1]
                                command = info_act[-1]
                                self.options[option]['command']='@'+command
                            else:
                                info_act = re.split('@|=', lines)
                                option = info_act[1]
                                text = info_act[-1]
                                self.options[option]={
                                    'text':text,
                                    'command':'@',
                                }
                        elif not('.' in talker):
                            character_name = info_act[-1]
                            if talker == 'npc' or talker == 'n':
                                if character_name == 'clear':
                                    self.npcs_list.clear()
                                else:
                                    if not(character_name in self.npcs_list):
                                        self.npcs_list.append(character_name)
                                        self.text_color_dict[character_name]='black'
                            elif talker == 'player' or talker == 'p':
                                if character_name == 'clear':
                                    self.player_list.clear()
                                else:
                                    if not(character_name in self.player_list):
                                        self.player_list.append(character_name)
                                        self.text_color_dict[character_name]='red'
                            if not(character_name in self.talker_img_name):
                                self.talker_img_name[character_name] = 'none'
                        self.multiline[line_id]='@'
                        # to clear command not to repeat

                    elif 'select' in lines:
                        self.multiline[line_id]='@'
                        self.select = True
                        self.option_menu.show_options(line_id)

                    elif 'jump' in lines:
                        self.multiline[line_id]='@'
                        info_act = re.split('@|=| ', lines)
                        tag = info_act[-1]
                        if len(info_act)==4:
                            self.now_script_file_name = info_act[-2]
                        self.level.change_line_script(self.now_script_file_name, '@' + tag, True)
                        self.refresh_lines(3)

                    elif 'refresh' in lines:
                        self.multiline[line_id]='@'
                        self.refresh_lines(3)
                    else:
                        self.multiline[line_id]='@'

                else:
                    if ':' in lines:
                        talker_and_line = lines.split(':')
                        if len(talker_and_line)>1:
                            talker = talker_and_line[0]
                            if (talker in self.player_list) or (talker == 'player' or talker == 'p'):
                                if talker != 'player' and talker != 'p':
                                    self.talker_name = talker
                                else:
                                    if len(self.player_list)>0:
                                        self.talker_name = self.player_list[0]
                                    else:
                                        self.talker_name = 'Unknown'
                                self.talker_type = 'player'
                            else:
                                if talker != 'npc' and talker != 'n':
                                    self.talker_name = talker
                                else:
                                    if len(self.npcs_list)>0:
                                        self.talker_name = self.npcs_list[0]
                                    else:
                                        self.talker_name = 'Unknown'
                                self.talker_type = 'npc'
                            if self.talker_type == 'npc':
                                self.talker_image_rect = self.talker_image.get_rect(bottomright = self.textbox_rect.topright)
                            elif self.talker_type == 'player':
                                self.talker_image_rect = self.talker_image.get_rect(bottomleft = self.textbox_rect.topleft)
                            lines = talker_and_line[-1]

                    # to determine if img name has this character
                    if self.talker_name in self.talker_img_name:
                        self.talker_image = self.talker_image_or[self.talker_img_name[self.talker_name]].copy()
                        # if switch chracter talk refresh text
                        
                    elif self.talker_name in self.talker_image_or:
                        self.talker_image = self.talker_image_or[self.talker_name].copy()

                    else:
                        self.talker_image = self.talker_image_or[self.talker_img_name[self.talker_type]].copy()
                        # if switch chracter talk refresh text

                    if line_num > 1 and line_id < line_num - 1:
                        row_text = self.font.render(lines, self.font_AA, self.text_color_dict[self.talker_name])
                        self.multi_label.append(row_text)

                    elif line_id == line_num - 1:
                        # gradual type part
                        self.multi_label.append(self.text)
                        self.blit_textbox_bg()
                        for char in lines:
                            sound_dict['typing'].play()
                            pygame.time.delay(self.scrolling_text_time)
                            pygame.event.clear()

                            rendering = rendering + char
                            if self.talker_name in self.text_color_dict:
                                pass
                            else:
                                self.text_color_dict[self.talker_name] = 'black'
                            rendered_text = self.font.render(rendering, self.font_AA, self.text_color_dict[self.talker_name])

                            self.multi_label[-1] = rendered_text
                            for line in range(len(self.multi_label)):
                                self.textbox_surf.blit(self.multi_label[line], (20, 30 + line * self.line_internal))
                                screen.blit(self.textbox_surf, self.textbox_rect)
                                crt_shader()

        self.typing = False

    def get_option_names(self):
        self.option_names.clear()
        for name in self.options:
            self.option_names.append(name)

    def show_talker_name(self):
        if self.talker_name != 'none':
            self.talker_name_surf = self.font.render(self.talker_name, self.font_AA, TEXT_COLOR)
            self.talker_name_rect = self.talker_name_surf.get_rect(bottomright = self.talker_image_rect.bottomright)
            if self.talker_type == 'player':
                self.talker_name_rect = self.talker_name_surf.get_rect(bottomleft = self.talker_image_rect.bottomright)
            elif self.talker_type == 'npc':
                self.talker_name_rect = self.talker_name_surf.get_rect(bottomright = self.talker_image_rect.bottomleft)
            else:
                self.talker_name_rect = self.talker_name_surf.get_rect(bottomleft = self.talker_image_rect.bottomleft)
            pygame.draw.rect(screen, UI_BG_COLOR, self.talker_name_rect.inflate(self.talker_name_frame_extend))
            screen.blit(self.talker_name_surf, self.talker_name_rect)
            pygame.draw.rect(screen, UI_BORDER_COLOR, self.talker_name_rect.inflate(self.talker_name_frame_extend), 3)

    def add_line(self, text):
        self.text = text
        if len(self.multi_label) <= self.multiline_max_line - 1:
            self.multiline.append(self.text)
        else:
            self.refresh_lines()
            self.multiline.append(self.text)

    def find_prev_line(self, lines, line_id):
        if line_id < 0 and line_id*-1 > len(lines):
            return
        else:
            return lines[line_id]
    def refresh_lines(self, mode=1):
        # delay betwean refreshs
        delay = min(1000, self.scrolling_text_time * 40)
        pygame.time.delay(delay)
        pygame.event.clear()
        self.level.can_press_key = False
        self.level.press_key_time = pygame.time.get_ticks()

        if mode == 1:
            self.multiline.clear()
            self.multi_label.clear()
        elif mode == 2:
            self.multi_label.clear()
        elif mode == 3:
            line_id = -1
            if len(self.multiline)>0:
                last_line = self.multiline[-1]
                if '@jump' in last_line:
                    pass
                else:
                    while ('@' in last_line and not':' in last_line):
                        last_line = self.find_prev_line(self.multiline, line_id-1)
                    self.multiline.clear()
                    self.multi_label.clear()
                    if last_line:
                        self.multiline.append(last_line)
                        self.gradual_typing()

    def result_print(self):
        self.blit_textbox_bg()
        screen.blit(self.textbox_surf, self.textbox_rect)
        crt_shader()

    def blit_textbox_bg(self):
        pygame.draw.rect(self.textbox_bg_surf, "black", self.border_rect, 6)
        screen.blit(self.textbox_bg_surf, self.textbox_rect)
        screen.blit(self.talker_image, self.talker_image_rect)
        self.show_talker_name()

    def blit_press_hint(self):
        x = self.screen_width / 2
        y = self.screen_height - 100
        thickness = 2
        text = config['hint_use_t'] if (len(self.multiline) == 0 or not(self.show_textbox)) else config['hint_use_enter']
        if self.ending:
            if self.language == 'english':
                text = config['ending']
            elif self.language == 'tchinese':
                text = config['ending_tch']
            elif self.language == 'schinese':
                text = config['ending_sch']
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
        text = self.font.render(text, self.font_AA, color)
        text_rect = text.get_rect(center = (x, y))
        screen.blit(text, text_rect)

    def display(self):
        if self.show_textbox:
            if self.typing:
                self.gradual_typing()
            self.result_print()
        if self.select:
            self.option_menu.display()