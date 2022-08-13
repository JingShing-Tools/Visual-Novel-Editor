import pygame, sys
from settings import *
from level import Level
from music_player import *

class Game:
    def __init__(self, fullscreen = False):
        # general setup
        pygame.init()
        pygame.mouse.set_visible(False)
        self.fullscreen = fullscreen
        self.Full_screen()

        pygame.display.set_caption('In no mood') # game title
        pygame.display.set_icon(pygame.image.load(resource_path('assets/graphics/icon/icon.png')))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # level
        self.level = Level()
        self.level.title_screen()
        self.level.menu_state = 'title'
        init_bgm_list()
        init_sound_list()
        if config['intro_bgm']=='none':
            self.bgm_name = bgm_list[0] if len(bgm_list) <= 1 else bgm_list[1]
        else:
            self.bgm_name = config['intro_bgm']
        set_bgm(self.bgm_name)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.level.toggle_menu()
                    elif event.key == pygame.K_ESCAPE:
                        self.level.title_screen()
                    elif event.key == pygame.K_0:
                        crt_shader.__init__(crt_shader.screen, (crt_shader.style + 1) % 3, VIRTUAL_RES)
                    elif event.key == pygame.K_f:
                        self.fullscreen = not(self.fullscreen)
                        self.Full_screen()
                    elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                        self.level.dialog.scrolling_text_time=5
                    elif event.key == pygame.K_u:
                        self.cpu_gpu_switch()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                        self.level.dialog.scrolling_text_time=self.level.dialog.or_delay

            screen.fill('black')
            self.level.run()
            crt_shader()
            self.clock.tick(FPS)
            pygame.display.set_caption(config['window_caption'] + ' ' + str(round(self.clock.get_fps())))
    
    def Full_screen(self):
        if not(config['only_cpu']):
            if not(self.fullscreen):
                pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)
            else:
                pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL|pygame.FULLSCREEN)
        else:
            if not(self.fullscreen):
                pygame.display.set_mode(VIRTUAL_RES)
            else:
                pygame.display.set_mode(VIRTUAL_RES, pygame.FULLSCREEN)

    def cpu_gpu_switch(self):
        config['only_cpu'] = not(config['only_cpu'])
        self.Full_screen()
        crt_shader.__init__(crt_shader.screen,VIRTUAL_RES=VIRTUAL_RES, cpu_only=config['only_cpu'])

    def quit_game(self):
        pygame.quit()
        sys.exit()

need_helper = config['need_help']
if __name__ == '__main__':
    game = Game()
    if need_helper:
        from threading import Thread
        from gui_helper import Gui_helper
        def gui_run():
            gui_help = Gui_helper(game)
            gui_help.run()
        thread1 = Thread(target=gui_run)
        thread1.setDaemon(True)
        thread1.start()
    game.run()