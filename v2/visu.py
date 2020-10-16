import tkinter as tk
import time

def visu(dico, grid):
    window = tk.Tk()
    window.title("Puzzle solver size {}.".format(dico["size"]))
    window.geometry("900x600")
    window.resizable(height=False, width=False) #bloquer le resize de la window
    auto = False #true si on est en mode automatique, false pour coup par coup en pressant une touche
    speed = 1 #vitesse de rafraichissement de la window
    window.mainloop()

