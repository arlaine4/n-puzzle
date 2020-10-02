import sys
import argparse
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
