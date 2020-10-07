import sys
import argparse
import numpy as np
import csv
import utils
import heuristics as h
import Astar as star
from set_ideal_grid import set_ideal_grid

class   Node():
    def __init__(self):
        self.nb = 0
        self.pos = {"x" : 0, "y" : 0}
        self.g_c = 0.0 # g(x) : sum of g(x) of the parent node and the cost to travel to that node from it’s parent.
        self.h_c = 0.0 # heuristic cost of the node
        self.f_c = 0.0 # Final cost of the node     --> f_c = h_c + g_c ( h_c = h(x) / g_c = g(x) / f_c = f(x) )

class   Puzzle():
    def __init__(self):
        self.ideal_grid = []
        self.open = [] #instances de class Node
        self.closed = [] #instances de class Node
        self.next_node = None # instances de class Node aussi ?
        self.grid = []
        self.dico = None

    def check_heuristic_to_call(self, h_type):
        if "hamming" in h_type:
            h.h_hamming(self.get_dico(), self.get_grid())
        elif h_type == "manhattan":
            h.h_manhattan()
        elif h_type == "linear_conflict":
            h.h_linear_conflict()

    def main(self, h_type):
        self.set_dico()
        self.set_grid()
        solve_puzzle_bool = utils.check_dico_infos(self.get_dico())
        if solve_puzzle_bool is False:
            utils.print_grid("error", self.get_grid())
            print("This puzzle is \033[31;3munsolvable.\033[0m")
            sys.exit()
        self.set_ideal_grid()
        #print(self.get_ideal_grid())
        #utils.print_grid("debug", self.get_grid(), h_type, self.get_dico(), self.get_ideal_grid())
        self.check_heuristic_to_call(h_type)
        star.Astar(self.get_dico(), self.get_grid(), self.get_closed(), h_type)

#------------------------------------------------------------------------------
#                               Getteurs et setteurs

    def get_grid(self):
        return self.grid

    def get_dico(self):
        return self.dico

    def get_ideal_grid(self):
        return self.ideal_grid

    def get_open(self):
        return self.open

    def get_closed(self):
        return self.closed

    def get_next_node(self):
        return self.next_node

    def set_ideal_grid(self):
        self.ideal_grid = set_ideal_grid(self.get_dico())

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
    puzzle = Puzzle()
    puzzle.main(h_type)
