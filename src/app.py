class App:
    def __init__(self):
        self.screen_obj = None

    def change_screen(self, screen_obj):
        self.screen_obj = screen_obj

    def update(self, input_state):
        self.screen_obj.update(input_state)

    def draw(self):
        self.screen_obj.draw()
