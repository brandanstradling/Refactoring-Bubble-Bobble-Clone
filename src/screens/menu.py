from src.game import Game, Player

class MenuScreen:
    def __init__(self, app, screen, sounds, music):
        self.app = app
        self.screen = screen
        self.sounds = sounds
        self.music = music
        self.game = Game(with_player=False, sounds=sounds)

    def update(self, input_state):
        self.game.update(None)
        if input_state.fire_pressed:
            from src.screens.play import PlayScreen
            self.app.change_screen(PlayScreen(self.app, self.screen, self.sounds, self.music))

    def draw(self):
        self.game.draw(self.screen)
        self.screen.blit("title", (0, 0))
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        self.screen.blit("space" + str(anim_frame), (130, 280))
