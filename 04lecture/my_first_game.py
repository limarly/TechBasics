import pygame as pg

# initialise pygame
pg.init()

colour = 0, 0, 0
size = width, height = 1000, 1000
speed = [3, 4]

# create the display screen
# pass in the width and height
screen = pg.display.set_mode(size)

# set a caption
pg.display.set_caption("My First Game")

# load the image
ball = pg.image.load("image/ball.png")

ball_size = (100, 100)

resized_ball = pg.transform.scale(ball, ball_size)

ballrect = ball.get_rect()
# print(ballrect) # just for refernce

# overlay some music
#pg.mixer.music.load("music/test.mp3")
#pg.mixer.music.play(-1)


while True:
    for event in pg.event.get():
        # to close the window
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # move the ball
    ballrect = ballrect.move(speed)
    # print(ballrect) # just for reference

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(colour)
    # place the image
    screen.blit(resized_ball, ballrect)

    pg.display.flip()
