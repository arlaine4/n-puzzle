import utils
import sys
from Astar import Astar

class   Puzzle():
    def __init__(self):
        self.dico = {}
        self.visu = False

    def main(self, options, h_type):
        self.set_dico()
        self.set_visu(options.visual)
        if self.dico["solvable"] == "True":
            Astar(self.get_dico(), h_type, self.get_visu())
        elif self.dico["solvable"] == "False":
            print("This puzzle is not solvable, stopping now.")
            sys.exit()
        print("Dico infos : ",self.get_dico())

#-------------------------------------------------
# Getteurs et setteurs

    def set_dico(self):
        self.dico = utils.set_dico_infos()

    def set_visu(self, visu):
        self.visu = visu

    def get_dico(self):
        return self.dico

    def get_visu(self):
        return self.visu
#-------------------------------------------------

if __name__ == "__main__":
    options = utils.get_args_argparse()
    h_type = utils.get_heuristic_type(options)
    print(h_type)
    if h_type is None:
        print("Please enter only one heuristic type.")
        sys.exit()
    puzzle = Puzzle()
    puzzle.main(options, h_type)
