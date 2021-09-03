import tkinter as tk
from population_frame import PopulationFrame

class SocietyFrame:
    def __init__(self, game_window_object):
        self.color = '#ffbdbd'
        self.game_window_object = game_window_object

    def configure_frame(self):
        self.frame = tk.Frame(self.game_window_object.window)
        self.frame.place( height = self.get_gamewindow_geometry()['Height']/2,
            width = self.get_gamewindow_geometry()['Width']/10)
        self.frame.configure( bg = self.color )
        self.make_population_button()
        self.make_labor_button()

    def get_gamewindow_geometry(self):
        return {
            'Width': self.game_window_object.info['Width'],
            'Height': self.game_window_object.info['Height']
        }

    def make_population_button(self):
        self.population_button = tk.Button(self.frame,
            text = 'Production')
        self.population_button.place( height = 30,
            width = 90,
            x = 0,
            y = 200)

    def make_labor_button(self):
        self.labor_button = tk.Button(self.frame,
            text = 'Tools')
        self.labor_button.place( height = 30,
            width = 90,
            x = 0,
            y = 230)


# population_tab_button = tk.Button( society_frame, text = 'Population' )
# population_tab_button.place( height = 30, width = 90, x = 0, y = 200 )
# population_tab_button.configure( bg = society_color)
