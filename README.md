# Cavern (Bubble Bobble Clone)

Refactor of a PyGame Zero arcade platformer to improve structure and maintainability while keeping gameplay equivalent.

## Requirements / setup

- Python 3.10+
- Package: `pgzero` (includes/depends on `pygame`)

Install (recommended in a virtual environment):

```bash
python -m pip install pgzero
```
## How to Run

### Option 1 — Run via terminal
From the project root (the folder containing `main.py`):

```bash
python main.py
```

### Option 2 — Run via Visual Studio Code
- Open the project folder in VS Code.
- Select the correct interpreter (your venv, if you created one).
- Run main.py using your Run/Debug configuration

## Testing
### No automated tests are included (Manual verification):

- From the menu, press Space to start.
- In play, press Space to fire an orb; hold Space to blow it further.
- Press P to pause (gameplay freezes and a pause overlay appears), press P again to resume.
- Lose all lives to reach Game Over, then press Space to return to menu.

## Architectural changes (summary)
Added an App object that owns the current screen and delegates update() / draw().

Implemented MenuScreen, PlayScreen, and GameOverScreen, with screen switching via a single method (app.change_screen(...)).

Centralized input into an InputState snapshot built once per frame (edge detection for jump/fire/pause).

Added Pause toggled by P: freezes simulation updates and draws a pause overlay