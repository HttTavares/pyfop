import tkinter as tk
from Society.society_frame import SocietyFrame
from Capital.capital_frame import CapitalFrame

class GameWindow():
    def __init__(self, info):
        # window_width = 1600
        # window_height = 1000
        self._info = info
        self.geometry_text = str(info['Width']) + 'x' + str(info['Height'])
        self.window = tk.Tk()
        self.window.geometry(self.geometry_text)
        self.add_society_frame()
        self.add_capital_frame()

    @property
    def info(self):
        return self._info

    def add_society_frame(self):
        self.society_frame = SocietyFrame(self)
        self.society_frame.configure_frame()

    def add_capital_frame(self):
        self.capital_frame = CapitalFrame(self)
        self.capital_frame.configure_frame()
