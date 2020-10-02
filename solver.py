import sys
import argparse
from build_dico import check_dico_infos, build_dictionnary_infos

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
    h_type = []
    if options.hamming:
        h_type.append("hamming")
    if options.manhattan:
        h_type.append("manhattan")
    if options.linear_conflict:
        h_type.append("linear_conflict")
    if len(h_type) > 1:
        print("Please choose only one heuristic function")
        exit(1)
    elif len(h_type) == 0:
        h_type.append("linear_conflict")
    print(h_type)
    puzzle = Puzzle()
    puzzle.main()
