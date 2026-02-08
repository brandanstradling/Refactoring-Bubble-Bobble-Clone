from src.game import Game
from src.ui import draw_status

class PlayScreen:
    def __init__(self, app, screen, sounds, music):
        self.app = app
        self.screen = screen
        self.sounds = sounds
        self.music = music
        self.game = Game(with_player=True, sounds=sounds)

    def update(self, input_state):
        self.game.update(input_state)
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            from src.screens.game_over import GameOverScreen
            self.app.change_screen(GameOverScreen(self.app, self.screen, self.sounds, self.music, self.game))

    def draw(self):
        self.game.draw(self.screen)
        draw_status(self.screen, self.game)
