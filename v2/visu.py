import curses
import time
import Astar as a
import queue as q
import utils
import algorithm as algo

def init_visu():
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.keypad(True)
    curses.cbreak()
    curses.curs_set(0)
    return stdscr

def destroy_visu(stdscr, mode="end"):
    if mode == "end":
        stdscr.refresh()
        time.sleep(5)
        stdscr.clear()
    stdscr.keypad(False)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

def stop_menu(key, stdscr):
    stdscr.addstr(30, 30, "bonsoir")
    stdscr.refresh()
    stdscr.clear()
    stdscr.refresh()
    if key == 258:
        stdscr.addstr(10, 10, "You selected Manual mode, starting now.")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Manual mode, starting now..")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Manual mode, starting now...")
        stdscr.refresh()
        time.sleep(1.4)
    elif key == 259 or key == None:
        stdscr.addstr(10, 10, "You selected Auto mode, starting now.")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Auto mode, starting now..")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Auto mode, starting now...")
        stdscr.refresh()
        time.sleep(1.4)
    stdscr.clear()
    stdscr.refresh()


def menu_visu(stdscr):
    mode = 0
    key = None
    x = 15
    y = 12
    last_move = None
    while 1:
        stdscr.addstr(10, 10, "Select a mode for visual:")
        if key == 259 or key is None:
            stdscr.addstr(12, 15, "->   Auto mode.")
            stdscr.addstr(14, 15, "     Manual mode.")
            last_move = key
        elif key == 258:
            stdscr.addstr(12, 15, "     Auto mode.")
            stdscr.addstr(14, 15, "->   Manual mode.")
            last_mode = key
        stdscr.refresh()
        while 1:
            key = stdscr.getch()
            #stdscr.addstr(20, 20, str(key))
            stdscr.refresh()
            if key ==  259 or key == 258 or key == 111: #change this with y position and give it to stop menu
                break
        if key == 111:
            #print(last_move)
            #time.sleep(2)
            #stop_menu(last_move, stdscr)
            break
    return last_move

def print_grid(stdscr, grid, dico, ite):
    stdscr.clear()
    stdscr.refresh()
    x = 10
    y = 10
    size = dico["size"]
    for i in range(size):
        for j in range(size):
            if j < size - 1:
                stdscr.addstr(y, x, "|----")
            else:
                stdscr.addstr(y, x, "|----|")
            x += 5
        x = 10
        y += 1
        for j in range(size):
            if j < size - 1:
                stdscr.addstr(y, x, "|    ")
            else:
                stdscr.addstr(y, x, "|    |")
            x += 5
        x = 10
        y += 1
        if i == size - 1:
            for k in range(size):
                stdscr.addstr(y, x, "|----|")
                x += 5
    #place_numbers_in_position(stdscr, grid, dico)
    stdscr.refresh()

def place_numbers_in_position(stdscr, grid, dico):
    positions = []
    #position une liste de tuple avec x, y pour chaque elem de la grid
    #append dans positions les coord de chaque elem de la grid
    #en faisant des ope sur size et ajustement avec les positions de depart

def shortest_way_visu(grid, ideal_grid, dico, h_type):
    stdscr = init_visu()
    mode = menu_visu(stdscr)
    stdscr.clear()
    stdscr.refresh()
    time.sleep(2)
    if mode == 258:
        mode = "manual"
    else:
        mode = "auto"
    queue = q.PriorityQueue()
    closed = set()
    queue.put((0, grid, grid, 0))
    iteration = 0
    switchs = 0
    print_grid(stdscr, grid, dico, switchs)
    while iteration < dico["iteration"]:
        g_c, grid, parent, cost = queue.get()
        if grid == ideal_grid:
            break
        closed.add(tuple(grid))
        moves = algo.get_moves(dico, grid)
        for move in moves:
            queue, switchs = algo.heuristic_and_move(dico, grid, move, switchs, h_type, \
                    closed, ideal_grid, queue, cost)
        print_grid(stdscr, grid, dico, switchs)
        iteration += 1
    destroy_visu(stdscr)
