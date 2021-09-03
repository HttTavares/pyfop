from game_window import GameWindow
from Society.society_frame import SocietyFrame

class Game():
    def __init__(self, info):
        self._info = info

    @property
    def info(self):
        return self._info
    @property
    def window(self):
        return self._window.window

    def init_window(self):
        self._window = GameWindow({
            'Width': 1600,
            'Height': 1000
            # 'Society Frame': SocietyFrame(self)
        })

    def add_society_frame(self):
        self.info['Society Frame'] = SocietyFrame()

    def start(self):
        self.init_tk()

    def init_tk(self):
        self.init_window()
        self.window.mainloop()

if __name__ == '__main__':
    game = Game({})
    game.start()
    print(game.info)
    game.info['seila'] = 2
    print(game.info)
    # print()
