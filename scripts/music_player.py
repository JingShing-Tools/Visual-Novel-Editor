import pygame
from settings import *
from save_and_load import found_all_bgm, found_asset_sounds

bgm_list = ['none']
sound_dict = {'none':None}
def init_bgm_list():
    found_all_bgm('assets/audio/bgm/', bgm_list=bgm_list)

def init_sound_list(volume = 0.1):
    found_asset_sounds(folder_path='assets/audio/sound/', sound_dict=sound_dict, allow_sound_format=config['allow_audio_format'])
    for sound in sound_dict:
        sound_dict[sound].set_volume(volume)

def set_bgm(bgm_name, change = False, bgm_volume = 0.3):
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