import sys


import pygame


from bullet import Bullet


def check_events(sets, screen, ship ,bullets):
    """Observaenventos de teclado e de mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, ship, sets, screen, bullets)

        elif event.type == pygame.KEYUP:
            check_events_keyup(event, ship)


def check_events_keydown(event, ship, sets, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < sets.bullet_allowed:
            new_bullet = Bullet(sets, screen, ship)
            bullets.add(new_bullet)


def check_events_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    """Atualiza a posição dos projeteis e se livra dos projteris antigos"""
    #Atualiza a posição dos projeteis
    bullets.update()

    # Livar-se dos projeteis que desapareceram na tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))



def update_screen(sets, screen, ship, bullets):
    # Redesenha a tela em cada passagem pelo laço
    screen.fill(sets.white_color)
    ship.blitme()


    #Redesenha todos os projeteis atras da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()


    # Deixa a tela mais recente sivel
    pygame.display.flip()