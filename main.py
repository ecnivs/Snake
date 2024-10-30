from settings import *
from snake import Snake

class Core:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.snake = Snake(self.screen)
        self.grass_color = (167,209,61)
        self.apple = pg.image.load(APPLE).convert_alpha()
        self.font = pg.font.Font(FONT, 25)

    def render(self):
        self.screen.fill((175,215,70))
        self.draw_grass()
        self.snake.draw_snake()
        pg.display.flip()

    def draw_grass(self):
        for row in range(CELL_NUMBER):
            if row % 2 == 0:  
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pg.Rect(col * CELL_SIZE,row * CELL_SIZE,CELL_SIZE,CELL_SIZE)
                        pg.draw.rect(self.screen,self.grass_color,grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pg.Rect(col * CELL_SIZE,row * CELL_SIZE,CELL_SIZE,CELL_SIZE)
                        pg.draw.rect(self.screen,self.grass_color,grass_rect)

    def update(self):
        self.snake.move_snake()

        self.delta_time = self.clock.tick(FPS)
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            if event.type == SCREEN_UPDATE:
                self.update()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    if self.snake.direction.y !=1:
                        self.snake.direction = Vector2(0,-1)
                if event.key == pg.K_DOWN: 
                    if self.snake.direction.y != -1:
                        self.snake.direction = Vector2(0,1)
                if event.key == pg.K_LEFT: 
                    if self.snake.direction.x !=1:
                        self.snake.direction = Vector2(-1,0)
                if event.key == pg.K_RIGHT: 
                    if self.snake.direction.x != -1:
                        self.snake.direction = Vector2(1,0)

    def run(self):
        while self.is_running:
            self.handle_events()
            self.render()
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    core = Core()
    SCREEN_UPDATE = pg.USEREVENT
    pg.time.set_timer(SCREEN_UPDATE,150)
    core.run()
