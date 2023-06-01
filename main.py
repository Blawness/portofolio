from contextlib import redirect_stderr
import os
from platform import win32_edition
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

#Game Data

FPS = 60
VEL = 5
BORDER = pygame.Rect(WIDTH//2 - 5,0,10, HEIGHT)
BULLET_VEL= 7
MAX_BULLETS = 3

SHIP1_HIT = pygame.USEREVENT + 1
SHIP2_HIT = pygame.USEREVENT + 2




#Importing Image
SHIP_WIDTH, SHIP_HEIGHT = 55, 40

SPACESHIP1_IMG = pygame.image.load(os.path.join('Assets','spaceship1.png'))
SPACESHIP1 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP1_IMG, (SHIP_WIDTH, SHIP_HEIGHT)), 270)

SPACESHIP2_IMG = pygame.image.load(os.path.join('Assets','spaceship2.png'))
SPACESHIP2 = pygame.transform.rotate(pygame.transform.scale(SPACESHIP2_IMG, (SHIP_WIDTH, SHIP_HEIGHT)),90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.jpg')), (WIDTH, HEIGHT))

#Drawing

def draw_window(ship1, ship2, ship1_bullets, ship2_bullets):
    
    WIN.blit(SPACE,)
    pygame.draw.rect(WIN,'BLACK', BORDER)
    WIN.blit(SPACESHIP1,(ship1.x,ship1.y))
    WIN.blit(SPACESHIP2,(ship2 .x,ship2.y))
    pygame.display.update()
    
    for bullet in ship1_bullets:
        pygame.draw.rect(WIN,'RED', bullet)
    
    for bullet in ship2_bullets:
        pygame.draw.rect(WIN,'GREEN', bullet)

    pygame.display.update()

#Game Function

def ship1_handle_movement(keys_pressed, ship1):
    if keys_pressed[pygame.K_a]and ship1.x - VEL > 0:# Left
        ship1.x -= VEL
    if keys_pressed[pygame.K_d]and ship1.x + VEL + ship1.width < BORDER.x:# Right
        ship1.x += VEL
    if keys_pressed[pygame.K_w]and ship1.y - VEL > 0 :# UP
        ship1.y -= VEL
    if keys_pressed[pygame.K_s]and ship1.y + VEL + ship1.height < HEIGHT -10 :# Down
        ship1.y += VEL

def ship2_handle_movement(keys_pressed, ship2):
    if keys_pressed[pygame.K_LEFT]and ship2.x - VEL > BORDER.x + BORDER.width:# Left
        ship2.x -= VEL
    if keys_pressed[pygame.K_RIGHT]and ship2.x + VEL + ship2.width < WIDTH:# Right
        ship2.x += VEL
    if keys_pressed[pygame.K_UP]and ship2.y - VEL > 0 :# UP
        ship2.y -= VEL
    if keys_pressed[pygame.K_DOWN]and ship2.y + VEL + ship2.height < HEIGHT -10 :# Down
        ship2.y += VEL

def handle_bullets(ship1_bullets, ship2_bullets, ship1, ship2):
    for bullet in ship1_bullets:
        bullet.x += BULLET_VEL
        if ship2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SHIP1_HIT))
            ship1_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            ship1_bullets.remove(bullet)
    
    for bullet in ship2_bullets:
        bullet.x -= BULLET_VEL
        if ship1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(SHIP2_HIT))
            ship2_bullets.remove(bullet)
        elif bullet.x < 0:
            ship2_bullets.remove(bullet)

#Game Loop
def main():
    ship1 = pygame.Rect(100, 300, SHIP_WIDTH, SHIP_HEIGHT)
    ship2 = pygame.Rect(700, 300, SHIP_WIDTH, SHIP_HEIGHT)

    ship1_bullets = []
    ship2_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(ship1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(ship1.x + ship1.width, ship1.y + ship1.height//2 -2, 10, 5)
                    ship1_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(ship2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(ship2.x, ship2.y + ship2.height//2 -2, 10, 5)
                    ship2_bullets.append(bullet)

        
        keys_pressed = pygame.key.get_pressed()
        ship1_handle_movement(keys_pressed, ship1)
        ship2_handle_movement(keys_pressed, ship2)

        handle_bullets(ship1_bullets, ship2_bullets, ship1, ship2)

        draw_window(ship1, ship2, ship1_bullets, ship2_bullets)

        

        

    pygame.quit()

if __name__ == "__main__":
    main()