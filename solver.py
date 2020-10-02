import sys

class   Puzzle():
    def __init__(self):
        self.open = []
        self.closed = []
        self.iter = 0
        self.dico = self.build_dictionnary_infos()

    def main(self):
        solve_puzzle_bool = self.check_dico_infos()
        print("solvable_puzzle : ", solve_puzzle_bool)
        print(self.dico)
        if solve_puzzle_bool is False:
            print("This puzzle is unsolvable.")
            sys.exit()

    def check_dico_infos(self):
        if self.dico["unsolvable"] == "True" or self.dico["solvable"] == "False":
            return False
        else:
            return True
    
    def build_dictionnary_infos(self):
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
                print(dico)
            except:
                print("Error with casting size and/or iteration to integer values, please enter a valid input.")
                sys.exit()
            dico["solvable"] = infos[1][1].replace('\n', '')
            dico["unsolvable"] = infos[2][1].replace('\n', '')
        except:
            print("Error in one of the parameters, please enter valid data for the puzzle.")
            sys.exit()
        return dico

if __name__ == "__main__":
    puzzle = Puzzle()
    puzzle.main()
