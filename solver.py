import sys
import argparse
from build_dico import check_dico_infos, build_dictionnary_infos

parser = argparse.ArgumentParser()
parser.add_argument("h-hamming", "-hh", type=str, help="hamming distance heuristic")
parser.add_argument("h-manhattan", "-hm", type-str, help="manhattan distance heuristic")
parser.add_argument("h-linear_conflict", "-hl", type=str, help="linear conflict heuristic")
options = parser.parse_args()

class   Puzzle():
    def __init__(self):
        self.open = []
        self.closed = []
        self.iter = 0
        self.dico = build_dictionnary_infos()

    def main(self):
        solve_puzzle_bool = check_dico_infos(self)
        print("solvable_puzzle : ", solve_puzzle_bool)
        print(self.dico)
        if solve_puzzle_bool is False:
            print("This puzzle is unsolvable.")
            sys.exit()

if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.main()
