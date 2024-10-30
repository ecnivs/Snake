import pygame as pg
from settings import *
from pygame.math import Vector2
import sys

class Snake:
    def __init__(self):
        pg.init()
        self.cell_size = CELL_SIZE
        self.cell_number = CELL_NUMBER
        self.screen = pg.display.set_mode((self.cell_number * self.cell_size, self.cell_number * self.cell_size))
        
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction =  Vector2(1,0)

        self.head_up = pg.image.load(HEAD_UP).convert_alpha()
        self.head_down = pg.image.load(HEAD_DOWN).convert_alpha()
        self.head_right = pg.image.load(HEAD_RIGHT).convert_alpha()
        self.head_left = pg.image.load(HEAD_LEFT).convert_alpha()

        self.tail_up = pg.image.load(TAIL_UP).convert_alpha()
        self.tail_down = pg.image.load(TAIL_DOWN).convert_alpha()
        self.tail_right = pg.image.load(TAIL_RIGHT).convert_alpha()
        self.tail_left = pg.image.load(TAIL_LEFT).convert_alpha()  

        
        self.body_vertical = pg.image.load(BODY_VER).convert_alpha()
        self.body_horizontal = pg.image.load(BODY_HOR).convert_alpha()

        
        self.body_tr = pg.image.load(BODY_TR).convert_alpha()
        self.body_tl = pg.image.load(BODY_TL).convert_alpha()
        self.body_br = pg.image.load(BODY_BR).convert_alpha()
        self.body_bl = pg.image.load(BODY_BL).convert_alpha()
        self.crunch_sound = pg.mixer.Sound(CRUNCH_WAV)

        self.apple = pg.image.load(APPLE).convert_alpha()
        self.font = pg.font.Font(FONT, 25)

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    snake = Snake()
    snake.run()
