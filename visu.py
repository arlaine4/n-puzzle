import curses
import time
import sys
import Astar as a
import queue as q
import utils
import algorithm as algo

def init_visu():
    """Initialisation des proprietes du visu et des couleurs"""
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.keypad(True)
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    return stdscr

def destroy_visu(stdscr, mode):
    """Destructeur du visu pour retablir l'etat 'normal' du terminal"""
    if mode == "end":
        stdscr.refresh()
        stdscr.clear()
        time.sleep(4)
    elif mode == "stop_early" or mode == "iteration":
        stdscr.refresh()
        stdscr.clear()
        if mode == "iteration":
            stdscr.addstr(9, 10, "Iterations can't be <= 0.", curses.A_UNDERLINE)
            stdscr.refresh()
            time.sleep(1)
        stdscr.addstr(10, 10, "Stopped early, setting back terminal configuration to default.", curses.A_UNDERLINE)
        stdscr.refresh()
        time.sleep(3)
        stdscr.clear()
    stdscr.keypad(False)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

def stop_menu(pos, stdscr):
    """Menu d'apres selection du mode"""
    stdscr.clear()
    stdscr.refresh()
    if pos == 14:
        stdscr.addstr(10, 10, "You selected Slow mode, starting now.")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Slow mode, starting now..")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Slow mode, starting now...")
        stdscr.refresh()
        time.sleep(1.4)
    elif pos == 0:
        stdscr.addstr(10, 10, "You selected Fast mode, starting now.")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Fast mode, starting now..")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Fast mode, starting now...")
        stdscr.refresh()
        time.sleep(1.4)
    stdscr.clear()
    stdscr.refresh()


def menu_visu(stdscr):
    """Menu de selection du mode de resolution (manual or auto)"""
    mode = 0
    key = None
    x = 15
    y = 12
    last_move = None
    while 1:
        if key == 259 or key is None:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(10, 10, "Select a mode for visual:", curses.A_UNDERLINE)
            stdscr.addstr(12, 12, "->  ", curses.color_pair(3))
            stdscr.addstr(12, 16, "Fast mode.", curses.A_STANDOUT)
            stdscr.addstr(14, 16, "Slow mode.")
            last_move, x = curses.getsyx()
        elif key == 258:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(10, 10, "Select a mode for visual:", curses.A_UNDERLINE)
            stdscr.addstr(14, 12, "->  ", curses.color_pair(3))
            stdscr.addstr(12, 16, "Fast mode.")
            stdscr.addstr(14, 16, "Slow mode.", curses.A_STANDOUT)
            stdscr.refresh()
            last_move, x = curses.getsyx()
        stdscr.refresh()
        while 1:
            key = stdscr.getch()
            stdscr.refresh()
            if key ==  259 or key == 258 or key == 111:
                break
        if key == 111:
            stop_menu(last_move, stdscr)
            break
    return last_move

def print_grid(stdscr, grid, dico, pos_nb):
    """Tracage de la grille"""
    stdscr.clear()
    stdscr.refresh()
    x = 10
    y = 10
    size = dico["size"]
    if dico["iteration"] <= 0:
        destroy_visu(stdscr, "iteration")
        sys.exit()
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
    place_numbers_in_position(stdscr, pos_nb, "fast", None) # Placement des nombres a leur positions respecives
    stdscr.refresh()

def init_pos_nb(dico, grid):
    """Initialisation des nombres et de leurs positions x, y dans le visu
    a partir de la grid"""
    pos_nb = []
    x = 12
    y = 9
    for i in range(dico["size"] * dico["size"]):
        if i % dico["size"] == 0:
            y += 2
            x = 12
        pos_nb.append([y, x, grid[i]])
        x += 5
    return pos_nb

def place_numbers_in_position(stdscr, pos_nb, mode, old_pos):
    """Fonction qui place les nombres sur le visu en fonction de leur x et y"""
    x = 12
    y = 12
    bool_standout = True
    for i in range(len(pos_nb)):
        if old_pos is not None and bool_standout is True and pos_nb[i][2] != old_pos[i][2]: #STANDOUT si un move a ete fait
            bool_standout = False
            if len(str(pos_nb[i][2])) > 1:
                stdscr.addstr(pos_nb[i][0], pos_nb[i][1], str(pos_nb[i][2]), curses.A_STANDOUT)
            else:
                stdscr.addstr(pos_nb[i][0], pos_nb[i][1], '  ')
                stdscr.refresh()
                stdscr.addstr(pos_nb[i][0], pos_nb[i][1], str(pos_nb[i][2]), curses.A_STANDOUT)
            stdscr.refresh()
        else:
            if len(str(pos_nb[i][2])) > 1:
                stdscr.addstr(pos_nb[i][0], pos_nb[i][1], str(pos_nb[i][2]))
            else:
                stdscr.addstr(pos_nb[i][0], pos_nb[i][1], '  ')
                stdscr.refresh()
                stdscr.addstr(pos_nb[i][0], pos_nb[i][1], str(pos_nb[i][2]))
            stdscr.refresh()
        stdscr.refresh()
    stdscr.refresh()
    if mode == "slow":
        time.sleep(0.1)

def shortest_way_visu(grid, ideal_grid, dico, h_type):
    stdscr = init_visu()
    mode = menu_visu(stdscr)
    stdscr.clear()
    stdscr.refresh()
    time.sleep(2)
    if mode == 14: #position du y a la fin du visu determine le mode
        mode = "slow"
    else:
        mode = "fast"
    queue = q.PriorityQueue()
    closed = set()
    queue.put((0, grid, grid, 0))
    iteration = 0
    switchs = 0

    #--------------------------------------------------------------------
    # Preparation de la grille et des nombres pour le visu

    time.sleep(2)
    pos_nb = init_pos_nb(dico, grid)
    print_grid(stdscr, grid, dico, pos_nb)
    place_numbers_in_position(stdscr, pos_nb, mode, None)

    #
    #--------------------------------------------------------------------
    ch = None
    stdscr.nodelay(1)
    while iteration < dico["iteration"]:
        ch = stdscr.getch()
        if ch == 111:
            destroy_visu(stdscr, "stop_early")
            break
        elif ch is not None and ch != 111:
            ch = None
        g_c, grid, parent, cost = queue.get()
        old_pos = pos_nb
        pos_nb = init_pos_nb(dico, grid)
        place_numbers_in_position(stdscr, pos_nb, mode, old_pos)
        if grid == ideal_grid:
            old_pos = pos_nb
            pos_nb = init_pos_nb(dico, grid)
            place_numbers_in_position(stdscr, pos_nb, mode, old_pos)
            break
        closed.add(tuple(grid))
        moves = algo.get_moves(dico, grid)
        for move in moves:
            queue, switchs = algo.heuristic_and_move(dico, grid, move, switchs, h_type, \
                closed, ideal_grid, queue, cost)
        old_pos = pos_nb
        pos_nb = init_pos_nb(dico, grid)
        place_numbers_in_position(stdscr, pos_nb, mode, old_pos)
        if ch == 111:
            break
        iteration += 1
    if iteration >= dico["iteration"] and grid != ideal_grid:
        stdscr.addstr(10 + (dico["size"] * dico["size"]), 10 + (dico["size"] * dico["size"]), \
            "{} iterations was not enough to find the solutions.".format(dico["iteration"]))
        stdscr.refresh()
        time.sleep(1)
    if ch is None:
        destroy_visu(stdscr, "end")
