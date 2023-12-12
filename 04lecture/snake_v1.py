import pygame as pg

# initialise pygame
pg.init()

background_colour = 0, 0, 0
size = dis_width, dis_height = 800, 800
snake_colour = 69, 168, 95
x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0
y1_change = 0

# create the display screen
# pass in the width and height
screen = pg.display.set_mode(size)

# set a caption
pg.display.set_caption("SNAKE")

surface1 = pg.Surface((100, 50))
surface1.fill((126, 156, 137))

#control the speed
clock = pg.time.Clock()

# overlay some music
pg.mixer.music.load("sounds/snake_music.mp3")
pg.mixer.music.play(-1)

while True:
    for event in pg.event.get():
        # to close the window
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pg.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pg.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pg.K_DOWN:
                x1_change = 0
                y1_change = 10

    # what happens if you reach the border
    if x1 < 0 or y1 < 0 or x1 >= dis_width or y1 >= dis_height:
        pg.quit()
        quit()

    x1 += x1_change
    y1 += y1_change

    # running the game
    screen.fill(background_colour)

    # draw your snake
    pg.draw.rect(screen, snake_colour, [x1, y1, 30, 30], 2)  # 2 makes it no fill

    clock.tick(30)

    pg.display.update()
