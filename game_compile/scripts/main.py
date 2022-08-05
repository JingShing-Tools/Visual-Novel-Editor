import pygame, sys
from settings import *
from level import Level

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
                        crt_shader.__init__(crt_shader.screen, (crt_shader.style + 1) % 3)
                    elif event.key == pygame.K_f:
                        self.fullscreen = not(self.fullscreen)
                        self.Full_screen()
                if event.type == pygame.MOUSEWHEEL:
                    self.level.visible_sprites.zoom_scale += event.y * 0.03

            screen.fill('black')
            self.level.run()
            crt_shader()
            self.clock.tick(FPS)
            pygame.display.set_caption('In no mood' + ' ' + str(round(self.clock.get_fps())))
    
    def Full_screen(self):
        if not(self.fullscreen):
            pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL)
        else:
            pygame.display.set_mode(REAL_RES, pygame.DOUBLEBUF|pygame.OPENGL|pygame.FULLSCREEN)

    def quit_game(self):
        pygame.quit()
        sys.exit()

need_helper = True
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