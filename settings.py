class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 1300
        self.screen_height = 650
        self.bg_color = (255, 255, 255)

        # bullet settings
        self.bullet_speed = 6
        self.bullet_width = 6
        self.bullet_height = 25
        self.bullet_color = (30, 30, 30)

        # alien setting
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # ship setting
        self.ship_speed = 5
        self.ship_limit = 3
