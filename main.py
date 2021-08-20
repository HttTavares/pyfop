import tkinter as tk
from game import Game

game = Game()

window_width = 1600
window_height = 1000
geometry_text = str(window_width) + 'x' + str(window_height)

game_window = tk.Tk()
game_window.geometry(geometry_text)
society_frame = tk.Frame(game_window)
society_frame.place( height = window_height/2, width = window_width/2)
society_frame.configure( bg = '#ffbdbd' )
capital_frame = tk.Frame(game_window)
capital_frame.place( x = window_width/2, y = 0, height = window_height/2, width = window_width )
capital_frame.configure( bg = '#bde6ff' )
knowledge_color = '#e7abff'
nature_color = '#6a9471'



# capital_frame = tk.Frame(game_window)



population_tab_button = tk.Button( society_frame, text = 'Population' )
population_tab_button.place( height = 30, width = 60, x = 0, y = 200 )
# test_button2 = tk.Button( capital_frame, text = 'Production' )
# test_button2.pack()

game_window.mainloop()
