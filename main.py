from settings import *
from snake import Snake

class Core:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
        self.snake = Snake()

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True

    def render(self):
        self.screen.fill((175,215,70))
        self.draw_grass()
        pg.display.flip()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(CELL_NUMBER):
            if row % 2 == 0:  
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pg.Rect(col * CELL_SIZE,row * CELL_SIZE,CELL_SIZE,CELL_SIZE)
                        pg.draw.rect(self.screen,grass_color,grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pg.Rect(col * CELL_SIZE,row * CELL_SIZE,CELL_SIZE,CELL_SIZE)
                        pg.draw.rect(self.screen,grass_color,grass_rect)

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
            self.render()
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    core = Core()
    core.run()
