class GameStats:
  """Track game stats"""

  def __init__(self, ai_game):
    """initilize stats"""
    self.settings = ai_game.settings
    self.reset_stats()

  def reset_stats(self):
    """Initilize stats that can change during the game"""
    self.ships_left = self.settings.ship_limit
