import utils
import sys

if __name__ == "__main__":
    options = utils.get_args_argparse()
    h_type = utils.get_heuristic_type(options)
    print(h_type)
