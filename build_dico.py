import sys

def check_dico_infos(instance_puzzle):
    if instance_puzzle.dico["unsolvable"] == "True" or instance_puzzle.dico["solvable"] == "False":
        return False
    else:
        return True

def build_dictionnary_infos():
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
