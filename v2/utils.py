import argparse

def get_args_argparse():
    """Initialisation et ajout des arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--hamming', '-a', action='store_true', help='hamming distance heuristic')
    parser.add_argument('--manhattan', '-m', action='store_true', help='manhattan distance heuristic')
    parser.add_argument('--linear_conflict', '-l', action='store_true', help='linear conflict heuristic')
    parser.add_argument('-visual', '-v', action='store_true', help='trigger visualisation')
    options = parser.parse_args()
    return options

def get_heuristic_type(options):
    """Parsing types heuristiques en arguments"""
    h_type = []
    if options.hamming:
        h_type.append("hamming")
    if options.manhattan:
        h_type.append("manhattan")
    if options.linear_conflict:
        h_type.append("linear_conflict")
    if len(h_type) > 1:
        return None
    elif len(h_type) == 0:
        h_type.append("linear_conflict")
    return str(h_type)
