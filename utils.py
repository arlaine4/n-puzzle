import sys
import csv
import argparse
import numpy as np

def get_args_argparse():
    """Initialisation et ajout des arguments, ils sont utilisees dans solver.py"""

    parser = argparse.ArgumentParser()
    parser.add_argument('--hamming', '-a', action='store_true', help='hamming distamce heuristic')
    parser.add_argument('--manhattan', '-m', action='store_true', help='manhattan distance heuristic')
    parser.add_argument('--linear_conflict', '-l', action='store_true', help='linear conflict heuristic')
    parser.add_argument('-visual', '-v', action='store_true', help='trigger visualition')
    options = parser.parse_args()
    return options

def check_dico_infos(dico):
    """Fonction de check si on solve le puzzle ou pas"""

    if dico["unsolvable"] == "True" or dico["solvable"] == "False":
        return False
    else:
        return True

def load_grid():
    """Chargement du puzzle dans une var grid depuis le csv
    C'est la grid qui sera utilisee dans tout le programme"""

    grid = []
    i = 0
    with open('data/puzzle.csv', 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            i += 1      # le i sert juste a skip la premiere row ou il y a la size du puzzle
            if i > 1:
                grid.append(row)
    return grid

def set_iter(dico):
    return int(dico["iteration"])

def print_grid(mode="debug", grid=None, h_type=None, dico=None, ideal_grid=None):
    if mode == "debug":
        print("Selected Heuristic : \033[31;3m{}\033[0m\nInfos on grid : \033[32;3m{}\033[0m".format(h_type, dico))
    print("\033[35;3mInput grid:\033[0m")
    for row in grid:
        print(row)
    print("\033[35;3mIdeal grid:\033[0m")
    print(ideal_grid)

def build_dictionnary_infos():
    """Recuperation et stockage des infos concernant le puzzle
    dans infos.txt dans un dico"""

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
            print("Error with casting size and/or iteration to integer values, please enter a valid input.")
            sys.exit()
        dico["solvable"] = infos[1][1].replace('\n', '')
        dico["unsolvable"] = infos[2][1].replace('\n', '')
    except:
        print("Error in one of the parameters, please enter valid data for the puzzle.")
        sys.exit()
    return dico

def options_parsing(options):
    """Fonction qui handle les conflits sur le type d'heuristique passee
    en argument, par defaut ou en cas de conflit on utilise linear_conflict"""

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
