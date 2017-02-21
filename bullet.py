import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Uma classe que adminitra projeteis lançados pela spaçonave"""


    def __init__(self, sets, screen, ship):
        """Criar um objeto para o projetil na posição atual da espaçonave"""
        super().__init__()
        #super(Bullet, self).__init__()
        self.screen = screen


        #Cria m retangulo para o projetil em (0, 0) e em seguida define a
        #posição correta

        self.rect = pygame.Rect(0, 0, sets.bullet_width, sets.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


        #Armazena a posição do projetil com um valor decimal
        self.y = float(self.rect.y)


        self.color = sets.black_color
        self.speed_factor = sets.bullet_speed_factor


    def update(self):
        """Move o projetil para cima da tela"""
        #Atualiza a posição decimal do projétil
        self.y -= self.speed_factor
        #Atualiza a posição de rect
        self.rect.y = self.y


    def draw_bullet(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.screen, self.color,self.rect)