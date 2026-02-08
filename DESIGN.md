# Cavern (Bubble Bobble Clone)


This project refactors the original PyGame Zero game to improve structure and maintainability while keeping gameplay equivalent. The refactor focuses on separating responsibilities (screens/state, input handling, and game simulation) and reducing hidden dependencies.

## Screens (State pattern)
The game uses an `App` object that owns the active screen.
- `App.change_screen(new_screen)` is the single way the program transitions between states.
- Each screen is a class with:
  - `update(input_state)`
  - `draw()`

Screens implemented:
- `MenuScreen`: displays the title/menu and starts the game on Space.
- `PlayScreen`: runs the main game simulation and handles pause.
- `GameOverScreen`: displays game over and returns to the menu on Space.

The global `update()` and `draw()` functions are thin delegates that call `app.update(...)` and `app.draw()`.

## Input snapshot + edge detection
Input is captured once per frame into an `InputState` object. This removes the need for the player (or other entities) to read `keyboard` directly.
- Level/held inputs: `left`, `right`, `fire_held`
- Edge/pressed-this-frame inputs: `jump_pressed`, `fire_pressed`, `pause_pressed`

An `InputBuilder` tracks previous key states to compute edge presses consistently. `Player.update(input_state)` consumes the snapshot.

## Pause
Pause is implemented in `PlayScreen` and toggled by `P`.
- When paused, the play screen does not call `Game.update()`, so movement/spawning/timers freeze.
- The game scene still draws, and a pause overlay is rendered on top.
- Pressing `P` again resumes cleanly.

## Collision / World injection (refactor detail)
Tile collision queries are handled through a `World` object (`is_solid(x, y)`) that is passed to moving entities.
- Movement/collision code calls `world.is_solid(...)` instead of reaching into `Game.grid` directly.
- When levels change, the world’s grid reference is updated so collisions match the new level layout.
