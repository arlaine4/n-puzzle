from set_ideal_grid import *
import numpy as np
import re

def call_heuristic(dico, grid, h_type, ideal_grid): # Determine quelle fonction heuristic utilisee
    if "hamming" in h_type:
        return h_hamming(dico, grid, ideal_grid)
    elif "manhattan" in h_type:
        return h_manhattan()
    elif "linear_conflict" in h_type:
        return h_linear_conflict()

def h_manhattan():
    print("manhattan not done")
    return

def h_linear_conflict():
    print("linear conflict not done")
    return

def h_hamming(dico, grid, ideal_grid):
    size = dico["size"]
    hamming = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            if ideal_grid[i][j] != grid[i][j] and grid[i][j] != 0:
                hamming[i][j] = 1
    h_ham = sum(sum(hamming))
    #print("Hamming heuristic atm is : " + str(h_ham))
    return h_ham
