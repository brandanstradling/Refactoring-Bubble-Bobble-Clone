from dataclasses import dataclass

@dataclass(frozen=True)
class InputState:
    left: bool
    right: bool
    jump_pressed: bool
    fire_pressed: bool
    fire_held: bool
    pause_pressed: bool

class InputBuilder:
    def __init__(self):
        self._prev_space = False
        self._prev_up = False
        self._prev_p = False

    def build(self, keyboard) -> InputState:
        space = keyboard.space
        up = keyboard.up
        p = keyboard.p

        state = InputState(
            left=keyboard.left,
            right=keyboard.right,
            jump_pressed=(up and not self._prev_up),
            fire_pressed=(space and not self._prev_space),
            fire_held=space,
            pause_pressed=(p and not self._prev_p),
        )

        self._prev_space, self._prev_up, self._prev_p = space, up, p
        return state
