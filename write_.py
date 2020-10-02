def write_puzzle(puzzle, size, solvable, unsolvable, iterations):
    fd = open("data/puzzle.csv", "w+")
    fd.write(str(size) + '\n')
    for i in range(len(puzzle)):
        if i % size == 0 and i != 0:
            fd.write(str(puzzle[i]) + '\n')
        elif i % size != 0:
            fd.write(str(puzzle[i]) + ' ')
    fd.write('\n')
    fd_infos = open("data/infos.txt", "w+")
    fd_infos.write("size={}\n".format(str(size)))
    fd_infos.write("solvable={}\n".format(solvable))
    fd_infos.write("unsolvable={}\n".format(unsolvable))
    fd_infos.write("iteration={}\n".format(iterations))
