import sys
import argparse
import numpy as np
import csv
import utils

class   Puzzle():
    def __init__(self):
        self.open = []
        self.closed = []
        self.grid = []
        self.iter = 0
        self.dico = None

    def check_heuristic_to_call(self, h_type):
        if h_type == "hamming":
            self.h_hamming()
        elif h_type == "manhattan":
            self.h_manhattan()
        elif h_type == "linear_conflict":
            self.h_linear_conflict()

    def main(self, h_type):
        self.set_dico()
        print("dico in main: ", self.get_dico())
        solve_puzzle_bool = utils.check_dico_infos(self.get_dico())
        if solve_puzzle_bool is False:
            print("This puzzle is unsolvable.")
            sys.exit()
        self.set_grid()
        utils.print_grid(self.get_grid())
        #self.check_heuristic_to_call(h_type)

#------------------------------------------------------------------------------
#                               Getteurs et setteurs

    def get_grid(self):
        return self.grid

    def get_dico(self):
        return self.dico

    def set_dico(self):
        self.dico = utils.build_dictionnary_infos()

    def set_grid(self):
        self.grid = utils.load_grid()

#
#------------------------------------------------------------------------------

if __name__ == "__main__":
    options = utils.get_args_argparse()
    h_type = utils.options_parsing(options)
    if h_type is None:
        print("Please enter only one heuristic function type at a time.")
        sys.exit()
    print(h_type)
    puzzle = Puzzle()
    puzzle.main(h_type)
