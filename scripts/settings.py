import os, sys
import pygame
from crt_shader import Graphic_engine

pygame.init()

# for packing game
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		absolute_path = os.path.join(sys._MEIPASS, relative)
	else:
		absolute_path = os.path.join(relative)
	return absolute_path

# game setup
WIDTH    = 1280
HEIGHT   = 720
VIRTUAL_RES = (800, 600)
REAL_RES = (WIDTH, HEIGHT)
screen = pygame.Surface(VIRTUAL_RES).convert((255, 65280, 16711680, 0))
pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)
crt_shader = Graphic_engine(screen)
FPS      = 60

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
if found_dialogue_or_not('default.txt'):
    all_lines_en = load_dialogue('dialogues/default.txt')
else:
    all_lines_en = ['Just give up.', 'You can\'t go out there.', 'No chance.', 'We just stuck in here.']

if found_dialogue_or_not('default_tch.txt'):
    all_lines_tch = load_dialogue('dialogues/default_tch.txt')
else:
    all_lines_tch = ['放棄吧。', '你不可能出去的。', '沒有任何可能性。', '我們被困在這了。']
# npc_lines_sch = ['放弃吧。', '你不可能出去的。', '没有任何可能性。', '我们被困在这了。']

lines_acts_all = all_lines_en.copy()
