import tkinter as tk

class Visu(tk.Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self, size=3):
        self.master.title("Puzzle solver for size {}".format(size))
        self.pack()
        canvas = tk.Canvas(self, width=1000, height=1000)
        x_top = 20
        y_top = 20
        x_bottom = 220
        y_bottom = 220
        widgets = []
        for i in range(1, size * size + 1):
            canvas.create_rectangle(x_top, y_top, x_bottom, y_bottom, outline='#000000', fill='#FFFFFF')
            canvas.pack()
            print(x_top, y_top, x_bottom, y_bottom)
            if i % 3 == 0 and i != 0:
                y_top += 200
                x_top = 20
                x_bottom = 220
                y_bottom += 200
            else:
                x_top += 200
                x_bottom += 200

class Widget(tk.Frame):
    def __init__(self, nb_list):
        frames = []
        for i in range(len(nb_list)):
            frame = tk.Frame(height = 200, width=200)
            nb = nb_list[i]

            


def main():
    window = tk.Tk()
    window.geometry("640x640+200+200")
    window.configure()
    ex = Visu()
    window.mainloop()

if __name__ == "__main__":
    main()
