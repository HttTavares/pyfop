import tkinter as tk
from game import Game
from Society.society_frame import SocietyFrame

game = Game({

})

# society_color = '#ffbdbd'
# capital_color = '#bde6ff'
# knowledge_color = '#e7abff'
# nature_color = '#6a9471'
# knowledge_frame = tk.Frame(game_window)
# knowledge_frame.place( y = window_height/2, height = window_height/2, width = window_width/10)
# knowledge_frame.configure( bg = knowledge_color )
# nature_frame = tk.Frame(game_window)
# nature_frame.place( x = 9*window_width/10, y = window_height/2, height = window_height/2, width = window_width/10)
# nature_frame.configure( bg = nature_color )

game.start()
