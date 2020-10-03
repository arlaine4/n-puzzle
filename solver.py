import sys
import argparse
import numpy as np
import csv
import utils

parser = argparse.ArgumentParser()
parser.add_argument("--hamming", "-a", action='store_true', help="hamming distance heuristic")
parser.add_argument("--manhattan", "-m", action='store_true',  help="manhattan distance heuristic")
parser.add_argument("--linear_conflict", "-l", action='store_true', help="linear conflict heuristic")
options = parser.parse_args()

class   Puzzle():
    def __init__(self):
        self.open = []
        self.closed = []
        self.grid = []
        self.iter = 0
        self.dico = self.set_dico()

    def check_heuristic_to_call(self, h_type):
        if h_type == "hamming":
            self.h_hamming()
        elif h_type == "manhattan":
            self.h_manhattan()
        elif h_type == "linear_conflict":
            self.h_linear_conflict()

    def main(self, h_type):
        solve_puzzle_bool = utils.check_dico_infos(self.get_dico())
        print(self.dico)
        if solve_puzzle_bool is False:
            print("This puzzle is unsolvable.")
            sys.exit()
        self.grid = self.set_grid()
        utils.print_grid(self.get_grid())
        #self.check_heuristic_to_call(h_type)

#------------------------------------------------------------------------------
# Getteurs et setteurs

    def get_grid(self):
        return self.grid

    def get_dico(self):
        return self.dico

    def set_dico(self):
        return utils.build_dictionnary_infos()

    def set_grid(self):
        return utils.load_grid()

#------------------------------------------------------------------------------

    def h_manhattan(self):
        print("manhattan not done")
        return

    def h_linear_conflict(self):
        print("linear conflict not done")
        return

    def h_hamming(self):
        print("hamming not done")
        return
        """tosolve = np.array(([8, 4, 5, 10], [11, 13, 12, 16], [3, 0 , 1, 14], [7, 2, 6, 15]))
        a_size = int(np.sqrt(tosolve.size))
        solution = np.zeros((a_size, a_size), dtype=int)
        i = 0
        j = 0
        n = 1
        a = 0
        b = 1
        cpy = a_size
        while n < tosolve.size:
            while i < cpy - a:
                solution[j][i] = n
                n += 1
                i += 1
            i -= 1
            j += 1
            while j < cpy - a:
                solution[j][i] = n
                n += 1
                j += 1
            j -= 1
            while i >= 0 + a:
                solution[j][i] = n
                n += 1
                i -= 1
            i += 1
            j -= 1
            a += 1
            while j >= 0 + a:
                solution[j][i] = n
                n += 1
                j -= 1
            a += 1
            n += 1
        print(solution)
        hamming = np.zeros((a_size, a_size), dtype=int)
        for i in range(a_size):
            for j in range(a_size):
                if solution[i][j] == tosolve[i][j] and tosolve[i][j] != 0:
                    hamming[i][j] = 1
        print(sum(sum(hamming)))"""

if __name__ == "__main__":
    h_type = utils.options_parsing(options)
    if h_type is None:
        print("Please enter only one heuristic function type at a time.")
        sys.exit()
    print(h_type)
    puzzle = Puzzle()
    puzzle.main(h_type)
