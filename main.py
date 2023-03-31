import pygame
import random

pygame.font.init()
WIDE = 800
HIGH = 480

window = pygame.display.set_mode([WIDE, HIGH])
pygame.display.set_caption('pingpog')
clock = pygame.time.Clock()
game = True


def lor():
    l_or_r = random.randint(0, 1)
    return l_or_r


ARIAL_FONT_36 = pygame.font.Font(pygame.font.match_font('arial'), 36)
score = 0
P_WIDE = 100
P_HIGH = 15
C_WIDE = 20
P_SPEED = 6
SPEED = 4
FIRST_COL = True
C_R = 10
C_X_SP = 0
C_Y_SP = SPEED
platform_rect = pygame.rect.Rect(WIDE // 2 - P_WIDE // 2, HIGH - P_HIGH * 2, P_WIDE, P_HIGH)
circle_rect = pygame.rect.Rect(WIDE // 2, HIGH // 2, C_R, C_WIDE)
game_over = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            platform_rect = pygame.rect.Rect(WIDE // 2 - P_WIDE // 2, HIGH - P_HIGH * 2, P_WIDE, P_HIGH)
            circle_rect = pygame.rect.Rect(WIDE // 2, HIGH // 2, C_R, C_WIDE)
            C_X_SP = 0
            C_Y_SP = SPEED
            FIRST_COL = True
            game_over = False
    window.fill('black')

    if not game_over:
        press = pygame.key.get_pressed()
        if press[pygame.K_a]:
            platform_rect.x -= P_SPEED
        if press[pygame.K_d]:
            platform_rect.x += P_SPEED

        if platform_rect.colliderect(circle_rect):
            score += 1
            if FIRST_COL:
                lore = lor()
                if lore == 1:
                    C_X_SP += SPEED

                else:
                    C_X_SP -= SPEED
                FIRST_COL = False
            C_Y_SP = -SPEED

        pygame.draw.rect(window, 'white', platform_rect)
    circle_rect.y += C_Y_SP
    circle_rect.x += C_X_SP

    if circle_rect.top <= 0:
        C_Y_SP = SPEED
    if circle_rect.left <= 0:
        C_X_SP = SPEED
    if circle_rect.right >= WIDE:
        C_X_SP = -SPEED
    if circle_rect.bottom >= HIGH:
        game_over = True
        C_Y_SP = -SPEED
    lore_surf = ARIAL_FONT_36.render(f'{score}', True, '#121910')
    if game_over:
        title_surf = ARIAL_FONT_36.render('Press [SPACE]', True, 'white')
        window.blit(title_surf, (WIDE // 2 - title_surf.get_width() // 2,
                                 HIGH // 2 - title_surf.get_height() // 2))
        score = 0
    else:
        window.blit(lore_surf, (WIDE // 2, HIGH * 0))


    pygame.draw.circle(window, 'yellow', circle_rect.center, C_R)
    clock.tick(60)
    pygame.display.update()
    
    
# привет
