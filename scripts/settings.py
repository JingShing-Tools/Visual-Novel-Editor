import os, sys
import pygame
from crt_shader import Graphic_engine
from save_and_load import load_config

pygame.init()

# for packing game
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

config = {
	'need_help':True,
	'title_screen_text':'Crt TV',
	'window_caption':'still_loading',
	'dialogue_file_name':'default',
	'shader_default':1,
	'default_lang':'english',
	'ending':'Nothing here',
	'resolution':(800, 600),
	'window_size':(1280, 720),
	'allow_img_format':['png', 'jpg', 'bmp'],
	'allow_audio_format':['mp3', 'wav'],
	'text_frame_alpha':200,
	'text_frame_color':(255,255,255),
	'title_cover_img':'bg2',
	'only_cpu':False,
	'hint_use_t':'press \'T\' to talk',
	'hint_use_enter':'press \'enter\' to continue',
}
load_config(config=config)

# game setup
WIDTH    = config['resolution'][0]
HEIGHT   = config['resolution'][1]
VIRTUAL_RES = config['resolution']
REAL_RES = config['window_size']
FPS = 60
if config['only_cpu']:
	pygame.display.set_mode(VIRTUAL_RES)
else:
	pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)
screen = pygame.Surface(VIRTUAL_RES).convert((255, 65280, 16711680, 0))
crt_shader = Graphic_engine(screen, config['shader_default'], VIRTUAL_RES, cpu_only=config['only_cpu'])

# ui
BAR_HEIGHT = 20
UI_FONT = resource_path('assets/graphics/font/joystix.ttf')
dialogue_font = resource_path('assets/graphics/font/youyuan.ttf')
UI_FONT_SIZE = 18
 
# general colors
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

from save_and_load import found_dialogue_or_not, load_dialogue
# npc dialogue
# if had dialogue file then read it
global all_lines_en, all_lines_tch, all_lines_sch
all_lines_en = []
all_lines_tch = []
all_lines_sch = []
dia_fore_path = 'dialogues/'
now_dia_file_format = '.txt'

def change_lines_all_langs(now_dia_file, flag=None):
	global all_lines_en, all_lines_tch, all_lines_sch
	if found_dialogue_or_not(now_dia_file + now_dia_file_format):
		load_dialogue(dia_fore_path+now_dia_file+now_dia_file_format, all_lines_en, flag)
	else:
		all_lines_en = ['Just give up.', 'You can\'t go out there.', 'No chance.', 'We just stuck in here.']

	if found_dialogue_or_not(now_dia_file + '_tch' + now_dia_file_format):
		load_dialogue(dia_fore_path + now_dia_file + '_tch' + now_dia_file_format, all_lines_tch, flag)
	else:
		all_lines_tch = ['放棄吧。', '你不可能出去的。', '沒有任何可能性。', '我們被困在這了。']

	if found_dialogue_or_not(now_dia_file + '_sch' + now_dia_file_format):
		load_dialogue(dia_fore_path + now_dia_file + '_sch' + now_dia_file_format, all_lines_sch, flag)
	else:
		all_lines_sch = ['放弃吧。', '你不可能出去的。', '没有任何可能性。', '我们被困在这了。']

change_lines_all_langs(config['dialogue_file_name'])
if config['default_lang'] == 'english':
	lines_acts_all = all_lines_en.copy()
elif config['default_lang'] == 'schinese':
	lines_acts_all = all_lines_sch.copy()
elif config['default_lang'] == 'tchinese':
	lines_acts_all = all_lines_tch.copy()
else:
	lines_acts_all = all_lines_en.copy()