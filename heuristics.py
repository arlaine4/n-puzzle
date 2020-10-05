import utils
import numpy as np
import re

def static_additive_patern_database(npgrid):
    patern_grid = [[], [], []]
    return pater_grid

def h_manhattan():
    print("manhattan not done")
    return

def h_linear_conflict():
    print("linear conflict not done")
    return

def h_hamming(dico, grid):
    size = dico["size"]
    # CONVERTION DE LA LIST grid EN NUMPY ARRAY npgrid
    npgrid = np.zeros((size, size), dtype=int)
    test = str(grid).split()
    tmp = []
    l = 0
    n = 0
    for i in test:
        tmp = re.sub('[^0-9]', '', i)
        if l == size and n < size:
            l = 0
            n += 1
        npgrid[n][l] = int(tmp)
        l += 1
    # FIN
    solved = utils.set_ideal_grid(dico, grid)
    hamming = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if solved[i][j] != npgrid[i][j] and npgrid[i][j] != 0:
                hamming[i][j] = 1
    # DEBUG
    print("HAMMING COMP")
    print(solved)
    print(npgrid)
    # FIN DEBUG
    h_ham = sum(sum(hamming))
    print("Hamming heuristic atm is : " + str(h_ham))
    return h_ham
