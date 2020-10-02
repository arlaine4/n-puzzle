import sys
import argparse
import numpy as np
from utils import check_dico_infos, build_dictionnary_infos, options_parsing

parser = argparse.ArgumentParser()
parser.add_argument("--hamming", "-a", action='store_true', help="hamming distance heuristic")
parser.add_argument("--manhattan", "-m", action='store_true',  help="manhattan distance heuristic")
parser.add_argument("--linear_conflict", "-l", action='store_true', help="linear conflict heuristic")
options = parser.parse_args()

class   Puzzle():
    def __init__(self):
        self.open = []
        self.closed = []
        self.iter = 0
        self.dico = build_dictionnary_infos()

    def h_hamming(self):
        solution = np.array(([1, 2, 3], [8, 0 ,4], [7, 6, 5]))
        tosolve = np.array(([8, 4, 5], [3, 0 ,1], [7, 2, 6]))
        hamming = np.array(([0, 0, 0], [0, 0 ,0], [0, 0, 0]))
        a_size = int(np.sqrt(tosolve.size))
        for i in range(a_size):
            for j in range(a_size):
                if solution[i][j] == tosolve[i][j] and tosolve[i][j] != 0:
                    hamming[i][j] = 1
        print(sum(sum(hamming)))

    def main(self):
        solve_puzzle_bool = check_dico_infos(self)
        print("solvable_puzzle : ", solve_puzzle_bool)
        print(self.dico)
        if solve_puzzle_bool is False:
            print("This puzzle is unsolvable.")
            sys.exit()


if __name__ == "__main__":
    h_type = options_parsing(options)
    if h_type is None:
        print("Please enter only one heuristic function type at a time.")
        sys.exit()
    print(h_type)
    puzzle = Puzzle()
    puzzle.main()
    puzzle.h_hamming()
