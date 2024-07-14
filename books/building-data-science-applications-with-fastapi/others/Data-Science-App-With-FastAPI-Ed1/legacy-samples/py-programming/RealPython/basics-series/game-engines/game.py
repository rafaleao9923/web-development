import pygame as pg
from random import randint
from pathlib import Path
from typing import Tuple

WIDTH, HEIGHT = 800, 600
coin_coutdown, coin_interval = 2500, 100
COINT_COUNT = 10


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        player_image = str(
            Path(__file__).parent / "assets" / "alien.png"
        )

        self.surf = pg.image.load(
            player_image).convert_alpha()  # convert to alpha
        self.rect = self.surf.get_rect()

    def update(self, pos: Tuple):
        self.rect.center = pos


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()

        coin_image = str(
            Path(__file__).parent / "assets" / "coin.png"
        )

        self.surf = pg.image.load(
            coin_image).convert_alpha()  # convert to alpha
        self.rect = self.surf.get_rect(
            center=(
                randint(10, WIDTH - 10),
                randint(10, HEIGHT - 10),
            )
        )

    # def update(self, pos: Tuple):
    #     self.rect.center = pos


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.mouse.set_visible(False)
clock = pg.time.Clock()
# ADD
