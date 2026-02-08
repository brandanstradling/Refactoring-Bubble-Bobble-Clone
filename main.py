import pgzrun

from src.constants import WIDTH as _WIDTH, HEIGHT as _HEIGHT, TITLE as _TITLE
WIDTH = _WIDTH
HEIGHT = _HEIGHT
TITLE = _TITLE

from src.app import App
from src.input import InputBuilder
from src.screens.menu import MenuScreen

app = App()
inputs = InputBuilder()
_initialized = False

def _ensure_init():
    global _initialized
    if _initialized:
        return
    app.change_screen(MenuScreen(app, screen, sounds, music))
    _initialized = True

def update():
    _ensure_init()
    input_state = inputs.build(keyboard)
    app.update(input_state)

def draw():
    _ensure_init()
    app.draw()

pgzrun.go()
