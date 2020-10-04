import pandas as pd
import numpy as np

def write_puzzle(puzzle, size, solvable, unsolvable, iterations):
    fd = open("data/puzzle.csv", "w+")
    fd.write(str(size) + '\n')

    lst = puzzle
    array = np.array(lst)
    array = np.reshape(array, (-1, size))
    fd.write(str(array) + '\n')

    fd_infos = open("data/infos.txt", "w+")
    fd_infos.write("size={}\n".format(str(size)))
    fd_infos.write("solvable={}\n".format(solvable))
    fd_infos.write("unsolvable={}\n".format(unsolvable))
    fd_infos.write("iteration={}\n".format(iterations))
