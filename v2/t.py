from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(33, 33, 333, 333,
            outline="#fb0", fill="#fb0")
        canvas.create_rectangle(33, 363, 663, 663,
            outline="#f50", fill="#f50")
        canvas.create_rectangle(833, 833, 1133, 1133,
            outline="#05f", fill="#05f")
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("1200x1200+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
