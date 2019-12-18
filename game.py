import pygame, random

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Tetris")
ended = False
fast = False
locked = False
falling_tetrominos = []
set_tetrominos = []
clock = pygame.time.Clock()
fall_cooldown = 0


class Tetromino:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        falling_tetrominos.append(self)
        self.rect = pygame.Rect(self.x, self.y, 25, 25)

    def fall(self):
        self.rect.y += 25
        self.y +=25

    def move(self):
        if pressed[pygame.K_RIGHT]:
            self.x += 25
            if self.x > 375:
                self.x = 0
        if pressed[pygame.K_LEFT]:
            self.x -= 25
            if self.x < 0:
                self.x = 375

    def drawtetromino(self):
        pygame.draw.rect(screen, self.color[0], pygame.Rect(self.x, self.y, 21, 21))
        pygame.draw.polygon(screen, self.color[1], (
        (self.x, self.y), (self.x + 3, self.y + 3), (self.x + 21, self.y + 3), (self.x + 24, self.y)))
        pygame.draw.polygon(screen, self.color[2], (
        (self.x, self.y), (self.x + 3, self.y + 3), (self.x + 3, self.y + 21), (self.x, self.y + 24)))
        pygame.draw.polygon(screen, self.color[3], (
        (self.x, self.y + 24), (self.x + 3, self.y + 21), (self.x + 21, self.y + 21), (self.x + 24, self.y + 24)))
        pygame.draw.polygon(screen, self.color[4], (
        (self.x + 24, self.y + 24), (self.x + 21, self.y + 21), (self.x + 21, self.y + 3), (self.x + 24, self.y)))


def appear():
    tetrominonum = random.randint(0, 6)

    if tetrominonum == 0:
        # I tetromino
        colors = [(129, 184, 231),
                  (179, 223, 250),
                  (146, 202, 238),
                  (76, 126, 189),
                  (96, 157, 213)]

        Tetromino(175, 0, colors)
        Tetromino(175, 25, colors)
        Tetromino(175, 50, colors)
        Tetromino(175, 75, colors)
    elif tetrominonum == 1:
        # L-reversed tetromino
        colors = [(60, 121, 159),
                  (119, 168, 249),
                  (124, 164, 201),
                  (46, 62, 116),
                  (53, 75, 148)]

        Tetromino(200, 0, colors)
        Tetromino(200, 25, colors)
        Tetromino(200, 50, colors)
        Tetromino(175, 50, colors)
    elif tetrominonum == 2:
        # L tetromino
        colors = [(208, 117, 64),
                  (223, 181, 112),
                  (219, 129, 49),
                  (186, 61, 63),
                  (153, 88, 34)]

        Tetromino(175, 0, colors)
        Tetromino(175, 25, colors)
        Tetromino(175, 50, colors)
        Tetromino(200, 50, colors)

    elif tetrominonum == 3:
        # O tetromino
        colors = [(255, 212, 37),
                  (226, 193, 159),
                  (235, 225, 65),
                  (163, 140, 34),
                  (203, 180, 55)]

        Tetromino(175, 0, colors)
        Tetromino(175, 25, colors)
        Tetromino(200, 0, colors)
        Tetromino(200, 25, colors)
    elif tetrominonum == 4:
        # S tetromino
        colors = [(146, 165, 66),
                  (214, 208, 117),
                  (164, 218, 80),
                  (110, 160, 69),
                  (139, 179, 89)]

        Tetromino(175, 0, colors)
        Tetromino(175, 25, colors)
        Tetromino(200, 0, colors)
        Tetromino(150, 25, colors)
    elif tetrominonum == 5:
        # Z tetromino
        colors = [(214, 32, 39),
                  (219, 140, 129),
                  (220, 89, 70),
                  (149, 41, 39),
                  (178, 40, 38)]

        Tetromino(175, 0, colors)
        Tetromino(225, 25, colors)
        Tetromino(200, 0, colors)
        Tetromino(200, 25, colors)
    else:
        # T tetromino
        colors = [(151, 68, 150),
                  (190, 150, 190),
                  (163, 101, 170),
                  (118, 45, 123),
                  (116, 51, 135)]

        Tetromino(175, 0, colors)
        Tetromino(175, 25, colors)
        Tetromino(200, 0, colors)
        Tetromino(150, 0, colors)


appear()

while not ended:

    screen.fill((0, 0, 32))
    a=0
    for i in range(24):
        pygame.draw.line(screen, (55,55,55), (0, a), (400, a))
        a+=25
        if a == 600:
            a=0
    for i in range(16):
        pygame.draw.line(screen, (50, 50, 50), (a, 0), (a, 600))
        a+=25
    pressed = pygame.key.get_pressed()

    for falling_tetromino in falling_tetrominos:
        falling_tetromino.drawtetromino()
        falling_tetromino.move()

    for settetromino in set_tetrominos:
        settetromino.drawtetromino()

    if fall_cooldown >= 50:
        for falling_tetromino in falling_tetrominos:
            falling_tetromino.fall()
        fall_cooldown = 0
    pygame.display.flip()

    if pressed[pygame.K_SPACE]:
        fast = True

    if fast:
        fall_cooldown = 50
    elif pressed[pygame.K_DOWN]:
        fall_cooldown += 8
    else:
        fall_cooldown += 1

    for falling_tetromino in falling_tetrominos:
        for settetromino in set_tetrominos:
            if falling_tetromino.rect.colliderect(settetromino.rect):
                locked = True
        if falling_tetromino.y == 575 and not locked:
            locked = True

    if locked:
        set_tetrominos += falling_tetrominos
        falling_tetrominos = []
        appear()
        locked = False

    clock.tick(50)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ended = True
