import  Buttons
from main_tetris import *

from pygame.locals import *

pygame.init()
resolution=0
class Button_Control:
    def __init__(self):
        self.main()

    def display(self):
        self.screen = pygame.display.set_mode((650,600))
        pygame.display.set_caption("Tetris")

    # 2 ??????
    def update_display(self):
        self.screen.fill((30,150,255))
        self.Button1.create_button(self.screen, (115,150,40), 225, 170, 200, 100, 1, "Start", (255,255,255))
        self.Button2.create_button(self.screen, (115,150,40), 225, 320, 200, 100, 1, "Exit", (255,255,255))
        pygame.display.flip()



    def main(self):
        self.Button1 = Buttons.Button()
        self.Button2 = Buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        start()
                    elif self.Button2.pressed(pygame.mouse.get_pos()):
                        pygame.quit()

if __name__ == '__main__':
    obj = Button_Control()
