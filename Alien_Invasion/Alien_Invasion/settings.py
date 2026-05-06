class Settings:
    """A class to store all the settings for Alien Invasion"""


    def __init__(self):
        """Initilize the game  ststic settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1
        self.ship_limit = 1

        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15


        #Alien Settings
        self.alien_width = 80
        self.alien_height = 80
        self.alien_speed = 10.0
        self.fleet_drop_speed = 45.0
        #Fleet direction 1 is right, -1 is left
        self.fleet_direction = 1

        # How quick the game speeds up
        self.speedup_scale =1.1
        #how quick the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout a game"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        #Fleet direction 1 is right, -1 is left
        self.fleet_direction = 1

        #scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)



