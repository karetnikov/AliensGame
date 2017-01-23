class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stars()
    def reset_stars(self):
        self.ships_left = self.ai_settings.ship_limit