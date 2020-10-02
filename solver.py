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
        tosolve = np.array(([8, 4, 5], [3, 0 ,1], [7, 2, 6]))
        a_size = int(np.sqrt(tosolve.size))
        solution = np.zeros((a_size, a_size), dtype=int)
        i = 0
        j = 0
        n = 1
        a = 0
        b = 1
        cpy = a_size
        while n < tosolve.size:
            while i < cpy + a:
                solution[j][i] = n
                n += 1
                i += 1
            i -= 1
            j += 1
            while j < cpy + a:
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
            n += 1
        print(solution)
        hamming = np.zeros((a_size, a_size), dtype=int)
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
