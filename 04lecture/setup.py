import pygame as pg


# initialise pygame
pg.init()

# create the display screen
# pass in the width and height
screen = pg.display.set_mode((400, 500))

# set a caption
pg.display.set_caption("SETTING UP")

surface1 = pg.Surface((100, 50))
surface2 = pg.Surface((50, 50))
surface3 = pg.Surface((70, 30))

surface1.fill((126, 156, 137))  # colour in RGB
surface2.fill((102, 128, 111))
surface3.fill((166, 134, 148))

# while True is needed to launch the window
while True:
    for event in pg.event.get():
        # to close the window
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        screen.fill((227, 248, 235))  # RGB coordinates
        screen.blit(surface1, (20, 20))  # coordinates in screen
        screen.blit(surface2, (70, 70))
        screen.blit(surface3, (100, 30))

        # running thw game
        pg.display.update()
