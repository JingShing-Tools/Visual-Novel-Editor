import pygame
from settings import *
from save_and_load import found_all_bgm

bgm_list = ['none']
def init_bgm_list():
    found_all_bgm('assets/audio/bgm/', bgm_list=bgm_list)

bgm_volume = 0.5
def set_bgm(bgm_name, change = False):
    if change:
        pygame.mixer.music.fadeout(1000)
        # pygame.mixer.music.unload()
    if bgm_name:
        if bgm_name == 'none':
            return
        path = 'assets/audio/bgm/'
        path = path + bgm_name + '.mp3'
        pygame.mixer.music.load(resource_path(path))
        pygame.mixer.music.set_volume(bgm_volume)
        pygame.mixer.music.play(-1)

def bgm_pause(pause=True):
    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

bgm_name='none'