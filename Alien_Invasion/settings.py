class Settings:
    """A class to store all the settings for Alien Invasion"""


    def __init__(self):
        """Initilize the game settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15


        #Alien Settings
        self.alien_width = 80
        self.alien_height = 80
        self.alien_speed = 1.0
        self.fleet_drop_speed = 45.0
        #Fleet direction 1 is right, -1 is left
        self.fleet_direction = 1
