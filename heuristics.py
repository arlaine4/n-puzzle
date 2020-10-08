from set_ideal_grid import *
import numpy as np
import re

def static_additive_patern_database(npgrid):
    patern_grid = [[], [], []]
    return pater_grid


def call_heuristic(dico, grid, h_type, ideal_grid): # Determine quelle fonction heuristic utilisee
    if "hamming" in h_type:
        return h_hamming(dico, grid, ideal_grid)
    elif "manhattan" in h_type:
        h_manhattan()
    elif "linear_conflict" in h_type:
        h_linear_conflict()

def h_manhattan():
    print("manhattan not done")
    return

def h_linear_conflict():
    print("linear conflict not done")
    return

def h_hamming(dico, grid, ideal_grid):
    size = dico["size"]
    # CONVERTION DE LA LIST grid EN NUMPY ARRAY npgrid
    npgrid = np.zeros((size, size), dtype=int)
    test = str(grid).split()
    l = 0
    n = 0
    for i in test:
        tmp = re.sub('[^0-9]', '', i)
        if l == size and n < size:
            l = 0
            n += 1
        if tmp.isdigit():
            npgrid[n][l] = int(tmp)
            l += 1
    # FIN
    hamming = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if ideal_grid[i][j] != npgrid[i][j] and npgrid[i][j] != 0:
                hamming[i][j] = 1
    # DEBUG
    # print("HAMMING COMP")
    # print(ideal_grid)
    # print(npgrid)
    # FIN DEBUG
    h_ham = sum(sum(hamming))
    print("Hamming heuristic atm is : " + str(h_ham))
    return h_ham
