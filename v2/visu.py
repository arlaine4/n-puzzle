import tkinter as tk
import time

def create_grid(c, event=None):
    print("bonsoir")
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, 333):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, 333):
        c.create_line([(0, i), (w, i)], tag='grid_line')
    c.bind('<Configure>', create_grid)

"""root = tk.Tk()

c = tk.Canvas(root, height=1000, width=1000, bg='white')
c.pack(fill=tk.BOTH, expand=True)
c.bind('<Configure>', create_grid)

root.mainloop()"""


def visu(dico, grid):
    window = tk.Tk()
    window.title("Puzzle solver size {}.".format(dico["size"]))
    window.resizable(height=False, width=False) #bloquer le resize de la window
    auto = False #true si on est en mode automatique, false pour coup par coup en pressant une touche
    speed = 1 #vitesse de rafraichissement de la window
    window.mainloop()

