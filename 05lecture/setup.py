import pygame
import pygame as pg

# initialise pygame
pg.init()

# create variables to change colour and size
colour = 192, 192, 192  # this is rgb code - you can adjust this
size = width, height = 500, 400
font = pygame.font.SysFont(None, 24)
img = font.render('Hello Word', True, (0, 225, 0), (0, 0, 128))

# create the display
screen = pg.display.set_mode(size)

while True:
    for event in pg.event.get():
        # close the game if the user clicks exit
        if event.type == pg.QUIT:
            pg.quit()
            quit()


        # this part wil ru the "game"
        screen.fill(colour)  # changes the background
        screen.blit(img, (20, 20))


        pg.display.update()
