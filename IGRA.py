import pygame
import random

pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('IGRA')

plat_width = 100
plat_height = 10

#plat_x = 0
plat_x = display_width // 2
plat_y = display_height // 3

ball_x = display_width // 2
ball_y = display_height // 2
ball_speed_x = 3
ball_speed_y = 3
#ball_speed_x = random.randrange(3, 5)
#ball_speed_y = random.randrange(3, 5)

clock = pygame.time.Clock()

## Запуск игры
def run_game():
    global plat_x

    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if plat_x >= 0:
                plat_x -= 10
        elif keys[pygame.K_RIGHT]:
            if plat_x <= 700:
                plat_x += 10

        if plat_x + plat_width + 8 >= ball_x >= plat_x \
                and plat_y + plat_height + 8 >= ball_y >= plat_y - 7:
            quit()

        display.fill((255, 255, 255))

        pygame.draw.rect(display, (0, 0, 0), (plat_x, plat_y, plat_width, plat_height))
        pygame.draw.circle(display, (0, 0, 0), (ball_x, ball_y), 10)
        ball_move()

        plat_move()
        pygame.display.update()
        clock.tick(60)

## Движение мячика
def ball_move():
    global ball_speed_x, ball_speed_y, ball_x, ball_y, plat_x
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_y <= 10 or ball_y >= 595:
        ball_speed_y = -ball_speed_y
    if ball_x <= 10 or ball_x >= 790:
        ball_speed_x = -ball_speed_x



## Движение платформы

def plat_move():
    global plat_x, ball_speed_x, ball_speed_y, ball_x, ball_y

    if abs(plat_y - ball_y) < 100 and plat_x-ball_x < 30:
        #print(plat_x - ball_x)
        if(ball_speed_x > 0 and ball_speed_y > 0):
            if (plat_x > 0 and plat_x < display_width):
                plat_x -= 4
        elif (ball_speed_x > 0 and ball_speed_y < 0):
            if (plat_x > 0 and plat_x < display_width):
                plat_x -=4
        elif (ball_speed_x < 0 and ball_speed_y < 0):
            if (plat_x > 0 and plat_x < display_width):
                if (plat_x-ball_x < 30):
                    plat_x -=4
                else:
                    plat_x +=4
        else:
            if (plat_x > 0 and plat_x < display_width):
                plat_x +=4



    ball_need_y = display_height // 3



    #plat_x += 1


run_game()
