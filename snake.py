from settings import *

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction =  Vector2(1,0)
        self.on_init()

    def on_init(self):
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
