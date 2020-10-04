import pandas as pd
import numpy as np

def write_puzzle(puzzle, size, solvable, unsolvable, iterations):
    """Ecriture de la grid dans data/puzzle.csv"""

#--------------------------------------------------------------------
#                   Partie ecriture de la grid

    fd = open("data/puzzle.csv", "w+")
    fd.write(str(size) + '\n')

    lst = puzzle
    array = np.array(lst)
    array = np.reshape(array, (-1, size))
    for elem in array:
        for i in range(len(elem)):
            if i < len(elem) - 1:
                fd.write(str(elem[i]) + ' ')
            else:
                fd.write(str(elem[i]))
        fd.write('\n')

#
#--------------------------------------------------------------------

#--------------------------------------------------------------------
#               Partie ecriture des infos sur la grid

    fd_infos = open("data/infos.txt", "w+")
    fd_infos.write("size={}\n".format(str(size)))
    fd_infos.write("solvable={}\n".format(solvable))
    fd_infos.write("unsolvable={}\n".format(unsolvable))
    fd_infos.write("iteration={}\n".format(iterations))

#
#--------------------------------------------------------------------
