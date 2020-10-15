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

def set_dico_infos():
    dico = {"size" : 0, "solvable" : None, "unsolvable" : None, "iteration" : 10000}
    fd = open("data/infos.txt", "r+")
    infos = []
    for elem in fd:
        infos.append(elem)
    for i in range(len(infos)):
        infos[i] = infos[i].split('=')
    try:
        try:
            dico["size"] = int(infos[0][1])
            dico["iteration"] = int(infos[3][1])
        except:
            print("Error with casting size or iteration to integer types, please enter a valid input.")
            sys.exit()
        dico["solvable"] = infos[1][1].replace('\n', '')
        dico["unsolvable"] = infos[2][1].replace('\n', '')
    except:
        print("Error in one of the parameters, please enter a valid input.")
        sys.exit()
    return dico

def load_grid(dico):
    grid = []
    file_name = 'data/puzzle-{}-1.txt'.format(str(dico["size"]))
    fd = open(file_name, 'r+')
    i = 0
    for row in fd:
        if i == 0:
            i += 1
        else:
            grid.append(row.replace('\n', ''))
    print(grid)
    return grid


