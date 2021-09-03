import tkinter as tk

class CapitalFrame:
    def __init__(self, game_window_object):
        self.color = '#bde6ff'
        self.game_window_object = game_window_object
        # self.make_production_button()

    def configure_frame(self):
        self.frame = tk.Frame(self.game_window_object.window)
        self.frame.place(
            x = 9*self.get_gamewindow_geometry()['Width']/10,
            y = 0,
            height = self.get_gamewindow_geometry()['Height']/2,
            width = self.get_gamewindow_geometry()['Width']/10 )
        self.frame.configure( bg = self.color )
        print(self.get_gamewindow_geometry()['Height'])
        self.make_production_button()
        self.make_tools_button()

    def get_gamewindow_geometry(self):
        return {
            'Width': self.game_window_object.info['Width'],
            'Height': self.game_window_object.info['Height']
        }

    def make_production_button(self):
        self.production_button = tk.Button(self.frame,
            text = 'Production')
        self.production_button.place( height = 30,
            width = 90,
            x = 0,
            y = 200)

    def make_tools_button(self):
        self.tools_button = tk.Button(self.frame,
            text = 'Tools')
        self.tools_button.place( height = 30,
            width = 90,
            x = 0,
            y = 230)


    # population_tab_button = tk.Button( society_frame, text = 'Population' )
    # population_tab_button.place( height = 30, width = 90, x = 0, y = 200 )
    # population_tab_button.configure( bg = society_color)
