import pygame
import random
import math

# Initialising pygame and setting the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
bg_img = pygame.image.load("background.png")

# Setting the window details
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#  Font
font = pygame.font.Font('freesansbold.ttf', 32)


#  Player rendering and details
player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
player_change_x = 0


def player(x, y):
    screen.blit(player_img, (x, y))


# Enemy rendering and details
enemy_img = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 750)
enemy_y = random.randint(50, 100)
enemy_change_x = 3
enemy_change_y = 10


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Bullet rendering and details
bullet_img = pygame.image.load("bullet.png")
bullet_x = 370
bullet_y = 480
bullet_change_y = 10
bullet_state = "rest"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bullet_img, (x+16, y+10))


def hasCollided(enemy_x, enemy_y, bullet_y, bullet_x):
    distance = math.sqrt(((enemy_x - bullet_x) ** 2) +
                         ((enemy_y-bullet_y) ** 2))
    if distance < 25:
        return True
    return False


# Global variables
running = True
score = 0


# Game Loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg_img, (0, 0))
    score_board = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_board, (0, 0))

    for event in pygame.event.get():

        # Exit status
        if event.type == pygame.QUIT:
            running = False

        # Checking for keystrokes
        if event.type == pygame.KEYDOWN:
            # print("Key is pressed")
            if event.key == pygame.K_LEFT:
                # print("Left key is pressed")
                player_change_x = -4
            if event.key == pygame.K_RIGHT:
                # print("Right key is pressed")
                player_change_x = 4

            if event.key == pygame.K_SPACE:
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_change_x = 0

            # Altering the values with keystrokes
    player_x += player_change_x

    # Adding the boundaries to the window
    if player_x <= 0:
        player_x = 0
    if player_x >= 736:
        player_x = 736

    # Adding enemy movement

    enemy_x += enemy_change_x
    if enemy_x <= 0:
        enemy_change_x = 3
        enemy_y += enemy_change_y
    if enemy_x >= 736:
        enemy_change_x = -3
        enemy_y += enemy_change_y

    # Bullet movement
    if bullet_state is "fired":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_change_y

    if bullet_y < 0:
        bullet_y = 480
        bullet_state = "rest"
        # print(bullet_x, bullet_y)

    # Bullet collision
    hit = hasCollided(enemy_x, enemy_y, bullet_y, bullet_x)
    if hit:
        score += 1
        bullet_y = 480
        bullet_state = "rest"
        enemy_x = random.randint(0, 750)
        enemy_y = random.randint(50, 100)
        print(score)

    if enemy_y > 155:
        game_end = font.render("Game Over", True, (255, 255, 255))
        screen.blit(game_end, (320, 250))
        enemy_change_x = 0
        enemy_change_y = 0

# Rendering Player,enemy and gate
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()
