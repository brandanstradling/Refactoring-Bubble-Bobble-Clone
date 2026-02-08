import pygame

from src.constants import WIDTH, HEIGHT
from src.game import Game
from src.ui import draw_status, draw_text

class PlayScreen:
    def __init__(self, app, screen, sounds, music):
        self.app = app
        self.screen = screen
        self.sounds = sounds
        self.music = music
        self.game = Game(with_player=True, sounds=sounds)
        self.paused = False

    def update(self, input_state):
        if input_state.pause_pressed:
            self.paused = not self.paused

            try:    
                if self.paused:
                    self.music.pause()
                else:
                    self.music.unpause()

            except Exception:
                if self.paused:
                    self.music.stop()
                else:
                    self.music.play("theme")
            return
        
        if self.paused:
            return
        
        self.game.update(input_state)
        if self.game.player.lives < 0:
            self.game.play_sound("over")
            from src.screens.game_over import GameOverScreen
            self.app.change_screen(GameOverScreen(self.app, self.screen, self.sounds, self.music, self.game))

    def draw(self):
        self.game.draw(self.screen)
        draw_status(self.screen, self.game)

        if self.paused:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 140))
            self.screen.surface.blit(overlay, (0, 0))

            draw_text(self.screen, "PAUSED", 200) 
