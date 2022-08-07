import pygame
def set_bgm(bgm_name, change = False):
    if change:
        pygame.mixer.music.unload()
    if bgm_name:
        path = 'assets/audio/bgm/'
        path = path + bgm_name + '.mp3'
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)

def bgm_pause(pause=True):
    if pause:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

bgm_name='light_tune'