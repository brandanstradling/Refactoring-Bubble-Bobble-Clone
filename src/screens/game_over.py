from src.screens.menu import MenuScreen
from src.ui import draw_status

class GameOverScreen:
    def __init__(self, app, screen, sounds, music, game):
        self.app = app
        self.screen = screen
        self.sounds = sounds
        self.music = music
        self.game = game

    def update(self, input_state):
        if input_state.fire_pressed:
            self.app.change_screen(MenuScreen(self.app, self.screen, self.sounds, self.music))

    def draw(self):
        self.game.draw(self.screen)
        draw_status(self.screen, self.game)
        self.screen.blit("over", (0, 0))
