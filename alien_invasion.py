import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group



def run_game():
    #Inicializa o jogo e cria um objeto tela


    sets = Settings()
    pygame.init()
    screen = pygame.display.set_mode((sets.screen_width, sets.screen_height))
    pygame.display.set_caption(sets.screen_title)


    #Cria uma nave
    ship = Ship(screen, sets)


    #Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()



    #Inicia o laço principal do jogo
    while True:
        gf.update_screen(sets, screen, ship, bullets)
        gf.check_events(sets, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)


run_game()