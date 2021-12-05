class GameStats:
    '''track statictics for alien invasion'''

    def __init__(self, ai_game):
        '''initialize statistics '''
        self.settings = ai_game.settings
        self.reset_stats()
        # start alien invasion in an inactive state
        self.game_active = False
        # high score should never be reset
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.ships_left = self.settings.ship_limit

        self.score = 0