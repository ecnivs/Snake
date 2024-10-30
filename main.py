import pygame as pg
import sys

class Snake:
    def __init__(self):
        pg.init()
        self.cell_size = 40
        self.cell_number = 20
        self.screen = pg.display.set_mode((self.cell_number * self.cell_size, self.cell_number * self.cell_size))
        
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True

    def update(self):
        self.delta_time = self.clock.tick(60)
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
