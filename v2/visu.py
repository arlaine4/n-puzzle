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
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    return stdscr

def destroy_visu(stdscr, mode="end"):
    if mode == "end":
        stdscr.refresh()
        stdscr.clear()
        time.sleep(1)
    stdscr.keypad(False)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

def stop_menu(pos, stdscr):
    stdscr.clear()
    stdscr.refresh()
    if pos == 14:
        stdscr.addstr(10, 10, "You selected Manual mode, starting now.")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Manual mode, starting now..")
        stdscr.refresh()
        time.sleep(1.4)
        stdscr.addstr(10, 10, "You selected Manual mode, starting now...")
        stdscr.refresh()
        time.sleep(1.4)
    elif pos == 12:
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
        if key == 259 or key is None:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(10, 10, "Select a mode for visual:", curses.A_UNDERLINE)
            stdscr.addstr(12, 12, "->  ", curses.color_pair(3))
            stdscr.addstr(12, 16, "Auto mode.", curses.A_STANDOUT)
            stdscr.addstr(14, 16, "Manual mode.")
            last_move = key
        elif key == 258:
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(10, 10, "Select a mode for visual:", curses.A_UNDERLINE)
            stdscr.addstr(14, 12, "->  ", curses.color_pair(3))
            stdscr.addstr(12, 16, "Auto mode.")
            stdscr.addstr(14, 16, "Manual mode.", curses.A_STANDOUT)
            stdscr.refresh()
            y, x = curses.getsyx()
        stdscr.refresh()
        while 1:
            key = stdscr.getch()
            stdscr.refresh()
            if key ==  259 or key == 258 or key == 111: #change this with y position and give it to stop menu
                break
        if key == 111:
            stop_menu(y, stdscr)
            break
    return last_move

def print_grid(stdscr, grid, dico, pos_nb):
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
    place_numbers_in_position(stdscr, pos_nb, None)
    stdscr.refresh()

def init_pos_nb(dico, grid):
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

def place_numbers_in_position(stdscr, pos_nb, old_pos):
    x = 12
    y = 12
    bool_standout = True
    for i in range(len(pos_nb)):
        if old_pos is not None and bool_standout is True and pos_nb[i][2] != old_pos[i][2]:
            bool_standout = False
            stdscr.addstr(pos_nb[i][0], pos_nb[i][1], str(pos_nb[i][2]), curses.A_STANDOUT)
            stdscr.refresh()
        else:
            stdscr.addstr(pos_nb[i][0], pos_nb[i][1], str(pos_nb[i][2]))
            stdscr.refresh()
        stdscr.refresh()
    stdscr.refresh()
    time.sleep(0.1)

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
    pos_nb = init_pos_nb(dico, grid)
    print_grid(stdscr, grid, dico, pos_nb)
    place_numbers_in_position(stdscr, pos_nb, None)
    ch = None
    while iteration < dico["iteration"]:
        if mode == "manual":
            ch = stdscr.getch()
        g_c, grid, parent, cost = queue.get()
        old_pos = pos_nb
        pos_nb = init_pos_nb(dico, grid)
        place_numbers_in_position(stdscr, pos_nb, old_pos)
        if grid == ideal_grid:
            old_pos = pos_nb
            pos_nb = init_pos_nb(dico, grid)
            place_numbers_in_position(stdscr, pos_nb, old_pos)
            break
        closed.add(tuple(grid))
        moves = algo.get_moves(dico, grid)
        for move in moves:
            queue, switchs = algo.heuristic_and_move(dico, grid, move, switchs, h_type, \
                    closed, ideal_grid, queue, cost)
        old_pos = pos_nb
        pos_nb = init_pos_nb(dico, grid)
        place_numbers_in_position(stdscr, pos_nb, old_pos)
        if ch == 111:
            break
        #print_grid(stdscr, grid, dico, pos_nb)
        iteration += 1
    destroy_visu(stdscr)
