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

def destroy_visu(stdscr):
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
            if key ==  259 or key == 258 or key == 111:
                break
        if key == 111:
            stop_menu(last_move, stdscr)
            break

def shortest_way_visu(grid, ideal_grid, dico, h_type):
    stdscr = init_visu()
    mode = menu_visu(stdscr)
    destroy_visu(stdscr)
