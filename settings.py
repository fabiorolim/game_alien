class Settings():

    """Uma classe para armazenar das as configurações da Invasão Alienigena"""


    def __init__(self):
        """Inicializa configurações do jogo"""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_title = "Alien Invasion"
        self.white_color =  (255, 255, 255)
        self.bg_color = (230, 230 ,230)
        self.black_color = (0, 0, 0)


        # Velocidade de movimento da nave
        self.ship_speed_factor = 1.5


        #Configurações de projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_allowed = 3
