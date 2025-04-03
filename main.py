import pygame as pg
from scripts.player import Player

# pygame setup
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption(f'Harvest Utopia')
clock = pg.time.Clock()
running = True

while running:
    # check events
    # pg.QUIT event for exiting the game by clicking X to close window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Screen background fill
    screen.fill("green")

    # flip() the display to update it
    pg.display.flip()

    clock.tick(60) # limit fps to 60

pg.quit()