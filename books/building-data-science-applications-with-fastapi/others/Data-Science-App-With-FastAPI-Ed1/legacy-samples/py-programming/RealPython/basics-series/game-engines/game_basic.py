import pygame as pg

pg.init()

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    # screen.fill((255, 255, 255))

    pg.display.flip()   # update the screen
    pg.draw.circle(screen, (255, 0, 0), (WIDTH//2, HEIGHT//2), 50)

    red_square = pg.Rect((50, 50), (100, 100))
    pg.draw.rect(screen, (200, 0, 0), red_square, 1)
    text_font = pg.font.SysFont("any_font", 60)

    text_surface = text_font.render("Hello Pygame", False, (200, 0, 0))
    screen.blit(text_surface, (50, HEIGHT - 50))

    pg.display.flip()   # update the screen

pg.quit()